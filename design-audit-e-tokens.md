# FASE 1: DESIGN AUDIT (Salgadinhos Torcida)

## Paleta Cromática
- **Cores Dominantes da Marca:** Amarelo Vibrante (Energia, Fome, Acessibilidade) e Azul Profundo (Confiança, Contraste Institucional).
- **Cores Secundárias (Saborização):** Vermelho Quente (Pimenta/Camarão), Verde Bandeira (Cebola/Mexicana), Roxo Intenso (Churrasco), Laranja/Mostarda (Queijo), Marrom Terroso (Costelinha).
- **Contraste & Temperatura:** Altíssimo contraste (Amarelo vs Azul/Cores escuras). A temperatura geral é quente, estimulando urgência e apetite.

## Sistema Tipográfico
- **Logo/Marca:** Sem serifa, itálica (skewed), bold. Transmite movimento, velocidade e ação.
- **Tipografia de Apoio:** Condensada, bold, muitas vezes com texturas desgastadas (distressed) ou caixas delimitadoras irregulares.
- **Personalidade:** Alta voz, informal, chamativa ("grita" na prateleira).

## Vocabulário de Forma
- **Geometria Predominante:** Angular e dinâmica. Linhas diagonais (paralelogramos), cortes secos.
- **Formas de Apoio:** Curvas de onda separando blocos de cor (o "sorriso" da embalagem que divide o topo colorido da base amarela).

## Textura e Acabamento
- **Fundo:** Halftones (retículas), raios de explosão (starbursts), linhas de velocidade (action lines).
- **Visualização do Produto:** Fotografia real (apetite appeal) em tigelas, com ingredientes (bacon, cebola) orbitando com motion blur ou linhas de energia.

## Espaço Negativo e Hierarquia
- **Uso de Espaço:** Denso e preenchido. Muito pouco respiro (horror vacui visual).
- **Hierarquia:** 1. Logo da Marca (Topo) -> 2. Nome do Sabor (Centro) -> 3. Produto Físico (Base).

---

# FASE 2: BRAND POSITIONING

- **Personalidade da Marca:** Enérgica, Popular, Intensa, Descomplicada.
- **Tom de Voz Sugerido:** Direto, vibrante, com gírias e apelo à coletividade (A linguagem da "galera", do jogo de futebol, do churrasco de domingo).
- **Público-Alvo Implícito:** Jovens adultos, adolescentes e o "brasileiro médio" buscando um snack acessível para compartilhar em momentos de descontração.

---

# FASE 3: O "DESVIO AUTORAL" (Transposição para Web)

A regra de ouro é **não copiar a embalagem**, mas usar sua gramática para criar uma UI contemporânea:

1. **Texturas (De Halftone para Ruído Orgânico):**
   - *Original:* Raios estourados e retículas impressas (estilo salgadinho barato).
   - *Desvio UI:* Fundo liso com um `noise-filter` (SVG overlay) bem sutil a 5%. Dá a sensação tátil de crocância sem sujar a tela, elevando a percepção de valor.

2. **Formas (De Grafismos Poluídos para Componentes Angulares):**
   - *Original:* Logos e faixas distorcidas, ondas irregulares.
   - *Desvio UI:* Uso de `clip-path: polygon()` para criar cortes diagonais agressivos nos limites das seções (`section`) e nos botões. A velocidade da marca vira o "shape" do próprio botão, que se distorce no hover.

3. **Paleta (De Bloqueio de Prateleira para Tokens de Interação):**
   - *Original:* Amarelo e azul gritando ao mesmo tempo.
   - *Desvio UI:* O Amarelo (#FDE02F) atua como cor de destaque (Hero) e CTA. O Azul Profundo (#1A237E) vira o background principal (modo escuro) para descansar os olhos e contrastar fortemente. As cores de sabor (Vermelho, Verde, Roxo) viram fundos de `cards` nas seções de scroll.

4. **Tipografia (De Distressed para Brutalismo Limpo):**
   - *Original:* Fontes desgastadas e inclinadas.
   - *Desvio UI:* Substituição por uma fonte geométrica ultra-condensada (`Anton`) para os títulos gigantes (Kinetic Typography), garantindo o impacto "in your face", mas combinada com uma sans-serif limpa e tecnológica (`Space Grotesk`) para leitura corporal, garantindo legibilidade e uma estética "brutalista digital" em vez de "rótulo de supermercado".

5. **Motion e Espaço (De Denso para Coreografado):**
   - *Original:* Tudo apertado na embalagem.
   - *Desvio UI:* Na web, o espaço negativo é amplo. A energia não vem de aglomerar elementos, mas da **velocidade do motion** (GSAP stagger). Elementos entram rasgando a tela em diagonais, traduzindo a "intensidade" do snack através do movimento, não da poluição visual.
