# Baseline de Motion — Tropical Pet Shop

Data do Baseline: 15/10/2026  
Status Pré-Motion: Layout Estático & Passada Responsiva Aprovados (Commit: `e7df439`)

---

## 1. Auditoria Lighthouse Mobile (Baseline Oficial)

Auditoria realizada via Lighthouse CLI (`--form-factor=mobile`, emulação throttled 4G / CPU slow):

| Categoria | Score Baseline | Meta durante Motion | Tolerância Máxima |
| :--- | :---: | :---: | :---: |
| **Performance** | **37 / 100** | $\ge$ 34 / 100 | Queda máxima de 3 pontos |
| **Acessibilidade** | **100 / 100** | **100 / 100** | 0 regressão permitida |
| **Boas Práticas** | **96 / 100** | $\ge$ 96 / 100 | 0 regressão permitida |
| **SEO** | **100 / 100** | **100 / 100** | 0 regressão permitida |

### Core Web Vitals (Baseline Mobile)
- **First Contentful Paint (FCP):** 3.1 s
- **Largest Contentful Paint (LCP):** 8.5 s (cão saltando no Hero)
- **Total Blocking Time (TBT):** 2.220 ms
- **Cumulative Layout Shift (CLS):** **0.001** (Zero salto de layout)
- **Speed Index:** 5.6 s

---

## 2. Inventário de Viewports & Acessibilidade

Testado em 12 resoluções completas com 100% de sucesso (0 rolagem horizontal, 0 alvos < 44px, 0 erros no console):
- `2560x1440` (Ultra-wide)
- `1920x1080` (Desktop Full HD)
- `1440x900` (MacBook / Laptop)
- `1366x768` (Laptop corporativo)
- `1280x720` (Desktop HD)
- `1024x768` (iPad paisagem)
- `768x1024` (iPad retrato)
- `430x932` (iPhone Pro Max)
- `390x844` (iPhone moderno)
- `360x740` (Android médio)
- `320x568` (iPhone SE compacto)
- `844x390` (Celular em landscape / deitado)
- **Modos Especiais:** Zoom de texto 200% sem quebra, fallback de fontes estável, `prefers-reduced-motion` ativo, `color-scheme: light` contra inversão forçada de dark mode.

---

## 3. Diretrizes de Engenharia do Núcleo de Motion

1. **Camadas-folha exclusivas:** Apenas propriedades `transform` e `opacity` em elementos folha. Blobs orgânicos contínuos e camadas de textura permanecem fixos e sem ancestrais com filtros ou opacidade reduzida.
2. **Modos de Motion:**
   - `full`: Animações completas, stagger suave e loops controlados.
   - `reduced`: Desativa loops e parallax. Elementos aparecem com simples `fade` de 200ms ou permanecem visíveis imediatamente se `prefers-reduced-motion: reduce`.
   - `paused`: Botão flutuante acessível para congelar/retomar todas as timelines GSAP e scroll Lenis.
3. **Detecção de Qualidade (Quality Tiering):**
   - Nível `low` ativado se: `hardwareConcurrency <= 4`, `deviceMemory <= 4`, `saveData === true`, ou largura de viewport $< 768px$.
   - Em `low`: loops infinitos são desativados, flutuações e parallax são suspensos.
4. **Resiliência Acima da Dobra (Above-the-Fold):**
   - O Hero não depende de JavaScript para ser lido ou exibido. Se o script não rodar ou for bloqueado, o conteúdo é 100% legível e interativo.
5. **Carregamento Assíncrono dos Scripts:**
   - GSAP, ScrollTrigger e Lenis são auto-hospedados localmente (`site/js/vendor/`) e inicializados após o carregamento da página ou na primeira interação do usuário, garantindo que o FCP e LCP não sejam prejudicados.
