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
