#!/usr/bin/env python3
"""
rebuild_client_data.py — Reconstrutor Automático de Metadados e SEO Local
Tropical Pet Shop

Lê 'cliente.config.json' e aplica automaticamente no index.html, sitemap.xml e robots.txt
todos os dados fornecidos pelo cliente (Domínio, CNPJ, Razão Social, CRMV, Horários).
"""

import os
import re
import json

def rebuild():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(root_dir, 'cliente.config.json')
    index_path = os.path.join(root_dir, 'index.html')
    sitemap_path = os.path.join(root_dir, 'sitemap.xml')
    robots_path = os.path.join(root_dir, 'robots.txt')

    if not os.path.exists(config_path):
        print(f"Erro: Arquivo de configuração '{config_path}' não encontrado.")
        return

    with open(config_path, 'r', encoding='utf-8') as f:
        cfg = json.load(f)

    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    dominio = cfg.get('dominio', {}).get('url', '').strip().rstrip('/')
    legal = cfg.get('identificacao_legal', {})
    cnpj = legal.get('cnpj', '').strip()
    razao = legal.get('razaoSocial', '').strip()
    vet = cfg.get('responsavel_tecnica_veterinaria', {})
    crmv = vet.get('crmv', '').strip()
    horarios = cfg.get('horarios_funcionamento', {})

    print(f"Lendo configurações de: {config_path}")
    print(f"  - Domínio: '{dominio}'" if dominio else "  - Domínio: [PENDENTE / VAZIO]")
    print(f"  - CNPJ: '{cnpj}'" if cnpj else "  - CNPJ: [PENDENTE / VAZIO]")
    print(f"  - CRMV: '{crmv}'" if crmv else "  - CRMV: [PENDENTE / VAZIO]")

    # 1. Atualizar Domínio e Tags Canônicas
    if dominio:
        # Canonical tag
        html = re.sub(
            r'<!--\s*<link rel="canonical" href="[^"]*">\s*-->|<link rel="canonical" href="[^"]*">',
            f'<link rel="canonical" href="{dominio}/">',
            html
        )
        # Open Graph URL
        html = re.sub(
            r'<!--\s*<meta property="og:url" content="[^"]*">\s*-->|<meta property="og:url" content="[^"]*">',
            f'<meta property="og:url" content="{dominio}/">',
            html
        )
        # Open Graph Image Absoluta
        html = re.sub(
            r'<!--\s*<meta property="og:image:secure_url" content="[^"]*">\s*-->|<meta property="og:image:secure_url" content="[^"]*">',
            f'<meta property="og:image:secure_url" content="{dominio}/site/assets/og-image.jpg">',
            html
        )
        # Twitter Image Absoluta
        html = re.sub(
            r'<meta name="twitter:image" content="[^"]*">',
            f'<meta name="twitter:image" content="{dominio}/site/assets/og-image.jpg">',
            html
        )
        print("  ✓ Tags canônicas, og:url e og:image absoluta ativadas com sucesso!")

        # Atualizar sitemap.xml
        if os.path.exists(sitemap_path):
            with open(sitemap_path, 'r', encoding='utf-8') as f:
                sitemap_content = f.read()
            sitemap_content = re.sub(
                r'<loc>https?://[^<]+</loc>',
                f'<loc>{dominio}/</loc>',
                sitemap_content
            )
            with open(sitemap_path, 'w', encoding='utf-8') as f:
                f.write(sitemap_content)
            print("  ✓ sitemap.xml atualizado com o domínio definitivo!")

        # Atualizar robots.txt
        if os.path.exists(robots_path):
            with open(robots_path, 'r', encoding='utf-8') as f:
                robots_content = f.read()
            robots_content = re.sub(
                r'#?\s*Sitemap:\s*https?://[^\n]+',
                f'Sitemap: {dominio}/sitemap.xml',
                robots_content
            )
            with open(robots_path, 'w', encoding='utf-8') as f:
                f.write(robots_content)
            print("  ✓ robots.txt atualizado com a diretiva Sitemap oficial!")

    # 2. Atualizar Rodapé com Dados Legais (CNPJ & Razão Social)
    if cnpj or razao:
        legal_text = "© 2026 Tropical Pet Shop. Todos os direitos reservados. 28 anos de tradição e amor em São Bernardo do Campo."
        extra = []
        if razao:
            extra.append(razao)
        if cnpj:
            extra.append(f"CNPJ: {cnpj}")
        if crmv:
            extra.append(f"Resp. Técnica: Dra. Vânia ({crmv})")
        
        full_footer_copy = f"{legal_text}<br><span class=\"legal-registry\">{' | '.join(extra)}</span>"
        html = re.sub(
            r'<div class="footer-bottom-copy">\s*<p>.*?</p>\s*</div>',
            f'<div class="footer-bottom-copy">\n          <p>{full_footer_copy}</p>\n        </div>',
            html,
            flags=re.DOTALL
        )
        print("  ✓ Rodapé atualizado com informações cadastrais e regulatórias!")

    # 3. Salvar index.html
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print("\nReconstrução concluída! O site está sincronizado com 'cliente.config.json'.")

if __name__ == '__main__':
    rebuild()
