import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_seo_block = """  <title>Tropical Pet Shop | Clínica Veterinária, Banho e Tosa e Rações em São Bernardo do Campo</title>
  <meta name="description" content="Pet shop completo em São Bernardo do Campo (Vila Santa Luzia): Clínica Veterinária com a Dra. Vânia, Banho e Tosa, Farmácia e Rações com delivery rápido via WhatsApp. Rua Espanha, 415.">
  <meta name="theme-color" content="#FF6000">

  <!-- Configuração de Domínio e URL Canônica (veja seo.config.json). Descomente quando o domínio estiver ativo: -->
  <!-- <link rel="canonical" href="https://www.tropicalpetshop.com.br/"> -->

  <!-- Open Graph / Meta Compartilhamento -->
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="Tropical Pet Shop">
  <!-- <meta property="og:url" content="https://www.tropicalpetshop.com.br/"> -->
  <meta property="og:title" content="Tropical Pet Shop | Clínica Veterinária, Banho e Tosa em São Bernardo do Campo">
  <meta property="og:description" content="Pet shop completo em São Bernardo do Campo: Clínica Veterinária com a Dra. Vânia, Banho e Tosa, Farmácia e Rações Super Premium com entrega rápida via WhatsApp.">
  <meta property="og:image" content="site/assets/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:alt" content="Tropical Pet Shop — Clínica Veterinária, Banho e Tosa e Rações em São Bernardo do Campo">
  <!-- URL Absoluta da Imagem Open Graph (descomente quando o domínio estiver ativo): -->
  <!-- <meta property="og:image" content="https://www.tropicalpetshop.com.br/site/assets/og-image.jpg"> -->

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Tropical Pet Shop | Clínica Veterinária, Banho e Tosa em São Bernardo do Campo">
  <meta name="twitter:description" content="Pet shop completo em São Bernardo do Campo: Clínica Veterinária com a Dra. Vânia, Banho e Tosa, Farmácia e Rações com delivery rápido via WhatsApp.">
  <meta name="twitter:image" content="site/assets/og-image.jpg">
  <meta name="twitter:image:alt" content="Tropical Pet Shop em São Bernardo do Campo">
  <!-- <meta name="twitter:image" content="https://www.tropicalpetshop.com.br/site/assets/og-image.jpg"> -->

  <!-- Favicons e Manifest PWA -->
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐾</text></svg>">
  <link rel="icon" type="image/png" sizes="32x32" href="site/assets/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="site/assets/favicon-16x16.png">
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="site/assets/apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">

  <!-- Preload local WOFF2 critical fonts -->
  <link rel="preload" href="site/fonts/plus-jakarta-sans-800-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="site/fonts/dm-sans-400-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" as="image" href="site/assets/hero-dog-600.webp" imagesrcset="site/assets/hero-dog-400.webp 400w, site/assets/hero-dog-600.webp 600w, site/assets/hero-dog-720.webp 720w, site/assets/hero-dog.webp 1122w" imagesizes="(max-width: 600px) 260px, (max-width: 1024px) 340px, 420px" fetchpriority="high">

  <!-- 
    ==========================================================================
    DIRETRIZES DE CONFORMIDADE SCHEMA.ORG / GOOGLE (CAMPOS COMENTADOS):
    ==========================================================================
    1. aggregateRating: As avaliações registradas (4.5 estrelas, 723 avaliações no Google Maps)
       são de plataformas de terceiros. De acordo com as diretrizes de dados estruturados do Google,
       avaliações de terceiros NÃO podem ser publicadas como aggregateRating proprietário no
       próprio site. Descomente apenas se houver sistema de avaliação nativo próprio no domínio:
       
       "aggregateRating": {
         "@type": "AggregateRating",
         "ratingValue": "4.5",
         "reviewCount": "723",
         "bestRating": "5",
         "worstRating": "1"
       }

    2. openingHoursSpecification: O CLIENTE.md confirma encerramento às 18:00 ('Aberto · Fecha 18:00'),
       porém a grade completa semanal por dia (segunda a sábado/domingo) deve ser confirmada formalmente
       com o cliente antes de ser publicada como definitiva:
       
       "openingHoursSpecification": [
         {
           "@type": "OpeningHoursSpecification",
           "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
           "opens": "08:00",
           "closes": "18:00"
         }
       ]

    3. priceRange: Faixa de preço varia conforme porte do animal e produto (ex: "$$").
  -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": ["PetStore", "VeterinaryCare"],
    "@id": "https://www.tropicalpetshop.com.br/#localbusiness",
    "name": "Tropical Pet Shop",
    "alternateName": "Tropical Pet",
    "description": "Pet shop completo e clínica veterinária em São Bernardo do Campo com mais de 28 anos de tradição. Consultas com a Dra. Vânia, banho e tosa carinhoso, farmácia veterinária e rações super premium com entrega rápida.",
    "url": "https://www.tropicalpetshop.com.br",
    "telephone": "+55-11-96036-5965",
    "image": "site/assets/og-image.jpg",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Rua Espanha, 415",
      "addressLocality": "São Bernardo do Campo",
      "addressRegion": "SP",
      "postalCode": "09671-050",
      "addressCountry": "BR"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": -23.6705,
      "longitude": -46.5645
    },
    "areaServed": {
      "@type": "City",
      "name": "São Bernardo do Campo"
    },
    "sameAs": [
      "https://www.instagram.com/tropicalpetshop"
    ],
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "Serviços e Produtos Tropical Pet Shop",
      "itemListElement": [
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Clínica Veterinária",
            "description": "Consultas veterinárias dedicadas e acompanhamento com a Dra. Vânia."
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Banho e Tosa",
            "description": "Estética animal, hidratação, tosa na máquina e tesoura com equipe atenciosa."
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Farmácia Veterinária",
            "description": "Medicamentos, antiparasitários, calmantes e suplementos essenciais."
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Super Mercado Pet & Delivery",
            "description": "Rações super premium, petiscos crocantes, brinquedos e entrega rápida via WhatsApp."
          }
        }
      ]
    }
  }
  </script>"""

# Replace from <title> down to just before <style id="critical-css">
head_pattern = r'  <title>[\s\S]*?<link rel="preload" as="image"[^>]+>'
html = re.sub(head_pattern, new_seo_block, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html with comprehensive local SEO head tags!")
