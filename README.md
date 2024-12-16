# Jogo da Velha em Python

Este repositório contém a implementação de um **Jogo da Velha** simples utilizando Python. O jogo permite que um jogador humano jogue contra o computador diretamente no terminal.

## 🚀 Funcionalidades

- Representação do tabuleiro em formato visual no terminal.
- Jogador humano realiza sua jogada digitando o número do campo desejado.
- O computador realiza movimentos aleatórios em campos livres.
- Verificação automática de vitória ou empate após cada jogada.
- Exibição clara do estado do jogo a cada turno.

---

## 📂 Estrutura do Código

### Importações

`from random import randrange`

O código utiliza a função `randrange` da biblioteca `random` para determinar os movimentos do computador.

---

### Funções Principais

#### **`display_board(board)`**

Exibe o tabuleiro no terminal com linhas separadoras e os valores correspondentes aos campos.

- **Entrada:** Uma matriz 3x3 representando o estado atual do tabuleiro.
- **Saída:** Impressão do tabuleiro formatado no console.

#### **`enter_move(board)`**

Permite que o jogador humano insira sua jogada.

- Valida se a entrada é um número entre 1 e 9 e se o campo está disponível.
- Atualiza o tabuleiro com a jogada do jogador.

#### **`make_list_of_free_fields(board)`**

Cria uma lista com os campos livres disponíveis para jogadas.

- **Saída:** Lista de tuplas `(row, col)` representando as posições livres no tabuleiro.

#### **`victory_for(board, sgn)`**

Verifica se há um vencedor no jogo.

- **Entrada:**
    - `board`: Matriz 3x3 do tabuleiro.
    - `sgn`: Sinal ('O' ou 'X') a ser verificado.
- **Saída:**
    - `'you'` se o jogador humano vencer.
    - `'me'` se o computador vencer.
    - `None` se ainda não houver vencedor.

#### **`draw_move(board)`**

Realiza a jogada do computador escolhendo um campo livre de forma aleatória.

- Atualiza o tabuleiro com a jogada do computador usando o sinal 'X'.

---

### Estrutura do Tabuleiro

O tabuleiro é representado como uma matriz 3x3, onde cada célula contém um número inicial (1 a 9) ou uma marcação ('O' ou 'X') após as jogadas.

Exemplo inicial do tabuleiro:

![image](https://github.com/user-attachments/assets/67589815-1169-4abb-98ab-63e0315d736d)

---

### Fluxo Principal do Jogo

1. O tabuleiro é inicializado com números de 1 a 9.
2. O computador começa jogando no centro do tabuleiro.
3. O jogador humano e o computador alternam suas jogadas.
4. Após cada jogada, o código verifica:
    - Se há um vencedor.
    - Se o jogo terminou em empate.
5. O jogo exibe o tabuleiro atualizado após cada jogada.
6. O resultado é exibido no final: vitória do jogador, vitória do computador ou empate.

---

## 🛠️ Requisitos

- Python 3.x instalado no sistema.
- Biblioteca padrão do Python (não requer instalação adicional).

---

## ✨ Exemplo de Uso

![image](https://github.com/user-attachments/assets/2d6d1057-f4b8-4f4b-afac-dea7b79f58f8)

---

## 📚 Aprendizados

Este projeto é ideal para:

- Estudo de listas e matrizes em Python.
- Implementação de lógica condicional e loops.
- Aprendizado sobre como validar entradas do usuário.
- Exercícios de manipulação de strings e formatação de saída no terminal.

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e compartilhar.

