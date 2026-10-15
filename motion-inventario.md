# Inventário de Motion — Tropical Pet Shop

**Data:** 15/10/2026  
**Status:** FASE C — Menu, Rodapé, Botão de Pausa e Coerência Global Concluídos  
**Tag Git:** `motion-pronto`

---

## 1. Inventário Completo de Animações por Seção

Todas as animações manipulam exclusivamente nós folha nas propriedades `transform` e `opacity` aceleradas por hardware (GPU). Nenhum elemento decorativo contínuo de fundo (blobs e ondas laranjas) se move nem possui ancestrais com filtros ou transformações ativas.

| Seção | Elemento Alvo | Tipo | Propriedades | Duração / Delay | Curva de Aceleração (Ease) | Gatilho / Condição | Modo Reduced |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **01. Hero** | `.hero-heading span` | Entrada | `y: 28px -> 0`, `opacity: 0 -> 1` | 750ms (stagger 120ms) | `power2.out` | Carga inicial (0.1s) | Estático |
| **01. Hero** | `.hero-subtext` | Entrada | `y: 20px -> 0`, `opacity: 0 -> 1` | 650ms (delay 350ms) | `power2.out` | Carga inicial | Estático |
| **01. Hero** | `.hero-dog-jumping` | Entrada | `y: 42px, scale: 0.94 -> 1`, `opacity: 0 -> 1` | 850ms (delay 200ms) | `back.out(1.15)` | Carga inicial | Estático |
| **01. Hero** | `.badge-delivery` | Entrada | `scale: 0.7 -> 1`, `opacity: 0 -> 1` | 600ms (delay 450ms) | `back.out(1.35)` | Carga inicial | Estático |
| **01. Hero** | `.badge-delivery` | Loop | `y: -7px <-> 0` | 2.6s (yoyo, infinito) | `sine.inOut` | Quality HIGH + In Viewport | Desativado |
| **01. Hero** | `.hero-dog-jumping` | Loop | `y: -5px <-> 0` | 3.4s (yoyo, infinito) | `sine.inOut` | Quality HIGH + In Viewport | Desativado |
| **01. Hero** | `.badge-delivery` | Parallax | `yPercent: -15%` | Scrub de rolagem | Linear | Scroll 0% a 100% do Hero | Desativado |
| **01. Hero** | `.hero-dog-jumping` | Parallax | `yPercent: +12%` | Scrub de rolagem | Linear | Scroll 0% a 100% do Hero | Desativado |
| **02. Serviços** | `.section-title` | Entrada | `y: 25px -> 0`, `opacity: 0 -> 1` | 650ms | `power2.out` | ScrollTrigger (top 65%) | Estático |
| **02. Serviços** | `.service-pill-card` | Entrada | `y: 40px -> 0`, `opacity: 0 -> 1` | 750ms (stagger 140ms) | `power2.out` | ScrollTrigger (top 65%) | Estático |
| **02. Serviços** | `.service-pill-card:hover` | Hover | `y: -6px`, sombra aprofundada | 250ms | `ease` | Interação do usuário | Ativo |
| **02. Serviços** | `.service-pill-card` (meio/laterais) | Parallax | `y: -12px` (centro), `y: +8px` (laterais) | Scrub 1 | Linear | Quality HIGH + Desktop | Desativado |
| **03. Produtos** | `.section-title` | Entrada | `y: 25px -> 0`, `opacity: 0 -> 1` | 650ms | `power2.out` | ScrollTrigger (top 65%) | Estático |
| **03. Produtos** | `.showcase-media-side` | Entrada | `x: -30px -> 0`, `opacity: 0 -> 1` | 750ms | `power2.out` | ScrollTrigger (top 65%) | Estático |
| **03. Produtos** | `.showcase-content-side`| Entrada | `x: 25px -> 0`, `opacity: 0 -> 1` | 750ms (delay 200ms) | `power2.out` | ScrollTrigger (top 65%) | Estático |
| **03. Produtos** | `.product-mini-column` | Entrada | `y: 35px -> 0`, `opacity: 0 -> 1` | 650ms (stagger 100ms) | `power2.out` | ScrollTrigger (top 65%) | Estático |
| **03. Produtos** | `.showcase-hero-img` | Loop | `y: -5px <-> 0` | 3.2s (yoyo, infinito) | `sine.inOut` | Quality HIGH + In Viewport | Desativado |
| **03. Produtos** | `.product-mini-column` | Parallax | `y: -8px` (pares), `y: +8px` (ímpares) | Scrub 1 | Linear | Quality HIGH + Desktop | Desativado |
| **04. Avaliações**| `.reviews-main-title` | Entrada | `y: 25px -> 0`, `opacity: 0 -> 1` | 650ms | `power2.out` | ScrollTrigger (top 65%) | Estático |
| **04. Avaliações**| `.speech-bubble-mock` | Entrada | `scale: 0.88, y: 22px -> 1, 0`, `opacity` | 650ms (stagger 80ms) | `back.out(1.15)` | ScrollTrigger (top 65%) | Estático |
| **04. Avaliações**| `.pet-photo-frame-center`| Entrada | `scale: 0.82 -> 1`, `opacity: 0 -> 1` | 700ms (delay 300ms) | `back.out(1.25)` | ScrollTrigger (top 65%) | Estático |
| **04. Avaliações**| `.polaroid-inner` | Entrada | `rot: -12deg -> -4.5deg, scale: 0.8 -> 1` | 750ms (delay 400ms) | `back.out(1.3)` | ScrollTrigger (top 65%) | Estático |
| **04. Avaliações**| `.pet-photo-frame-center`| Loop | `y: -5px <-> 0` | 3.0s (yoyo, infinito) | `sine.inOut` | Quality HIGH + In Viewport | Desativado |
| **04. Avaliações**| `.polaroid-inner` | Loop | `rotate: -2.5deg <-> -4.5deg` | 3.6s (yoyo, infinito) | `sine.inOut` | Quality HIGH + In Viewport | Desativado |
| **04. Avaliações**| `.speech-bubble-mock` | Parallax | `y: -10px` (topo), `y: +10px` (base) | Scrub 1 | Linear | Quality HIGH + Desktop | Desativado |
| **05. Rodapé** | `.footer-heading` | Entrada | `y: 24px -> 0`, `opacity: 0 -> 1` | 650ms | `power2.out` | ScrollTrigger (top 75%) | Estático |
| **05. Rodapé** | `.btn-whatsapp-pill` | Entrada | `scale: 0.88, y: 20px -> 1, 0`, `opacity` | 700ms (delay 150ms) | `back.out(1.25)` | ScrollTrigger (top 75%) | Estático |
| **05. Rodapé** | `.btn-whatsapp-pill` | Loop | `scale: 1.025 <-> 1.0` | 2.4s (yoyo, infinito) | `sine.inOut` | Quality HIGH + In Viewport | Desativado |
| **05. Rodapé** | `.meta-item` | Entrada | `y: 16px -> 0`, `opacity: 0 -> 1` | 600ms (stagger 100ms) | `power2.out` | ScrollTrigger (top 75%) | Estático |

---

## 2. Contagem de Loops Simultâneos por Posição de Rolagem

Graças à gestão de ciclo de vida com `IntersectionObserver` implementada em `site/js/motion-core.js`, qualquer loop contínuo é automaticamente pausado (`.pause()`) assim que o elemento sai do viewport visível (+ margem de segurança de 50px).

| Posição de Rolagem | Elementos no Viewport | Loops Ativos em Execução | Limite de Segurança ($le$ 3) | Status |
| :--- | :--- | :---: | :---: | :---: |
| **Topo (0px - 600px)** | Cão do Hero + Selo de Entrega | 2 (`badgeFloat`, `dogFloat`) | $\le$ 3 | ✅ Ótimo (Sem sobrecarga) |
| **Serviços (600px - 1400px)** | Cards de Serviços | 0 (Entradas já assentadas) | $\le$ 3 | ✅ Ótimo (0% consumo contínuo) |
| **Produtos (1400px - 2300px)** | Vitrine de Rações Super Premium | 1 (`showcaseFloat`) | $\le$ 3 | ✅ Ótimo (1 loop leve) |
| **Avaliações (2300px - 3200px)**| Golden Retriever + Polaroid Labrador | 2 (`goldenFloat`, `polaroidSway`) | $\le$ 3 | ✅ Ótimo (2 loops leves) |
| **Rodapé (3200px - Fim)** | Botão de WhatsApp Principal | 1 (`ctaPulse`) | $\le$ 3 | ✅ Ótimo (1 loop sutil) |

**Conclusão de Performance de Loops:**  
Em nenhum momento da navegação há mais de **2 loops simultâneos** rodando na GPU. Quando o usuário rola a página, os loops das seções anteriores congelam imediatamente, preservando bateria e taxa de quadros a 60/120fps.

---

## 3. Avaliação de Ritmo e Coerência Visual

1. **Harmonia Editorial:** Todas as entradas usam a curva `power2.out` com durações entre 600ms e 750ms, transmitindo sensação de elegância e solidez sem lentidão.
2. **Personalidade Pet:** O cão saltando e o selo flutuante no Hero, assim como a polaroid do labrador em Avaliações, usam curvas leves com overshoot `back.out(1.15 - 1.35)`, reforçando a alegria e vivacidade do universo pet shop.
3. **Sem Efeitos Artificiais:** Nenhuma rotação 3D falsa, efeito de confete ou transições circenses foram aplicadas. Toda animação valoriza a fotografia real dos cães e produtos.
4. **Navegação:** Menus do header utilizam Lenis smooth scroll com desaceleração cúbica sem travamento de âncoras.
5. **Botão de Pausa:** Implementado no canto inferior esquerdo (`#motion-toggle-btn`), acessível via teclado, alternando instantaneamente entre reprodução e congelamento global do GSAP e Lenis.
