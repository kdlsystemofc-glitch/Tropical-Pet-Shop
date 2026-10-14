# PROGRESSO.md — Tropical Pet Shop

## Status Atual: Etapa de Análise Concluída

### Concluído nesta etapa:
- [x] Leitura e síntese factual de `CLIENTE.MD` e auditoria de todas as 15 imagens reais de `imagens/`.
- [x] Análise aprofundada do mockup em `design/mockup-full.png.jpg` e criação de cópia de segurança em `design/mockup-full.png`.
- [x] Fatiamento do mockup por blocos de conteúdo limpos em `design/secoes/`:
  - `01-hero.png` (y: 0 a 330)
  - `02-servicos.png` (y: 330 a 575)
  - `03-produtos.png` (y: 575 a 895)
  - `04-avaliacoes.png` (y: 895 a 1190)
  - `05-cta-footer.png` (y: 1190 a 1376)
- [x] Criação do documento mestre `DESIGN.md`:
  - Auditoria Mockup vs. Realidade (eliminação de placeholders e fotos falsas).
  - Identificação da onda tropical orgânica e viabilidade técnica (SVG inline responsivo modular por seção).
  - Amostragem óptica de cores em HEX e auditoria de contraste WCAG 2.1 com correções aprovadas.
  - Seleção tipográfica justificadas com Google Fonts (`Plus Jakarta Sans`, `DM Sans`, `Outfit`).
  - Tabela de camadas por seção (CSS / SVG / Foto Real / Plate).
  - Especificação de motion e animações leves aceleradas por GPU.
  - Plano minucioso de imagens: slots, prompts prontos para plate e prompts de ajuste/recorte para fotos reais do cliente.
  - 4 perguntas estratégicas de negócio.
  - Checklist de pendências do cliente e mensagem pronta para WhatsApp.

### Próximos Passos:
- [ ] Aguardar retorno do usuário sobre as 4 perguntas e aprovação do plano de imagens.
- [ ] Tratamento/higienização das fotos reais em `site/assets/` conforme os prompts aprovados.
- [ ] Estruturação do HTML semântico mobile-first e CSS de design tokens.
