# Matuê: Guess The Flow 🎵

Jogo desenvolvido em Python inspirado no estilo do Wordle, onde o jogador precisa adivinhar músicas do Matuê em até 6 tentativas.

O projeto foi criado utilizando Pygame e conta com interface personalizada, sistema de dicas, feedback visual por cores e salvamento automático de progresso.

---

## Funcionalidades

- Sistema de tentativas estilo Wordle
- Feedback visual para letras corretas e posições
- Dicas desbloqueadas durante a partida
- Salvamento automático da sessão usando Pickle
- Interface personalizada com artes próprias
- Música de fundo durante o jogo
- Sistema de menus (inicial, regras, jogo e reinício)

---

## Tecnologias utilizadas

- Python
- Pygame
- Pickle
- Photoshop

---

## Estrutura do projeto

```bash
📁 projeto
│
├── mainguesstheflow.py
├── botao.py
├── saveloadguesstheflow.py
├── estado_jogo.pkl
│
├── fundo default.png
├── fundo regras.png
├── fundo jogo pipinha.png
│
├── botao iniciar.png
├── botao jogar.png
├── botao reiniciar.png
│
├── Blank River.ttf
├── Streetbomber.ttf
│
└── Matuê - O Som.mp3
Como executar
1. Clone o repositório
git clone https://github.com/SEUUSUARIO/matue-guess-the-flow.git
2. Acesse a pasta
cd matue-guess-the-flow
3. Instale as dependências
pip install pygame
4. Execute o projeto
python mainguesstheflow.py
Como jogar
O jogador deve adivinhar a música secreta do Matuê
São permitidas até 6 tentativas
Letras corretas na posição correta ficam azuis
Letras corretas em posições erradas ficam roxas
Novas dicas são desbloqueadas ao longo da partida
Objetivo do projeto

O projeto foi desenvolvido com foco em prática de lógica de programação, manipulação de interfaces gráficas com Pygame, organização modular de código e gerenciamento de estado da aplicação.

Além da programação, também houve cuidado com identidade visual e experiência do usuário.

Autor

Pietra Bezerra
