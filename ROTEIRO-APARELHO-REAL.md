# Roteiro de Teste em Aparelho Real — Tropical Pet Shop
*Guia passo a passo para validação prática em dispositivos físicos iPhone (iOS) e smartphones Android.*

---

## 1. Como Conectar o Aparelho Real ao Ambiente Local

Para testar o site no seu celular antes de publicar na web:
1. Conecte o seu smartphone na **mesma rede Wi-Fi** do computador de desenvolvimento.
2. No computador, descubra o seu endereço IP local executando no terminal:
   ```powershell
   ipconfig
   ```
   *(Procure pelo endereço IPv4 da sua placa Wi-Fi, por exemplo: `192.168.1.15`)*.
3. Inicie o servidor local na pasta do projeto:
   ```bash
   python -m http.server 8000 --bind 0.0.0.0
   ```
4. No navegador do smartphone (Safari no iPhone ou Chrome no Android), digite:
   `http://<SEU_IP_LOCAL>:8000` (exemplo: `http://192.168.1.15:8000`).

---

## 2. Checklist de Testes para iPhone (Apple iOS / Safari & Chrome)

| Área / Recurso | O que Verificar | Critério de Sucesso | Status |
| :--- | :--- | :--- | :---: |
| **Notch & Dynamic Island** | Abra a página no Safari com o aparelho na vertical. Observe a área superior da tela onde fica o entalhe/ilha e a barra de status. | O logo "Tropical Pet" e o botão de WhatsApp do header respeitam as margens de segurança (*safe-areas*), sem sobrepor os ícones do sistema de bateria e relógio. | [ ] |
| **Barra de Endereço Retrátil (100svh)** | Role a página para baixo e para cima lentamente para ver a barra de navegação inferior do Safari retrair e expandir. | O Hero e os elementos de topo utilizam unidades modernas de viewport (`100svh`), sem saltos visuais bruscos (*layout shift*) quando a barra do navegador muda de tamanho. | [ ] |
| **Rolagem Suave & Inércia (Momentum)** | Efetue gestos rápidos de swipe vertical para avaliar a inércia nativa do iOS junto ao motor Lenis. | Rolagem fluida a 60fps/120fps (em telas ProMotion), sem congelamentos ou atraso de resposta (*stutter*). | [ ] |
| **Botão de Pausa de Animações** | Toque no botão flutuante circular no canto inferior esquerdo (`#motion-toggle-btn`). | O toque é reconhecido de primeira (área mínima $\ge 44\times 44\text{px}$), o ícone alterna suavemente de ⏸ para ▶, e as animações congelam no local. | [ ] |
| **Abertura do Aplicativo do WhatsApp** | Toque no botão "PEDIR PELO WHATSAPP" ou em qualquer um dos botões "Comprar" dos cards. | O iOS solicita permissão para abrir diretamente o aplicativo oficial do WhatsApp instalado no aparelho, com a mensagem temática já digitada na caixa de texto. | [ ] |
| **Rotação para Modo Paisagem (Horizontal)** | Gire o iPhone para a horizontal (resolução típica $844\times 390$ ou $932\times 430$). | A página se ajusta perfeitamente. Nenhuma imagem vaza horizontalmente e não surge barra de rolagem lateral indesejada. | [ ] |
| **Efeitos Visuais e Textura Tátil** | Inspecione a textura granulada de fundo (`noise.png`) e o efeito de desfoque (*backdrop-filter*) do botão flutuante. | O efeito fosco translúcido renderiza de forma nítida, conferindo visual sofisticado e orgânico de alta fidelidade ao mockup. | [ ] |
| **Acessibilidade de Zoom Nativo** | Nas configurações do iOS (*Acessibilidade > Tamanho do Texto*), aumente o tamanho da fonte em 200%. | Os textos expandem preservando legibilidade e sem quebras de layout sobrepostas. | [ ] |

---

## 3. Checklist de Testes para Smartphones Android (Samsung, Xiaomi, Motorola, etc.)

| Área / Recurso | O que Verificar | Critério de Sucesso | Status |
| :--- | :--- | :--- | :---: |
| **Barra de Navegação do Sistema** | Em aparelhos configurados com a barra de navegação tradicional de 3 botões (Voltar, Home, Recentes). | O botão flutuante de pausa de motion fica acessível acima da barra inferior do sistema, sem sofrer oclusão. | [ ] |
| **Disparo do WhatsApp via Deep Link** | Toque nos links `wa.me/5511960365965?...`. | O sistema Android dispara o intent nativo do WhatsApp imediatamente sem loops de redirecionamento ou telas em branco no Chrome. | [ ] |
| **Modo "Remover Animações" do Sistema** | Ative a opção *Remover Animações* em *Configurações > Acessibilidade* do Android e recarregue a página. | O site detecta instantaneamente `prefers-reduced-motion: reduce`, desativando loops e exibindo o conteúdo diretamente sem transições longas. | [ ] |
| **Comportamento em Hardware Econômico** | Teste em um aparelho com modo de economia de energia ativado ou com hardware modesto. | O núcleo de motion detecta a restrição de recursos e reduz dinamicamente os efeitos de micro-flutuação, garantindo economia de bateria. | [ ] |
| **Teclado Virtual e Zoom de Leitura** | Dê um duplo toque em um parágrafo para ativar o zoom inteligente do navegador. | A linha de texto quebra harmoniosamente sem exigir rolagem horizontal para ler o restante da frase. | [ ] |

---

## 4. Teste em Condições Reais de Uso Externo (Iluminação Solar)

- **Legibilidade ao Ar Livre**: Abra o site sob luz solar direta para testar a paleta de cores.
  - *Critério:* Os títulos em marrom escuro (`#2C1810`) sobre o fundo creme (`#FAF6F0`) e os botões em tom terracota (`#E65700`) mantêm leitura imediata e alto contraste sem ofuscamento.
- **Conexão Móvel 4G/3G**: Desconecte do Wi-Fi e acesse via rede móvel com sinal moderado.
  - *Critério:* Graças às fontes locais, Critical CSS inline e imagens WebP responsivas em degraus leves (160w a 600w), a primeira dobra de conteúdo surge na tela em menos de 1,2 segundo.

---

## 5. Como Reportar e Tratar Inconsistências

Caso identifique qualquer comportamento imprevisto em um modelo específico:
1. Anote o modelo exato do dispositivo (ex.: *iPhone 13 iOS 17.4* ou *Samsung Galaxy A54 Android 14*).
2. Capture um screenshot ou gravação de tela demonstrando o ponto de atenção.
3. As variáveis e tokens no arquivo [`DESIGN.md`](file:///c:/Oficial/Tropical%20Pet%20Shop/DESIGN.md) e na folha [`site/css/style.css`](file:///c:/Oficial/Tropical%20Pet%20Shop/site/css/style.css) permitem calibrações pontuais sem afetar os outros navegadores.
