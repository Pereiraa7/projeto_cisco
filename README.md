# Jogo da Velha em Python

🚀 Funcionalidades
Representação do tabuleiro em formato visual no terminal.
Jogador humano realiza sua jogada digitando o número do campo desejado.
O computador realiza movimentos aleatórios em campos livres.
Verificação automática de vitória ou empate após cada jogada.
Exibição clara do estado do jogo a cada turno.
📂 Estrutura do Código
Importações
python
Copiar código
from random import randrange
O código utiliza a função randrange da biblioteca random para determinar os movimentos do computador.

Funções Principais
display_board(board)
Exibe o tabuleiro no terminal com linhas separadoras e os valores correspondentes aos campos.

Entrada: Uma matriz 3x3 representando o estado atual do tabuleiro.
Saída: Impressão do tabuleiro formatado no console.
enter_move(board)
Permite que o jogador humano insira sua jogada.

Valida se a entrada é um número entre 1 e 9 e se o campo está disponível.
Atualiza o tabuleiro com a jogada do jogador.
make_list_of_free_fields(board)
Cria uma lista com os campos livres disponíveis para jogadas.

Saída: Lista de tuplas (row, col) representando as posições livres no tabuleiro.
victory_for(board, sgn)
Verifica se há um vencedor no jogo.

Entrada:
board: Matriz 3x3 do tabuleiro.
sgn: Sinal ('O' ou 'X') a ser verificado.
Saída:
'you' se o jogador humano vencer.
'me' se o computador vencer.
None se ainda não houver vencedor.
draw_move(board)
Realiza a jogada do computador escolhendo um campo livre de forma aleatória.

Atualiza o tabuleiro com a jogada do computador usando o sinal 'X'.
Estrutura do Tabuleiro
O tabuleiro é representado como uma matriz 3x3, onde cada célula contém um número inicial (1 a 9) ou uma marcação ('O' ou 'X') após as jogadas.

Exemplo inicial do tabuleiro:

diff
Copiar código
+-------+-------+-------+
|   1   |   2   |   3   |
+-------+-------+-------+
|   4   |   X   |   6   |
+-------+-------+-------+
|   7   |   8   |   9   |
+-------+-------+-------+
Fluxo Principal do Jogo
O tabuleiro é inicializado com números de 1 a 9.
O computador começa jogando no centro do tabuleiro.
O jogador humano e o computador alternam suas jogadas.
Após cada jogada, o código verifica:
Se há um vencedor.
Se o jogo terminou em empate.
O jogo exibe o tabuleiro atualizado após cada jogada.
O resultado é exibido no final: vitória do jogador, vitória do computador ou empate.
🛠️ Requisitos
Python 3.x instalado no sistema.
Biblioteca padrão do Python (não requer instalação adicional).
⚙️ Como Executar
Clone este repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/tic-tac-toe-python.git
Navegue até o diretório:
bash
Copiar código
cd tic-tac-toe-python
Execute o script:
bash
Copiar código
python jogo_da_velha.py
✨ Exemplo de Uso
plaintext
Copiar código
+-------+-------+-------+
|   1   |   2   |   3   |
+-------+-------+-------+
|   4   |   X   |   6   |
+-------+-------+-------+
|   7   |   8   |   9   |
+-------+-------+-------+

Digite seu movimento: 5
Campo já ocupado – repita sua entrada!
Digite seu movimento: 1

+-------+-------+-------+
|   O   |   2   |   3   |
+-------+-------+-------+
|   4   |   X   |   6   |
+-------+-------+-------+
|   7   |   8   |   9   |
+-------+-------+-------+
📚 Aprendizados
Este projeto é ideal para:

Estudo de listas e matrizes em Python.
Implementação de lógica condicional e loops.
Aprendizado sobre como validar entradas do usuário.
Exercícios de manipulação de strings e formatação de saída no terminal.
📄 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para usar, modificar e compartilhar.

