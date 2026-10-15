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

- [x] **FASE C — Menu, Rodapé, Botão de Pausa e Coerência Global (Tag: `motion-pronto`)**:
  - Implementação de navegação suave com Lenis nos links de âncora do header.
  - Botão flutuante acessível de pausa de motion no canto inferior (`#motion-toggle-btn`) com suporte a teclado, `aria-label` dinâmico e alternância ⏸ / ▶.
  - Criação do `motion-inventario.md` com mapeamento detalhado de todos os 29 efeitos e controle de concorrência de loops ($\le 2$ loops simultâneos via `IntersectionObserver`).
  - Gravação de vídeo de walkthrough completo em `screenshots/video/motion_walkthrough.webm`.
  - Regressão final de 12 viewports 100% verde (0 rolagem horizontal, 0 alvos pequenos, 0 textos cortados, 0 erros no console).


