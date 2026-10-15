# PENDÊNCIAS DO CLIENTE — Tropical Pet Shop
*Lista objetiva de informações, ativos e decisões pendentes por parte do cliente, e o impacto direto de cada resolução no site.*

---

## 1. Visão Geral das Pendências

O site foi completamente projetado, estruturado, otimizado e aprovado tecnicamente com **100% dos dados confirmados** em `CLIENTE.md`. Para a publicação final e conformidade legal e regulatória máxima, os seguintes itens dependem exclusivamente de informações fornecidas pelo cliente ou proprietário:

| Item | Prioridade | Situação Atual | O que o Cliente Deve Fornecer | Efeito / Impacto Quando Resolvido |
| :--- | :---: | :--- | :--- | :--- |
| **1. Domínio Definitivo** | **Crítica** | Campo vazio em `seo.config.json` / `cliente.config.json`. Tags canônicas e links absolutos comentados no HTML e Sitemap. | URL registrada do domínio contratado (ex: `https://www.tropicalpetshop.com.br`). | Ativação imediata de tag `<link rel="canonical">`, metadados de compartilhamento `og:url` e `og:image` com URL absoluta para WhatsApp/Facebook/X, e submissão do `sitemap.xml` no Google Search Console para indexação acelerada. |
| **2. CRMV da Dra. Vânia** | **Alta** | Menção como "Dra. Vânia (28 anos de experiência)" sem o número de registro do conselho de classe. | Número de inscrição no Conselho Regional de Medicina Veterinária de São Paulo (ex: CRMV-SP 12345). | Conformidade com o Código de Ética do Médico Veterinário (Resolução CFMV nº 1138/2016 e exigências do CRMV-SP para divulgação de serviços clínicos). Inclusão no Schema.org `VeterinaryCare` (`identifier`), gerando autoridade clínica inquestionável no Google. |
| **3. CNPJ e Razão Social** | **Alta** | Rodapé exibe identificação de marca e direitos reservados ("Tropical Pet Shop"), sem os dados cadastrais da pessoa jurídica. | CNPJ e Razão Social oficial registrada na Receita Federal do Brasil. | Conformidade com o Decreto Federal nº 7.962/2013 (Lei do E-commerce e Atendimento Eletrônico) e art. 31 do Código de Defesa do Consumidor (CDC), aumentando a segurança jurídica e a credibilidade institucional perante órgãos de fiscalização (Procon). |
| **4. Grade Completa de Horários** | **Média** | Exibe horário geral comercial ("08:00 às 18:00") e horários com base no Google Maps. | Horário detalhado de Segunda a Sexta, Sábado e Domingos/Feriados para: Loja física, Consultas Veterinárias e Banho & Tosa. | Ativação da propriedade `openingHoursSpecification` no Schema.org JSON-LD para exibição dos badges "Aberto agora / Fecha às XXh" diretamente no snippet de busca do Google e na busca local do Maps. |
| **5. Link Oficial de Avaliação no Google Maps** | **Média** | O site exibe os depoimentos reais de clientes do Google com nota 4.5 e mais de 700 avaliações, mas sem o botão direto para avaliar. | Link curto "Avaliar no Google" extraído da Ficha do Google Meu Negócio (Perfil da Empresa) ou Google Place ID. | Permite incluir um botão de call-to-action "Deixe sua avaliação no Google", alimentando organicamente o ranking do Google Meu Negócio e impulsionando o SEO local no bairro Vila Santa Luzia e região de SBC. |
| **6. Tabela / Política de Preços** | **Baixa** | Todos os serviços e produtos direcionam para pedido/agendamento via WhatsApp com mensagem personalizada pré-preenchida. | Confirmação se a estratégia comercial continuará sendo consulta de preços via WhatsApp (recomendada para alta conversão em pet shop de bairro) ou se deseja divulgar valores fixos de banho/tosa e vacinas. | Se confirmada a estratégia de WhatsApp, mantém-se a alta conversão sem atrito de preço; se fornecidos valores fixos, podem ser adicionados ao Schema `hasOfferCatalog` com campo `price`. |
| **7. Fotos Reais Complementares (Opcional)** | **Baixa** | O site utiliza fotos reais do acervo (produtos Premier, Golden, loja e Dra. Vânia) associadas a plates de alta fidelidade visual (Hero e ambientação). | Fotos autorais adicionais em alta resolução: banhistas no salão em ação, fachada externa atual da Rua Espanha e novo retrato da Dra. Vânia em estúdio/consultório. | Substituição dos plates decorativos por imagens 100% autorais locais, caso o cliente deseje representação 1:1 de cada centímetro da loja sem ilustrações de apoio. |

---

## 2. Como Preencher e Reconstruir

Todos os dados acima foram centralizados no arquivo:
👉 [`cliente.config.json`](file:///c:/Oficial/Tropical%20Pet%20Shop/cliente.config.json)

### Passo a passo para atualização:
1. Abra o arquivo [`cliente.config.json`](file:///c:/Oficial/Tropical%20Pet%20Shop/cliente.config.json).
2. Preencha os campos `url`, `cnpj`, `razaoSocial`, `crmv` e os horários de cada setor.
3. Execute no terminal:
   ```bash
   python scripts/rebuild_client_data.py
   ```
4. O script irá:
   - Inserir as tags canônicas e de Open Graph completas em `index.html`.
   - Atualizar a URL do `sitemap.xml` e descomentar o link em `robots.txt`.
   - Atualizar os dados do Schema.org (`VeterinaryCare` e `PetStore`) com CRMV, CNPJ e horários exatos.
   - Atualizar o rodapé com os dados legais.
