# Baseline de Otimização — Tropical Pet Shop

Data do Baseline: 15/10/2026  
Status Pré-Otimização: Fases de Motion Finalizadas e Aprovadas (Tag: `motion-pronto`, Commit: `91e4823`)

---

## 1. Auditoria Lighthouse Mobile (Baseline Pré-Otimização)

Auditoria realizada via Lighthouse CLI (`--form-factor=mobile`, emulação simulada 4G / CPU slow):

| Categoria | Score Pré-Otimização | Meta da Otimização |
| :--- | :---: | :---: |
| **Performance** | **60 / 100** | **$\ge$ 90 - 92 / 100** |
| **Acessibilidade** | **100 / 100** | **100 / 100** |
| **Boas Práticas** | **100 / 100** | **100 / 100** |
| **SEO** | **100 / 100** | **100 / 100** |

### Core Web Vitals (Baseline)
- **First Contentful Paint (FCP):** 3.2 s
- **Largest Contentful Paint (LCP):** 9.3 s
- **Total Blocking Time (TBT):** 130 ms (Ótimo, score 0.96)
- **Cumulative Layout Shift (CLS):** **0.000** (Zero shift, score 1.0)
- **Speed Index:** 9.1 s

---

## 2. Diagnósticos Principais para Atingir Score > 90

1. **Bloqueio de Renderização (Render-Blocking):**
   - Import externo do Google Fonts via CSS `@import url('https://fonts.googleapis.com/...')` em `tokens.css`.
   - 3 arquivos CSS externos separados (`tokens.css`, `reset.css`, `style.css`).
   - Economia potencial de FCP: ~1.300 ms.
2. **Entrega de Imagens e LCP:**
   - O cão do Hero (`hero-dog.webp`) pesa 308 KiB e tem resolução de 1122x1402px, mas em telas mobile é exibido em ~268x332px.
   - Vitrine de produtos (`products-showcase.webp`) pesa 352 KiB (2172x724px) sendo servida sem variantes responsivas menores para mobile.
   - Fotos dos serviços (1254x1254px) servidas sem `srcset`/`sizes` adequados.
   - Economia potencial de payload: ~1.615 KiB.
3. **Fontes Externas:**
   - Trocar conexão CDN externa do Google Fonts por fontes WOFF2 locais com `font-display: swap` e preload do peso principal do Hero.
4. **Minificação de CSS e JS:**
   - Inline do CSS crítico no `<head>`.
   - Carregamento assíncrono/defer do CSS restante e minificação de `motion-core.js` e `motion-sections.js`.
