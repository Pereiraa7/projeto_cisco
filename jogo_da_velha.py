from random import randrange

def exibir_tabuleiro(tabuleiro):
    print("+-------" * 3, "+", sep="")
    for linha in range(3):
        print("|       " * 3, "|", sep="")
        for coluna in range(3):
            print("|   " + str(tabuleiro[linha][coluna]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def realizar_jogada(tabuleiro):
    jogada_valida = False
    while not jogada_valida:
        jogada = input("Digite seu movimento: ") 
        jogada_valida = len(jogada) == 1 and jogada >= '1' and jogada <= '9'
        if not jogada_valida:
            print("Jogada inválida – tente novamente!")
            continue
        jogada = int(jogada) - 1
        linha = jogada // 3
        coluna = jogada % 3
        simbolo = tabuleiro[linha][coluna]
        jogada_valida = simbolo not in ['O', 'X'] 
        if not jogada_valida:
            print("Campo já ocupado – tente novamente!")
            continue
    tabuleiro[linha][coluna] = 'O'

def listar_campos_livres(tabuleiro):
    livres = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] not in ['O', 'X']:
                livres.append((linha, coluna))
    return livres

def verificar_vitoria(tabuleiro, simbolo):
    if simbolo == "X":
        vencedor = 'computador'
    elif simbolo == "O":
        vencedor = 'você'
    else:
        vencedor = None
    diagonal1 = diagonal2 = True
    for i in range(3):
        if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
            return vencedor
        if tabuleiro[0][i] == simbolo and tabuleiro[1][i] == simbolo and tabuleiro[2][i] == simbolo:
            return vencedor
        if tabuleiro[i][i] != simbolo:
            diagonal1 = False
        if tabuleiro[i][2 - i] != simbolo:
            diagonal2 = False
    if diagonal1 or diagonal2:
        return vencedor
    return None

def jogada_computador(tabuleiro):
    livres = listar_campos_livres(tabuleiro)
    quantidade = len(livres)
    if quantidade > 0:
        escolhida = randrange(quantidade)
        linha, coluna = livres[escolhida]
        tabuleiro[linha][coluna] = 'X'

tabuleiro = [[3 * j + i + 1 for i in range(3)] for j in range(3)] 
tabuleiro[1][1] = 'X'
livres = listar_campos_livres(tabuleiro)
vez_humano = True

while len(livres):
    exibir_tabuleiro(tabuleiro)
    if vez_humano:
        realizar_jogada(tabuleiro)
        vencedor = verificar_vitoria(tabuleiro, 'O')
    else:
        jogada_computador(tabuleiro)
        vencedor = verificar_vitoria(tabuleiro, 'X')
    if vencedor != None:
        break
    vez_humano = not vez_humano
    livres = listar_campos_livres(tabuleiro)

exibir_tabuleiro(tabuleiro)
if vencedor == 'você':
    print("Você venceu!")
elif vencedor == 'computador':
    print("O computador venceu!")
else:
    print("Empate!")
