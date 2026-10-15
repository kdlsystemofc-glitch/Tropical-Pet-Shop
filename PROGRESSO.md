## Status Atual: FASE A — Base Global de Motion Concluída (Tag: motion-base)

### Concluído:
- [x] Construção do layout semântico e passada responsiva geral nas 12 resoluções oficiais (Commit `responsivo pronto`).
- [x] Auditoria inicial Lighthouse e criação do `motion-baseline.md` (Mobile Perf: 37, A11y: 100, BP: 96, SEO: 100).
- [x] Instalação e auto-hospedagem local dos scripts clássicos em `site/js/vendor/` (`gsap.min.js`, `ScrollTrigger.min.js`, `lenis.min.js`).
- [x] Criação do núcleo de motion em `site/js/motion-core.js`:
  - 3 modos de motion: `full`, `reduced` (respeitando `prefers-reduced-motion`) e `paused` (freeze/resume com Page Visibility API).
  - Detecção de qualidade de hardware (`high` / `low` via `hardwareConcurrency`, `deviceMemory`, `saveData` e largura de tela).
  - Suporte desacoplado para Lenis smooth scroll sincronizado com GSAP Ticker.
  - Framework declarativo para `data-reveal`, `data-parallax` e `data-loop` com auto-pausa de loops fora da tela (`IntersectionObserver`).
  - Nenhuma seção animada ainda na Fase A (tudo 100% visível estaticamente acima e abaixo da dobra).
- [x] Regressão completa de testes Playwright aprovada em 12/12 viewports (0 erros no console, 0 rolagem horizontal, 0 quebras).

### Próximos Passos:
- [ ] **FASE B**: Animar cada seção em ordem (`#hero`, `#servicos`, `#produtos`, `#avaliacoes`, `#cta-footer`), medindo impacto, empilhamento e Lighthouse a cada passo.
- [ ] **FASE C**: Menu, rodapé, botão flutuante de pausa acessível e inventário final de loops (`motion-inventario.md`).

