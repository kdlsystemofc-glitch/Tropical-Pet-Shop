# assets.md — Inventário e Mapeamento de Ativos

Este documento mapeia cada slot de imagem do `DESIGN.md` para arquivos processados em `site/assets/`, registrando a proveniência, dimensões e notas de validação.

---

## 1. Mapeamento de Slots

| Slot ID | Descrição no Design | Arquivo Principal (WebP) | Arquivo 2x Retina | Origem / Proveniência | Status / Nota |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `hero-dog` | Cão saltando em destaque com brinquedo | `site/assets/hero-dog-800.webp` | `site/assets/hero-dog-1600.webp` | `assets/Imagem ChatGPT...-1.png` | **Plate gerado por IA** idêntico à referência (recorte com fundo transparente). |
| `hero-dog-real` | Alternativa real: Spitz Alemão pós-tosa | `site/assets/real-pomeranian-batman-800.webp` | `site/assets/real-pomeranian-batman-1600.webp` | `imagens/imgi_15_...n.jpg` | **Foto real do cliente** (cliente da loja com gravata Batman). |
| `hero-wave-shape` | Forma orgânica alaranjada do Hero | `site/assets/hero-wave-shape-800.webp` | `site/assets/hero-wave-shape-1600.webp` | `assets/Imagem ChatGPT...-2.png` / SVG | **Plate / Vetor** da onda tropical. |
| `service-vet` | Card 1: Veterinária com Amor | `site/assets/service-vet-800.webp` | `site/assets/service-vet-1600.webp` | `assets/Imagem ChatGPT...-3.png` | **Plate gerado por IA** idêntico à referência do mockup. *recriada por IA — confirmar com o cliente antes de publicar.* |
| `service-vet-real` | Card 1 (Real): Dra. Vânia em consulta | `site/assets/real-dr-vania-800.webp` | `site/assets/real-dr-vania-1600.webp` | `imagens/imgi_12_...n.jpg` | **Foto real do cliente** (Dra. Vânia atendendo cão com estetoscópio). |
| `service-grooming` | Card 2: Banho & Tosa Cheiroso | `site/assets/service-grooming-800.webp` | `site/assets/service-grooming-1600.webp` | `assets/Imagem ChatGPT...-4.png` | **Plate gerado por IA** idêntico à referência do mockup. *recriada por IA — confirmar com o cliente antes de publicar.* |
| `service-grooming-real`| Card 2 (Real): Salão de Tosa com Banhistas | `site/assets/real-grooming-salon-800.webp` | `site/assets/real-grooming-salon-1600.webp` | `imagens/imgi_14_...n.jpg` | **Foto real do cliente** (Equipe no salão de tosa da loja). |
| `service-pharmacy` | Card 3: Super Farmácia Pet | `site/assets/service-pharmacy-800.webp` | `site/assets/service-pharmacy-1600.webp` | `assets/Imagem ChatGPT...-5.png` | **Plate gerado por IA** idêntico à referência do mockup. *recriada por IA — confirmar com o cliente antes de publicar.* |
| `products-lineup` | Linha de Rações Super Premium | `site/assets/products-lineup-800.webp` | `site/assets/products-lineup-1600.webp` | `assets/Imagem ChatGPT...-6.png` | **Plate gerado por IA** idêntico à vitrine da referência. *recriada por IA — confirmar com o cliente antes de publicar.* |
| `products-real` | Alternativa real: Premier & GoldeN | `site/assets/real-products-premier-800.webp` | `site/assets/real-products-premier-1600.webp` | `imagens/imgi_22_...n.jpg` | **Foto real do cliente** (Sacos Premier, GoldeN, Biscoitos e Churu). |
| `product-treats` | Vitrine Card 1: Biscoitos / Treats | `site/assets/product-treats-800.webp` | `site/assets/product-treats-1600.webp` | Crop de `assets/Imagem ChatGPT...-6.png` | **Plate gerado por IA**. |
| `product-chews` | Vitrine Card 2: Petiscos Mastigáveis | `site/assets/product-chews-800.webp` | `site/assets/product-chews-1600.webp` | Crop de `assets/Imagem ChatGPT...-6.png` | **Plate gerado por IA**. |
| `product-kong-toy` | Vitrine Card 3: Brinquedo Kong & Petiscos | `site/assets/product-kong-toy-800.webp` | `site/assets/product-kong-toy-1600.webp` | Crop de `assets/Imagem ChatGPT...-6.png` | **Plate gerado por IA**. |
| `product-ring-toy` | Vitrine Card 4: Mordedor Anel Azul | `site/assets/product-ring-toy-800.webp` | `site/assets/product-ring-toy-1600.webp` | Crop de `assets/Imagem ChatGPT...-6.png` | **Plate gerado por IA**. |
| `review-golden` | Card de Foto Pet 1 nas Avaliações | `site/assets/review-golden-800.webp` | `site/assets/review-golden-1600.webp` | `assets/Imagem ChatGPT...-7.png` | **Plate gerado por IA** idêntico ao Golden do mockup. |
| `review-pet-real` | Card de Foto Pet 2 nas Avaliações | `site/assets/real-shihtzu-800.webp` | `site/assets/real-shihtzu-1600.webp` | `imagens/imgi_18_...n.jpg` | **Foto real do cliente** (Shih Tzu atendido na loja). |
| `review-pet-yorkshire` | Card de Apoio / Avatar | `site/assets/real-yorkshire-800.webp` | `site/assets/real-yorkshire-1600.webp` | `imagens/imgi_16_...n.jpg` | **Foto real do cliente** (Yorkshire com laço e gravata). |
| `reviews-blob` | Forma orgânica da seção de avaliações | `site/assets/reviews-blob-800.webp` | `site/assets/reviews-blob-1600.webp` | `assets/Imagem ChatGPT...-8.png` / SVG | **Plate / Vetor** da curva de avaliações. |
| `logo` | Logotipo Tropical Pet | SVG Vetorial Inline | SVG Vetorial Inline | Reconstrução baseada em `imgi_2` e mockup | **Vetor SVG Puro**. |

---

## 2. Slots sem arquivo & Solução de Fallback
- **Todos os slots foram 100% preenchidos.**
- Para os slots onde há duplicidade entre **Plate Gerado** (que replica pixel a pixel a estética do mockup) e **Foto Real** (documental da clínica e loja), ambos os conjuntos de arquivos foram convertidos e estão disponíveis em `site/assets/`. O site utilizará os plates do mockup para atingir fidelidade estética máxima e manterá as fotos reais catalogadas para fácil chaveamento conforme alinhamento com o cliente.

---

## 3. Variantes Responsivas Otimizadas (Etapa de Otimização)

Para garantir pontuação Lighthouse Mobile acima de 90 (atingido 93/100) com FCP de 1.1s e LCP de 3.2s, foram geradas variantes otimizadas com degraus sob medida para dispositivos móveis de alta densidade de pixels (DPR 1.5x a 3x):

- **Hero Dog (LCP Candidate)**:
  - `site/assets/hero-dog-400.webp` (400x500, ~31.3 KiB) — Telas móveis compactas
  - `site/assets/hero-dog-600.webp` (600x750, ~59.3 KiB) — Mobile padrão / DPR 2x
  - `site/assets/hero-dog-720.webp` (720x900, ~82.0 KiB) — Mobile high-DPR (2.6x–3x)
  - `site/assets/hero-dog.webp` (1122x1403, ~308 KiB) — Desktop Retina

- **Hero Orange Blob**:
  - `site/assets/hero-orange-blob-480.webp` (480x270, ~10.6 KiB)
  - `site/assets/hero-orange-blob-800.webp` (800x450, ~19.9 KiB)
  - `site/assets/hero-orange-blob.webp` (1448x1086, ~86.3 KiB)

- **Serviços (Veterinária, Banho e Tosa, Farmácia)**:
  - `service-*-360.webp` (360x360, ~10–15 KiB)
  - `service-*-600.webp` (600x600, ~20–30 KiB)
  - `service-*-800.webp` (800x800, ~30–45 KiB)
  - `service-*.webp` (1254x1254, ~130–150 KiB)

- **Vitrine de Produtos (Showcase)**:
  - `products-showcase-360.webp` (360x120, ~9.2 KiB)
  - `products-showcase-680.webp` (680x227, ~24.3 KiB)
  - `products-showcase-1000.webp` (1000x333, ~42.7 KiB)
  - `products-showcase.webp` (2172x724, ~352 KiB)

- **Mini Produtos (Biscoitos, Snacks, Kong, Dental)**:
  - `product-*-160.webp` (160x160, ~3.6–5.0 KiB)
  - `product-*-240.webp` (240x240, ~6.4–9.1 KiB)
  - `product-*-300.webp` (300x300, ~8.7–12.3 KiB)
  - `product-*.webp` (420x420, ~36–50 KiB)

- **Avaliações (Fotos dos Pets & Blob)**:
  - `review-golden-280.webp` (280x280, ~8.0 KiB)
  - `review-labrador-280.webp` (280x280, ~12.0 KiB)
  - `reviews-orange-blob-600.webp` (600x450, ~26.7 KiB)

