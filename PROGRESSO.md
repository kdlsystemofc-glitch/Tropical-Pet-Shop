## Status Atual: Fases de Motion Concluídas (Tag: motion-pronto)

### Concluído:
- [x] **FASE A — Base Global de Motion (Tag: `motion-base`)**:
  - Auditoria inicial Lighthouse e baseline (`motion-baseline.md`).
  - Instalação e auto-hospedagem de scripts clássicos em `site/js/vendor/` (`gsap.min.js`, `ScrollTrigger.min.js`, `lenis.min.js`).
  - Núcleo de motion em `site/js/motion-core.js` com 3 modos (`full`, `reduced`, `paused`), detecção de qualidade (`high`, `low`), suporte desacoplado ao Lenis, e ciclo de vida de visibilidade de abas.
  - Regressão de 12 viewports aprovada (0 erros).

- [x] **FASE B — Animação Seção por Seção**:
  - **Seção 01 (Hero)**: Entrada escalonada dos títulos e texto, pouso com leve salto no cão Jack Russell e selo de entrega rápida, loops de flutuação e parallax de rolagem. Commit `motion: secao 01 hero animada`.
  - **Seção 02 (Serviços)**: Entrada suave dos 3 cards em formato cápsula a 35% de visibilidade com micro-parallax diferencial no desktop. Commit `motion: secao 02 servicos animada`.
  - **Seção 03 (Produtos)**: Entrada coordenada do showcase de rações super premium e sub-grid dos 4 produtos, com micro-flutuação das embalagens e parallax leve. Commit `motion: secao 03 produtos animada`.
  - **Seção 04 (Avaliações)**: Entrada em estilo balões de fala, pop-in das fotos do Golden Retriever e Labrador polaroid com rotação, loops contínuos de respiração e balanço suave. Commit `motion: secao 04 avaliacoes animada`.
  - **Seção 05 (CTA / Rodapé)**: Entrada do título, metadados e botão de WhatsApp com respiração periódica suave para guiar a conversão final. Commit `motion: secao 05 cta-footer animada`.
  - Lighthouse mobile pós-motion atingiu **Performance 63/100** (superior ao baseline de 37/100 devido a `fetchpriority="high"` e `width`/`height` explícitos), Acessibilidade 100/100, Boas Práticas 100/100, SEO 100/100.

- [x] **ETAPA DE OTIMIZAÇÃO (Tag: `otimizacao-pronta`)**:
  - Fontes auto-hospedadas locais em WOFF2 moderno com font-display swap e preload seletivo.
  - CSS unificado, Critical CSS inline no head e carregamento não bloqueante de estilos secundários.
  - Imagens WebP responsivas em múltiplos degraus com sizes precisos por breakpoint.
  - Scripts de motion carregados sob demanda após o load/primeira interação.
  - Documentação completa de cache e segurança em DEPLOY.md.
  - Lighthouse Mobile atingiu **Performance 92/100**.

- [x] **ETAPA DE SEO LOCAL (Tag: `seo-pronto`)**:
  - Title e meta description específicos para São Bernardo do Campo com serviços principais e Dra. Vânia.
  - Imagem Open Graph e Twitter Cards em 1200x630px gerada com a composição aprovada da marca.
  - Schema.org JSON-LD estruturado (`PetStore` e `VeterinaryCare`) com dados confirmados e comentários de salvaguarda.
  - Configuração central em `seo.config.json` e arquivos `robots.txt`, `sitemap.xml`, `site.webmanifest` e favicons gerados.
  - Semântica validada: exatamente um `<h1>`, hierarquia de `<h2>` e `alt` em todas as imagens informativas.

- [x] **RODADA FINAL & ENTREGA CONSOLIDADA (Tag: `v1.0.0`)**:
  - Auditoria em 14 resoluções de tela (incluindo 4K 3840x2160 e Ultrawide 3440x1440) no Chromium: 100% PASS.
  - Auditoria no motor WebKit (Safari engine) em desktop, tablet e mobile: 100% PASS.
  - Validação dos 3 modos de motion (Full, Reduced e Pausado com alternância acessível): 100% PASS.
  - Lighthouse Mobile: **93 Performance / 100 Acessibilidade / 100 Boas Práticas / 100 SEO**.
  - Lighthouse Desktop: **100 Performance / 100 Acessibilidade / 100 Boas Práticas / 100 SEO**.
  - Painel de configuração centralizado em `cliente.config.json` e script de reconstrução em `scripts/rebuild_client_data.py`.
  - Documentos de entrega gerados: `PENDENCIAS-CLIENTE.md`, `README.md`, `ROTEIRO-APARELHO-REAL.md`.


