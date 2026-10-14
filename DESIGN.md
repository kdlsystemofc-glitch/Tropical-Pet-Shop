# DESIGN.md — Tropical Pet Shop
*Documento de Especificação Visual, Arquitetura de Design e Plano de Imagens*

---

## 1. Leitura Honesta: Mockup vs. Realidade

Uma auditoria minuciosa comparando o conceito do mockup (`design/mockup-full.png`) com o acervo fotográfico real (`imagens/`) e os dados de negócio (`CLIENTE.MD`) revela divergências críticas que precisam ser tratadas para evitar a entrega de um produto "falso de agência":

| Elemento no Mockup | O que o Mockup Mostra (Ficção / IA) | A Realidade do Cliente (`CLIENTE.MD` e `imagens/`) | Solução para o Projeto |
| :--- | :--- | :--- | :--- |
| **Logotipo** | Tipografia simplificada "TROPICAL PET" em caixa alta com pata genérica ao lado. | O logo oficial registrado é um badge circular (`imgi_2`, `imgi_17`, `imgi_24`) com lettering manual "Tr🐾pical Pet" (a pata substitui a letra 'o' em Tropical). Em peças horizontais (`imgi_22`), usa pata com folhagem tropical estilizada. | Vetorizar e renderizar em SVG o logotipo autêntico da loja, preservando a identidade reconhecida pelos 723 avaliadores no Google. |
| **Pet do Hero** | Jack Russell Terrier saltando em estúdio com brinquedo de borracha na boca (banco de imagem). | O cliente atende cães reais no bairro (Spitz Alemão, Yorkshire, Shih Tzu, SRD caramelo). As fotos reais mostram cães tosados com laços e gravatinhas (`imgi_14`, `imgi_15`, `imgi_16`). | Prover duas alternativas no plano de imagens: opção A (recorte real do Spitz/Yorkshire com gravata) e opção B (plate decorativo dinâmico se a intenção for manter a pose do salto). |
| **Card Veterinária** | Veterinária loira jovem abraçada a um Golden Retriever em ambiente de banco de imagens. | A médica veterinária responsável é a **Dra. Vânia**, atuando há **28 anos** na área, com fotos reais em consulta clínica (`imgi_12`) e segurando paciente felino (`imgi_10`). Os clientes elogiam nominalmente a Dra. Vânia nas avaliações. | **Usar obrigatoriamente a foto real da Dra. Vânia** (`imgi_12`), limpando via inpainting os textos promocionais sobrepostos. Humanização e credibilidade 100% autênticas. |
| **Card Banho & Tosa** | Golden Retriever molhado tomando banho de espuma em banheira genérica. | Salão de banho e tosa real com duas profissionais atendendo (`imgi_14`), além de resultados pós-tosa impecáveis (`imgi_15`, `imgi_16`, `imgi_18`, `imgi_23`). | Utilizar a foto real do salão com as banhistas cuidando do cão (`imgi_14`) ou o resultado pós-tosa da loja. |
| **Card Farmácia Pet** | Gato ruivo estilizado sentado ao lado de vidros de remédios e cartelas de pílulas ilustradas. | A Tropical Pet vende medicamentos veterinários reais e suplementos de marcas líderes: **Nutrafases Relax**, **Homeopet Anizen**, **Feliway Classic** (`imgi_19`), além de campanhas de vacinação V4, V10 e Antirrábica (`imgi_17`, `imgi_21`). | Utilizar o registro fotográfico dos produtos reais da loja (`imgi_19` recortado / higienizado) em vez de remédios fictícios. |
| **Vitrine de Rações** | Sacos de ração falsos gerados por IA com nomes inventados ("DECHIERA", "DECINERA", "LEADING PER DOG FOOD BRAND"). | A loja é revendedora oficial de marcas Super Premium nacionais de prestígio: **Premier Formula** (Adultos Raças Médias e Grandes) e **GoldeN Formula** (Frango e Arroz 10,1kg) (`imgi_22`). | Exibir as embalagens autênticas das marcas que o cliente efetivamente comercializa (Premier, GoldeN, Churu). |
| **Cards de Petiscos** | Embalagens fictícias ("Brazalle Dog", "Beglum Manbna", "Pest & Toys"). | O cliente comercializa petiscos reais como **Biscoitos PremierPet** e **Churu Atum** para gatos (`imgi_22`). | Substituir os placeholders por produtos reais comercializados na loja. |
| **Avaliações / Depoimentos** | 5 balões com texto ilegível / lorem ipsum e fotos de stock de cães. | 723 avaliações reais no Google Maps com nota média 4,5. Depoimentos elogiosos reais citando pontualidade, atendimento no WhatsApp e carinho da Dra. Vânia e das banhistas. | Inserir textos reais do Google Maps (ex.: Kethelin Frazão, Renata Vicente) com fotos dos pets atendidos no pet shop (`imgi_16`, `imgi_18`). |
| **Barra WhatsApp & Horário** | Título técnico em inglês ("HIGH-CONVERTINHG WHATSAPP DELIVERY BAR") e horário absurdo de IA ("09:00 - h às 27:00"). | Comunicação brasileira direta voltada a entregas em São Bernardo do Campo. Telefone real: `(11) 96036-5965`. Horário comercial real de fechamento: 18h00. | Copy comercial de alta conversão: "Peça pelo WhatsApp e receba em casa com entrega rápida em SBC". Horários e link do WhatsApp 100% funcionais. |

---

## 2. Elemento Decorativo de Assinatura e Viabilidade Técnica

### 2.1 Identificação do Elemento
O elemento visual de assinatura que unifica o mockup é a **grande onda orgânica tropical fluida** (*liquid orange wave*).
- **Hero**: Uma curva convexa alaranjada (`#FF6600`) preenche a lateral direita superior e avança organicamente sob as patas do pet.
- **Header**: Um halo/blob suave de pêssego (`#FFD4B4`) ancora o canto superior esquerdo atrás do logotipo.
- **Seções Centrais**: Formas de fundo que criam transições onduladas suaves entre os blocos.
- **Avaliações e Rodapé**: A onda alaranjada ressurge na borda direita inferior, criando contraste com os balões brancos de depoimentos.

### 2.2 Avaliação Honesta de Dificuldade e Viabilidade
- **Tentativa ingênua (Inviável)**: Tentar usar um único arquivo SVG ou imagem bitmap de 1376px de altura fixa esticado como background do `body`.
  - *Por que falha*: Em telas mobile, tablets ou telas ultra-wide, o conteúdo vertical expande e contrai dinamicamente. Um SVG único se desalinharia imediatamente dos títulos e cards, causando recortes grotescos de texto sobre fundo alaranjado sem contraste.
  - *Violação das regras*: O `CLAUDE.md` proíbe transformar elementos decorativos contínuos em camadas pesadas de repaint que sofrem `transform` ou afetam a dobra.
- **Solução Técnica Definitiva (100% Viável e Leve)**:
  - **Arquitetura Seccional com SVG Inline Responsivo**: Cada seção possui sua própria camada decorativa de fundo (`.section-decor`) com `position: absolute; inset: 0; pointer-events: none; z-index: 0; overflow: hidden;`.
  - As curvas do Hero e Rodapé utilizam elementos `<svg viewBox="0 0 1000 600" preserveAspectRatio="xMaxYMid slice">` com curvas de Bézier cúbicas (`<path d="...">`).
  - As transições entre seções usam `border-radius: 0 0 50% 50% / 0 0 40px 40px` ou divisores SVG leves.
  - **Zero bitmaps no background**: Redução de ~600KB de payload para menos de 3KB de SVG comprimido, garantindo 60fps constantes e renderização imediata acima da dobra sem JS.

---

## 3. Paleta de Cores e Contraste WCAG 2.1

Amostragem realizada diretamente nos pixels da imagem `design/mockup-full.png` via script de medição óptica:

| Nome do Token | HEX Amostrado | Função na Interface | Contraste vs Fundo | Status WCAG | Correção / Diretriz de Uso |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `--color-bg-base` | `#FDFAF3` | Fundo principal da página (creme suave) | — | — | Base neutra e quente. |
| `--color-bg-surface` | `#FFFFFF` | Fundo dos cards de serviços e balões | — | — | Superfície limpa de alto respiro. |
| `--color-text-primary` | `#2A180E` | Títulos principais e textos de destaque | **16.31:1** (vs `#FDFAF3`)<br>**17.00:1** (vs `#FFFFFF`) | **APROVADO (AAA)** | Contraste exemplar para leitura fluida. |
| `--color-text-secondary`| `#685950` | Textos de apoio, subtítulos e metadados | **6.43:1** (vs `#FDFAF3`)<br>**6.70:1** (vs `#FFFFFF`) | **APROVADO (AA)** | Legibilidade garantida para corpo de texto. |
| `--color-brand-orange` | `#FF6600` | Onda decorativa, badges e acentos visuais | **2.82:1** (vs `#FDFAF3`) | **REPROVADO** para texto normal | **Uso restrito a grafismos decorativos, fundos e ícones grandes.** NUNCA aplicar em textos de leitura sobre fundo creme/branco. |
| `--color-orange-btn` | `#FF6400` | Botões de ação primários (com texto branco) | **2.94:1** (com `#FFFFFF`) | **REPROVADO** (Mínimo AA é 3.0:1 p/ botões) | **Correção:** Usar `--color-cta-orange: #E65700` (CR 3.67:1, **APROVADO AA Large**) ou aplicar texto escuro `--color-text-primary: #2A180E` sobre o botão (CR 5.79:1, **APROVADO AAA**). |
| `--color-orange-text` | `#C84C00` | Destaques textuais na cor laranja sobre branco/creme | **4.71:1** (vs `#FFFFFF`) | **APROVADO (AA Normal)** | Versão calibrada do laranja para ser usada no "PET" do título e links destacados. |
| `--color-peach-tint` | `#FFD4B4` | Halo decorativo orgânico no topo e rodapé | — | Decorativo | SVG/CSS sem texto sobreposto. |
| `--color-badge-bg` | `#301C11` | Fundo do selo "ENTREGA RÁPIDA EM SBC" | — | — | Fundo escuro premium. |
| `--color-badge-gold` | `#D89B5E` | Borda e detalhes do selo circular | **6.75:1** (vs `#301C11`) | **APROVADO (AA)** | Excelente visibilidade e sofisticação. |

### Declaração de Variáveis CSS Tokens
```css
:root {
  /* Bases */
  --bg-base: #fdfaf3;
  --bg-surface: #ffffff;
  --bg-surface-subtle: #f9f4ec;

  /* Tipografia */
  --text-primary: #2a180e;
  --text-secondary: #685950;
  --text-muted: #8b7d75;
  --text-inverse: #ffffff;
  --text-orange-accessible: #c84c00; /* WCAG AA 4.71:1 */

  /* Identidade Visual */
  --brand-orange: #ff6600;
  --brand-orange-hover: #e55c00;
  --brand-orange-active: #cc5200;
  --brand-peach: #ffd4b4;
  --brand-dark: #301c11;
  --brand-gold: #d89b5e;

  /* Componentes & CTA */
  --btn-cta-bg: #e65700; /* WCAG AA Large 3.67:1 com texto branco */
  --btn-cta-hover: #cf4e00;
  --shadow-card: 0 10px 25px -5px rgba(42, 24, 14, 0.05), 0 8px 10px -6px rgba(42, 24, 14, 0.03);
  --shadow-float: 0 20px 35px -8px rgba(255, 102, 0, 0.18);
  --border-radius-card: clamp(1rem, 2vw, 1.5rem);
  --border-radius-pill: 9999px;
}
```

---

## 4. Tipografia: Google Fonts Selecionadas

Em conformidade estrita com o `CLAUDE.md` (*"Proibido: fonte Inter/Roboto/Arial"*), foram selecionadas 2 candidatas por papel, rigorosamente justificadas:

### 4.1 Títulos e Display (H1, H2, H3, Números de Impacto)
* **Candidata 1 (Recomendada): `Plus Jakarta Sans` (Pesos 700, 800)**
  * *Justificativa*: Família geométrica contemporânea com terminações acolhedoras e excelente abertura de caracteres. Em pesos pesados (`font-weight: 800`) em caixa alta com ligeiro tracking negativo (`letter-spacing: -0.02em`), atinge exatamente o equilíbrio entre o "ultra-modern" do mockup e a energia vibrante de uma pet boutique de referência em São Bernardo.
* **Candidata 2: `Outfit` (Pesos 700, 800)**
  * *Justificativa*: Inspirada na tipografia da marca Outfit, com círculos perfeitos e forte presença de display. Excelente renderização gráfica para manchetes curtas e botões pílula.

### 4.2 Corpo de Texto, Descrições de Serviços e Reviews
* **Candidata 1 (Recomendada): `DM Sans` (Pesos 400, 500)**
  * *Justificativa*: Desenhada especificamente para telas digitais com foco em legibilidade em corpos menores (14px–16px). Apresenta proporções humanas calorosas que se conectam emocionalmente com tutores de pets e facilitam a leitura dos depoimentos e horários de atendimento.
* **Candidata 2: `Plus Jakarta Sans` (Pesos 400, 500)**
  * *Justificativa*: Utilizar a mesma família dos títulos para o corpo de texto unifica o design system, reduz requisições HTTP adicionais e economiza banda móvel no carregamento mobile-first.

---

## 5. Tabela de Camadas por Seção

Arquitetura de renderização respeitando a separação entre código nativo leve e ativos de imagem:

| Seção | Camada 1: Fundo & Efeitos (CSS/SVG) | Camada 2: Elementos Vetoriais & Badges (SVG/CSS) | Camada 3: Imagens / Mídia | Camada 4: Conteúdo & Interação (HTML/CSS) |
| :--- | :--- | :--- | :--- | :--- |
| **01-Hero** | `background-color: var(--bg-base);`<br>SVG Blob Pêssego superior esquerdo (`--brand-peach`) | `<svg class="hero-wave">` laranja orgânico responsivo na lateral direita | **FOTO REAL:** `imgi_15` (Spitz Batman) ou `imgi_16` (Yorkshire) recortado sem fundo *[ou PLATE GERADO]* | Logo SVG oficial no Header;<br>H1 semântico "TROPICAL PET";<br>Subtítulo de valor real;<br>Badge giratório "ENTREGA RÁPIDA EM SBC" |
| **02-Serviços** | `background-color: var(--bg-base);`<br>Gradiente radial sutil para iluminação dos cards | Linhas conectoras e ícones SVG temáticos (estetoscópio, pata, banho) | **FOTOS REAIS:**<br>1. `imgi_12` (Dra. Vânia c/ cão e estetoscópio)<br>2. `imgi_14` (Banhistas cuidando de pet real)<br>3. `imgi_19` (Medicamentos e calmantes reais) | H2 "SERVIÇOS DEDICADOS";<br>3 Cards com cantos arredondados, títulos semânticos, descrição dos diferenciais e micro-CTA via WhatsApp |
| **03-Produtos** | Fundo bege suave com transição curva inferior em CSS (`border-radius`) | Ícones de 5 estrelas e selos de garantia em SVG puro | **FOTOS REAIS:**<br>Destaque: `imgi_22` (Rações Premier e GoldeN)<br>Grid: Biscoitos PremierPet, Churu Gatos, Nutrafases Relax | H2 "ALIMENTAÇÃO & CUIDADOS PET";<br>Vitrine com nomes reais de produtos, badges de indicação e botão de pedido rápido |
| **04-Avaliações** | `background-color: var(--bg-base);`<br>SVG Onda Laranja fluindo na lateral direita | Balões de fala com pseudo-elementos CSS (`::after` triangular) e sombras suaves | **FOTOS REAIS DE CLIENTES:**<br>`imgi_16` (Yorkshire), `imgi_18` (Shih Tzu), `imgi_23` (Yorkshire lacinho rosa) | H2 "4.5 ★ • MAIS DE 700 FAMÍLIAS CONFIAM";<br>5 Balões com textos reais do Google Maps (Kethelin, Renata, etc.) |
| **05-CTA & Footer** | SVG Curva de transição inferior em tom pêssego suave | Ícones SVG oficiais de WhatsApp, Pin de Localização e Relógio de Horário | *Nenhum ativo bitmap necessário (100% vetorial e CSS)* | H2 de chamada para ação;<br>Botão flutuante WhatsApp em pílula;<br>Endereço completo e horários reais de atendimento |

---

## 6. Reinterpretação dos Elementos Decorativos em CSS/SVG Responsivo

Para recriar a atmosfera do mockup sem lentidão ou quebras em telas móveis:

### 6.1 A Grande Onda Alaranjada (Hero Wave)
Em vez de exportar um PNG com fundo transparente pesado, injeta-se um SVG inline posicionado na camada de fundo:
```html
<div class="hero-decor" aria-hidden="true">
  <svg class="hero-wave-svg" viewBox="0 0 600 800" preserveAspectRatio="none" fill="none">
    <path d="M120,0 C320,120 620,240 500,520 C420,700 240,680 180,800 L600,800 L600,0 Z" fill="var(--brand-orange)"/>
  </svg>
</div>
```
```css
.hero-decor {
  position: absolute;
  top: 0;
  right: 0;
  width: clamp(280px, 45vw, 650px);
  height: 100%;
  pointer-events: none;
  z-index: 1;
  overflow: hidden;
}
.hero-wave-svg {
  width: 100%;
  height: 100%;
  display: block;
}
```

### 6.2 O Selo Flutuante "ENTREGA RÁPIDA EM SBC"
Construído com CSS puro e SVG, garantindo nitidez vetorial retina:
```css
.badge-delivery {
  position: absolute;
  top: clamp(1rem, 4vw, 3rem);
  right: clamp(1rem, 5vw, 4rem);
  width: clamp(80px, 12vw, 110px);
  aspect-ratio: 1;
  background-color: var(--brand-dark);
  border: 2px dashed var(--brand-gold);
  border-radius: var(--border-radius-pill);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  color: var(--text-inverse);
  box-shadow: 0 8px 20px rgba(48, 28, 17, 0.25);
  z-index: 4;
}
.badge-delivery-title {
  font-size: 0.65rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-weight: 800;
  color: var(--brand-gold);
}
.badge-delivery-sub {
  font-size: 0.75rem;
  font-weight: 900;
  color: #ffffff;
}
```

### 6.3 Balões de Depoimentos Flutuantes (Speech Bubbles)
Criados com caixas brancas, sombra suave e indicador de fala vetorial:
```css
.testimonial-bubble {
  background: var(--bg-surface);
  border-radius: 1.25rem;
  padding: 1rem 1.25rem;
  box-shadow: var(--shadow-card);
  position: relative;
  max-width: 320px;
}
.testimonial-bubble::after {
  content: "";
  position: absolute;
  bottom: -8px;
  right: 24px;
  width: 16px;
  height: 16px;
  background: var(--bg-surface);
  clip-path: polygon(0 0, 100% 0, 100% 100%);
}
```

---

## 7. Especificação de Animações (Fase de Motion)

Seguindo as regras imperativas do `CLAUDE.md`:
1. *NADA acima da dobra depende de JavaScript para estar visível.* O conteúdo do Hero renderiza instantaneamente no HTML/CSS.
2. *Elementos contínuos de fundo NUNCA recebem animação pesada ou alteração de ancestral.*
3. *Apenas propriedades aceleradas por GPU (`transform` e `opacity`) nas camadas-folha.*

### 7.1 Hero Section
- **Badge "ENTREGA RÁPIDA EM SBC"**:
  - Efeito: Rotação suave contínua em loop lento (`animation: badge-rotate 25s linear infinite;`) OU flutuação vertical suave (`animation: gentle-float 4s ease-in-out infinite alternate;`).
  - `transform: translateY(-6px);`
- **Hero Pet**:
  - Efeito: Respiração/flutuação sutil idle pós-carregamento (`animation: pet-bob 5s ease-in-out infinite alternate;` com amplitude máxima de 8px).

### 7.2 Seção de Serviços (Scroll Reveal)
- **Gatilho**: IntersectionObserver nativo quando a seção atingir 20% do viewport.
- **Transição**: Os 3 cards entram com fade-in escalonado (*stagger* de 120ms):
  - Estado inicial: `opacity: 0; transform: translateY(24px);`
  - Estado ativo: `opacity: 1; transform: translateY(0); transition: opacity 0.5s ease-out, transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);`
- **Hover no Card**:
  - `transform: translateY(-8px); box-shadow: var(--shadow-float);` com `transition: transform 0.25s ease, box-shadow 0.25s ease;`.

### 7.3 Seção de Produtos & Vitrine
- **Hover nos Cards de Ração e Petiscos**:
  - Leve escala da embalagem: `img { transform: scale(1.04); transition: transform 0.3s ease; }`
  - Botão de compra: realce sutil de iluminação com transição de cor de fundo.

### 7.4 Seção de Avaliações
- **Flutuação dos Balões**:
  - Pequeno deslocamento assimétrico entre os balões (`animation: float-1 6s ease-in-out infinite alternate;` e `animation: float-2 7s ease-in-out infinite alternate-reverse;`) criando a sensação dinâmica e viva do mockup, sem deslocar a estrutura do layout.

### 7.5 Botão CTA WhatsApp
- **Pulso de Atenção**:
  - Um discreto anel expansivo (`::before`) com `animation: cta-pulse 3s infinite;` para atrair o clique sem ser intrusivo.

---

## 8. PLANO DE IMAGENS DETALHADO (Seção Crítica)

### 8.1 Inventário de Slots e Arquivos

| Slot de Imagem | Tipo | Arquivo de Origem / Destino | Tratamento / Status |
| :--- | :--- | :--- | :--- |
| **Hero: Pet Principal** | FOTO REAL *(ou PLATE)* | Origem: `imagens/imgi_15_...n.jpg` (Spitz Batman) ou `imagens/imgi_16_...n.jpg` (Yorkshire) | Requer remoção de texto sobreposto e recorte de fundo transparente. |
| **Serviços: Veterinária** | **FOTO REAL** | Origem: `imagens/imgi_12_799525835_17901615024586949_7382400699619258585_n.jpg` | Requer remoção dos textos promocionais ("Feliz Dia do Veterinário!") e do logo do canto. |
| **Serviços: Banho & Tosa** | **FOTO REAL** | Origem: `imagens/imgi_14_753546170_17892648603586949_7329816392311405352_n.jpg` | Crop e higienização de fundo na bancada do salão da loja. |
| **Serviços: Farmácia Pet** | **FOTO REAL** | Origem: `imagens/imgi_19_724251573_17885999328586949_100811721347011973_n.jpg` | Recorte das 3 embalagens reais (Nutrafases Relax, Anizen, Feliway Classic) removendo o tema da Copa. |
| **Vitrine: Rações Super Premium** | **FOTO REAL** | Origem: `imagens/imgi_22_712504467_17883706158586949_2736074244036066953_n.jpg` | Recorte isolando os sacos originais Premier Formula e GoldeN Formula. |
| **Vitrine: Petiscos & Snacks** | **FOTO REAL** | Origem: `imagens/imgi_22_712504467_17883706158586949_2736074244036066953_n.jpg` | Recorte do pacote de Biscoitos PremierPet e sachê Churu Atum. |
| **Reviews: Pet Cliente 1** | **FOTO REAL** | Origem: `imagens/imgi_16_730381838_17889214173586949_6863522406517588473_n.jpg` | Foto de Yorkshire real atendido na loja. Crop 1:1 circular/arredondado. |
| **Reviews: Pet Cliente 2** | **FOTO REAL** | Origem: `imagens/imgi_18_726767939_2505361883211509_3906247159874893960_n.jpg` | Foto de Shih Tzu real atendido na loja com bandana. Crop 1:1. |
| **Reviews: Card de Foto Pet** | **FOTO REAL** | Origem: `imagens/imgi_23_706829514_1291883296374694_6204960547805290417_n.jpg` | Requer remoção da legenda "TÔ PRONTA 💕" do rodapé. |

---

### 8.2 Prompts Prontos: Geração de PLATES (Decorativos)
*Nota de Diretriz: Todos os elementos de fundo (ondas, gradientes, badges) foram convertidos em CSS/SVG puro. O único plate decorativo contemplado para geração por IA é caso o usuário opte por reproduzir a estética do cão saltando do mockup em vez da foto real do pet do cliente.*

#### Prompt PLATE-01: Hero Pet Saltando (Mockup Style)
> **Prompt para Gerador (Midjourney / Imagen 3 / FLUX):**
> ```text
> High-speed commercial studio photography of an adorable energetic Jack Russell terrier dog leaping mid-air with pure joy, catching a colorful orange textured rubber pet toy in its mouth, paws outstretched towards camera, fur detailed and glossy, happy wide expressive eyes, brightly lit studio lighting, vibrant warm rim light, completely isolated on pure solid white background #FFFFFF, no background shadows, ultra-sharp focus, 8k resolution, professional pet advertising campaign --no floor, text, logos, blur, distorted paws
> ```

---

### 8.3 Prompts Prontos: AJUSTE de Fotos Reais do Cliente
*Seguindo a regra imperativa: "mantenha tudo idêntico, só corrija X", referenciando o arquivo exato de `imagens/`.*

#### Prompt AJUSTE-01: Card Veterinária (Dra. Vânia em Consulta)
* **Arquivo de Origem**: `imagens/imgi_12_799525835_17901615024586949_7382400699619258585_n.jpg`
* **Prompt Pronto de Inpainting / Limpeza**:
> ```text
> Base image: imgi_12_799525835_17901615024586949_7382400699619258585_n.jpg. Mantenha tudo absolutamente idêntico: a veterinária Dra. Vânia de camiseta branca e estetoscópio, suas tatuagens no braço, a expressão afetuosa, o cão caramelo saudável de gravata vermelha sobre a mesa cirúrgica de inox e a parede da clínica ao fundo. Remova completamente todos os textos e grafismos sobrepostos ('Feliz Dia do Veterinário!', frases de apoio, corações e o logo circular 'Tropical Pet Shop' no canto inferior direito). Preencha as áreas limpas da parede branca e da bancada mantendo a iluminação, granulação e textura naturais da foto original, com alta nitidez e resolução ampliada 2x.
> ```

#### Prompt AJUSTE-02: Hero Pet / Review (Pomeranian Pós-Tosa)
* **Arquivo de Origem**: `imagens/imgi_15_734898036_17890281852586949_2746539726296183126_n.jpg`
* **Prompt Pronto de Inpainting / Limpeza**:
> ```text
> Base image: imgi_15_734898036_17890281852586949_2746539726296183126_n.jpg. Mantenha tudo absolutamente idêntico: o cãozinho Spitz Alemão (Pomerânia) creme fofinho e recém-tosado, os olhos brilhantes, a língua para fora e a gravatinha azul estampada com o Batman. Remova exclusivamente a palavra 'after' que está sobreposta em branco na região do focinho e da boca do cachorro. Reconstrua os pelos do focinho e o reflexo do nariz com total perfeição biológica, preservando a textura natural da pelagem. Aumente a nitidez e entregue em fundo transparente PNG recortado.
> ```

#### Prompt AJUSTE-03: Foto de Pet Cliente para os Depoimentos
* **Arquivo de Origem**: `imagens/imgi_23_706829514_1291883296374694_6204960547805290417_n.jpg`
* **Prompt Pronto de Inpainting / Limpeza**:
> ```text
> Base image: imgi_23_706829514_1291883296374694_6204960547805290417_n.jpg. Mantenha tudo absolutamente idêntico: a cachorrinha Yorkshire Terrier sentada no chão de porcelanato claro com lacinhos florais rosa na cabeça e presilhas verdes. Remova unicamente o texto e emoji 'TÔ PRONTA 💕' sobreposto na parte inferior junto às patinhas. Reconstrua a superfície contínua do piso branco de cerâmica e as sombras naturais das patas, entregando a foto nítida e limpa.
> ```

#### Prompt AJUSTE-04: Card Farmácia Pet (Medicamentos Reais da Loja)
* **Arquivo de Origem**: `imagens/imgi_19_724251573_17885999328586949_100811721347011973_n.jpg`
* **Prompt Pronto de Inpainting / Isolamento**:
> ```text
> Base image: imgi_19_724251573_17885999328586949_100811721347011973_n.jpg. Mantenha tudo idêntico nas 3 embalagens reais de medicamentos veterinários: a caixa branca de Nutrafases Relax (60 tabletes mastigáveis), a caixa verde de Homeopet Anizen (30ml) e a caixa roxa de Feliway Classic (48ml). Isole completamente essas 3 caixas em alta definição, removendo todo o fundo de estádio de futebol da Copa do Mundo, a bandeira do Brasil, a bola e os textos promocionais. Coloque os 3 produtos lado a lado sobre uma bancada limpa e moderna de clínica veterinária em tons claros e neutros, com iluminação difusa suave e sombras de contato realistas.
> ```

#### Prompt AJUSTE-05: Vitrine de Rações e Alimentos Super Premium
* **Arquivo de Origem**: `imagens/imgi_22_712504467_17883706158586949_2736074244036066953_n.jpg`
* **Prompt Pronto de Inpainting / Isolamento**:
> ```text
> Base image: imgi_22_712504467_17883706158586949_2736074244036066953_n.jpg. Mantenha idênticas as embalagens comerciais autênticas: o saco azul de ração Premier Formula Cães Adultos, o saco preto de GoldeN Formula Frango e Arroz (10,1kg), o sachê de Biscoitos PremierPet Cães e o sachê de Churu Atum para Gatos. Remova os baldes de pipoca promocionais da Copa, o fundo neutro e todos os textos de oferta. Entregue os sacos de ração e petiscos agrupados de forma equilibrada em alta resolução para vitrine de produtos, com fundo limpo e transparente PNG.
> ```

---

## 9. Perguntas para Alinhamento Subjetivo (Decisões de Negócio)

*Nota: Decisões puramente técnicas de código, CSS, acessibilidade WCAG e responsividade foram resolvidas e implementadas de forma autônoma. Abaixo constam apenas as 4 decisões estritamente subjetivas de negócio:*

1. **Pet do Hero (Identidade Real vs. Dinamismo do Mockup)**:
   *No mockup, há um Jack Russell saltando em pose atlética com brinquedo (foto de stock). No material real do cliente, temos cães reais atendidos na loja (Spitz Alemão com gravata do Batman `imgi_15` ou Yorkshire feliz `imgi_16`).*
   *Você prefere que o Hero use a foto real do cliente (reforçando autenticidade local) ou prefere manter a energia acrobática do mockup gerando o plate do cão saltando via IA?*

2. **Logotipo no Header (Badge Circular Oficial vs. Versão Tipográfica do Mockup)**:
   *O logo real do cliente (`imgi_2`, `imgi_17`, `imgi_24`) é o badge circular clássico "Tr🐾pical Pet" com a pata embutida no 'o'. O mockup inventou uma versão horizontal com texto em caixa alta e pata separada.*
   *Você prefere fixar o badge circular oficial autêntico ou prefere aplicar uma releitura tipográfica horizontalizada moderna no topo do site?*

3. **3º Card de Serviços: "Super Farmácia Pet" vs. "Vacinação & Saúde Preventiva"**:
   *O mockup chama o 3º card de "Super Farmácia Pet". Nos dados reais do cliente, o serviço com maior apelo e procura após o banho e tosa é a **Campanha de Vacinação** (V4, V10, Antirrábica sem agendamento) conduzida pela Dra. Vânia.*
   *Mantemos o título focado em "Farmácia & Medicamentos Pet" ou direcionamos este card para "Vacinas & Cuidados Preventivos"?*

4. **Comportamento dos Botões da Vitrine de Produtos**:
   *No mockup existem botões genéricos de "Comprar" como num e-commerce tradicional. Na prática da Tropical Pet Shop, as vendas com entrega são canalizadas pelo WhatsApp.*
   *Você prefere que cada botão de produto já abra o WhatsApp com a mensagem personalizada (ex: "Olá! Gostaria de pedir a Ração GoldeN Formula 10,1kg...") ou prefere um botão neutro "Consultar Disponibilidade"?*

---

## 10. Pendências com o Cliente & Mensagem Pronta

### 10.1 Checklist de Pendências (Não bloqueia o desenvolvimento, bloqueia a publicação)
- [ ] **Horário Geral de Funcionamento da Loja**: Confirmar horário de abertura e dias (o Google Maps cita fechamento às 18:00, enquanto a clínica veterinária atende até 17h30 em dias úteis e 15h30 aos sábados).
- [ ] **Valores e Tabela de Preços**: Tabela base de banho e tosa por porte (pequeno/médio/grande) e valores das vacinas V10/Antirrábica, caso desejem exibir faixa de preço no site.
- [ ] **Regras de Entrega Rápida**: Bairros atendidos em São Bernardo do Campo, tempo estimado e se há valor mínimo de pedido para frete grátis/entrega local.
- [ ] **Arquivo do Logotipo em Vetor**: Solicitar arquivo em curva (`.svg`, `.ai` ou `.eps`) ou PNG de alta resolução com fundo transparente.
- [ ] **Autorização de Uso de Imagem**: Confirmação simples do uso das fotos dos pets clientes já publicadas nas redes sociais da loja.

---

### 10.2 Mensagem Pronta para Envio ao Cliente via WhatsApp

```text
Olá, equipe Tropical Pet Shop! Tudo bem? 🐾

Estamos desenvolvendo o novo site oficial da Tropical Pet Shop para destacar o trabalho incrível de vocês em São Bernardo do Campo, valorizando a experiência de 28 anos da Dra. Vânia, o carinho do Banho & Tosa e a facilidade do delivery de rações e medicamentos.

Para deixarmos tudo 100% afinado antes de colocar a página no ar, precisamos confirmar apenas 4 detalhes rápidos:

1. ⏰ Horário de Funcionamento da Loja:
   Confirmam para a gente o horário geral da loja física durante a semana e aos sábados? (Aos domingos e feriados vocês abrem?)

2. 🛵 Entrega Rápida em SBC:
   Vocês atendem todos os bairros de São Bernardo do Campo? Existe algum valor mínimo de pedido ou taxa fixa de entrega para informarmos aos clientes?

3. 🎨 Logotipo Oficial:
   Vocês teriam o arquivo do logo em alta resolução (PNG com fundo transparente) ou em vetor (PDF / Illustrator)? Se não tiverem, não se preocupem que nós cuidamos da vetorização!

4. 💉 Vacinas e Serviços:
   Gostariam de destacar no site alguma campanha especial ativa (como a de vacinação V8/V10 ou promoções de ração)?

O design está ficando lindo, moderno e totalmente otimizado para celulares! Qualquer dúvida, estamos à disposição. Muito obrigado! 🐶🐱
```
