# Tropical Pet Shop — Website Institucional & Delivery

Website oficial e landing page de alta conversão para o **Tropical Pet Shop**, tradicional clínica veterinária, banho & tosa, farmácia e pet shop completo com mais de 28 anos de história na Vila Santa Luzia, em São Bernardo do Campo - SP.

Construído com foco rigoroso em **fidelidade visual ao modelo de referência**, performance extrema (**Lighthouse 93+ Mobile / 100 Desktop**), acessibilidade total (WCAG 2.1 AA/AAA), arquitetura de motion suave desacoplada e SEO Local completo com Schema.org estruturado.

---

## 1. Como Rodar o Projeto

O projeto é 100% estático, autossuficiente e auto-hospedado (sem dependência de CDNs externos nem compiladores obrigatórios para rodar em produção).

### Execução Imediata (Navegador)
- Dê um duplo clique no arquivo [`index.html`](file:///c:/Oficial/Tropical%20Pet%20Shop/index.html) para abrir diretamente pelo protocolo `file://`. Todos os estilos, fontes locais e scripts funcionam nativamente sem quebrar.

### Servidor Local (Recomendado para Testes de Rede)
Utilizando o servidor HTTP nativo do Python:
```bash
python -m http.server 8000
```
Ou via Node.js:
```bash
npx serve .
```
Acesse no navegador: `http://localhost:8000`.

### Requisitos para Scripts de Auditoria (Opcional para Desenvolvedores)
Para rodar os testes automatizados de regressão em 14 resoluções e Lighthouse:
- Python 3.10+ com `playwright` (`pip install playwright && playwright install chromium webkit`)
- Node.js 18+ com `lighthouse` CLI

---

## 2. Estrutura do Repositório

```text
├── index.html                   # HTML semântico com Critical CSS inline e SEO estruturado
├── cliente.config.json          # Painel central de dados pendentes do cliente e domínio
├── PENDENCIAS-CLIENTE.md        # Lista detalhada de pendências e o impacto de cada resolução
├── ROTEIRO-APARELHO-REAL.md     # Roteiro prático de testes manuais em iPhone e Android
├── DESIGN.md                    # Especificação visual, leitura do mockup, WCAG e tokens
├── DEPLOY.md                    # Recomendações de headers HTTP de cache, compressão e segurança
├── robots.txt                   # Diretrizes de indexação para robôs de busca
├── sitemap.xml                  # Mapa de URLs no formato XML 0.9 padrão
├── site.webmanifest             # Manifesto PWA com ícones e tema da marca
├── favicon.ico                  # Favicon multi-resolução para navegadores
│
├── site/
│   ├── assets/                  # Imagens WebP responsivas em múltiplos degraus e favicons
│   │   ├── hero-dog-*.webp      # Hero do pet em 400w, 600w e 800w
│   │   ├── service-*.webp       # Fotos reais higienizadas e tratadas da Dra. Vânia e serviços
│   │   ├── products-*.webp      # Produtos autênticos (Premier, Golden, Churu, Kong)
│   │   ├── og-image.jpg         # Imagem para Open Graph e WhatsApp em 1200x630px
│   │   └── noise.png            # Textura granulada tátil de papel
│   ├── css/
│   │   ├── style.css            # Folha de estilo completa comentada e documentada
│   │   ├── style.min.css        # Folha de estilo unificada e minificada
│   │   └── critical.css         # CSS crítico acima da dobra para renderização instantânea
│   ├── fonts/                   # Fontes Google Fonts auto-hospedadas em WOFF2 moderno
│   │   ├── plus-jakarta-sans-*  # Família tipográfica dos títulos display
│   │   └── dm-sans-*            # Família tipográfica para corpo de texto e botões
│   └── js/
│       ├── motion-core.js       # Núcleo de orquestração de motion (modos full, reduced, paused)
│       ├── motion-sections.js   # Timelines e triggers por seção do site
│       └── vendor/              # Bibliotecas de animação locais (GSAP, ScrollTrigger, Lenis)
│
├── scripts/                     # Suíte de automação, auditoria, testes e build
│   ├── run_full_audit.py        # Auditoria completa em 14 resoluções, WebKit, Motion e Lighthouse
│   ├── rebuild_client_data.py   # Injeta dados de cliente.config.json no index.html e sitemap
│   ├── build_css.py             # Minificador e separador de CSS crítico
│   ├── generate_favicons.py     # Gerador automatizado de favicons e ícones PWA
│   └── generate_og_image.py     # Gerador da imagem de compartilhamento social 1200x630
│
├── design/                      # Mockups e fatias de referência original
└── imagens/                     # Acervo fotográfico bruto original fornecido pelo cliente
```

---

## 3. Decisões de Design & Arquitetura

Para detalhes aprofundados, consulte o [`DESIGN.md`](file:///c:/Oficial/Tropical%20Pet%20Shop/DESIGN.md). Principais pilares arquiteturais:

- **Fidelidade ao Conceito Visual**: Fundo creme acolhedor (`#FAF6F0`), tipografia editorial forte e elegante, textura de papel realçada com ruído suave (`noise.png`) e grandes formas orgânicas tropicais recortadas sem distorções horizontais.
- **Acessibilidade Universal (WCAG 2.1)**: Todos os contrastes de texto respeitam o nível AA/AAA. Os alaranjados de destaque foram calibrados para `--color-orange-text: #C84C00` (4.71:1 sobre branco) e botões escuros/contrastados para leitura sem fadiga visual.
- **Motion Respeitoso e Performático**:
  - Camadas exclusivas de `transform` e `opacity` sem repaints em blocos contínuos.
  - Três modos integrados: **Full**, **Reduced Motion** (`prefers-reduced-motion: reduce`) e **Pausado** (botão flutuante acessível no rodapé `#motion-toggle-btn`).
  - Suporte a rolagem suave via Lenis desacoplado da renderização principal.
- **Performance e Core Web Vitals**:
  - Imagens com degraus de resolução (`srcset`) e dimensões explícitas para **CLS = 0**.
  - Fontes locais em formato WOFF2 com `font-display: swap` e preload estrito apenas dos pesos acima da dobra.
  - Critical CSS inline no `<head>` e carregamento de motion diferido para eliminar bloqueio de renderização (**TBT = 0ms**).

---

## 4. Licenças e Créditos de Terceiros

| Recurso | Desenvolvedor / Autoria | Licença | Uso no Projeto |
| :--- | :--- | :--- | :--- |
| **GSAP 3 & ScrollTrigger** | [GreenSock](https://greensock.com/) | Standard "No-Charge" GreenSock License | Animações de entrada e revelação de cards |
| **Lenis** | [Darkroom Engineering / Studio Freight](https://lenis.darkroom.engineering/) | MIT License | Rolagem suave (*smooth scrolling*) |
| **Plus Jakarta Sans** | Tokotype (Gumpita Rahayu) | SIL Open Font License 1.1 (OFL) | Tipografia principal de títulos e números |
| **DM Sans** | Colophon Foundry (Google Fonts) | SIL Open Font License 1.1 (OFL) | Tipografia secundária e corpo de leitura |

---

## 5. Aviso Ético e Técnico sobre Imagens

Em consonância com as boas práticas de integridade e transparência:
- **Fotos Reais e Autênticas**: O site utiliza fotos reais do acervo original da Tropical Pet Shop (`imagens/`), incluindo os produtos autênticos das marcas **Premier Pet**, **Golden Formula** e **Churu**, além do registro fotográfico genuíno da **Dra. Vânia** em atendimento clínico e resultados do salão de tosa.
- **Plates e Elementos Gerados/Recriados por IA**: O cão Jack Russell do Hero e ambientações de apoio foram gerados/recriados via inteligência artificial para atender rigorosamente à composição dinâmica e à linguagem estética proposta no mockup de referência.
- **Substituição Fácil**: Caso o cliente opte no futuro por substituir qualquer uma dessas imagens por fotografias autorais adicionais da sua loja física, basta atualizar os arquivos indicados em `cliente.config.json`.

---

## 6. Como Atualizar Dados Quando Chegarem do Cliente

Todas as pendências comerciais e legais (domínio final, CRMV da Dra. Vânia, CNPJ, horários de atendimento) estão documentadas em [`PENDENCIAS-CLIENTE.md`](file:///c:/Oficial/Tropical%20Pet%20Shop/PENDENCIAS-CLIENTE.md).

Para atualizar:
1. Abra o arquivo [`cliente.config.json`](file:///c:/Oficial/Tropical%20Pet%20Shop/cliente.config.json).
2. Preencha os campos com os dados definitivos.
3. Execute o comando:
   ```bash
   python scripts/rebuild_client_data.py
   ```
4. O script atualizará de forma automática as tags canônicas, metadados sociais, sitemap, robots e dados cadastrais no rodapé.
