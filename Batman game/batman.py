import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def obter_salto (limite_maior, limite_menor):
    meio = ((limite_maior - limite_menor)//2) + 1
    print("Debug messages...", meio, file=sys.stderr, flush=True)
    return meio

# w: width of the building.
# h: height of the building.
if __name__ == "__main__":
    # w: width of the building.
    # h: height of the building.
    w, h = [int(i) for i in input().split()]
    print("Debug messages...Largura: ", w, file=sys.stderr, flush=True)
    print("Debug messages...Altura:", h, file=sys.stderr, flush=True)
    n = int(input())  # maximum number of turns before game over.
    x0, y0 = [int(i) for i in input().split()]
    coluna = x0
    linha = y0
    
    limite_esquerda, limite_superior= 0, 0
    limite_direita = w - 1 
    limite_inferior = h - 1

    # game loop
    while True:
        bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
        
        
        if bomb_dir == "U":
            limite_esquerda, limite_direita = coluna, coluna
            limite_inferior = linha - 1
            linha-= obter_salto(limite_inferior, limite_superior)
        elif bomb_dir == "D":
            limite_esquerda, limite_direita = coluna, coluna
            limite_superior = linha + 1
            linha += obter_salto(limite_inferior, limite_superior)
        elif bomb_dir == "R":
            limite_superior, limite_inferior = linha, linha
            limite_esquerda = coluna + 1
            coluna += obter_salto(limite_direita, limite_esquerda)
        elif bomb_dir == "L":
            limite_superior, limite_inferior = linha, linha
            limite_direita = coluna - 1
            coluna -= obter_salto(limite_direita, limite_esquerda)
        elif bomb_dir == "UR":
            limite_inferior = linha - 1
            limite_esquerda = coluna + 1
            coluna += obter_salto(limite_direita, limite_esquerda)
            linha -= obter_salto(limite_inferior, limite_superior)
        elif bomb_dir == "UL":
            limite_inferior = linha - 1
            limite_direita = coluna - 1
            coluna -= obter_salto(limite_direita, limite_esquerda)
            linha -= obter_salto(limite_inferior, limite_superior)
        elif bomb_dir == "DR":
            limite_superior = linha + 1
            limite_esquerda = coluna + 1
            coluna += obter_salto(limite_direita, limite_esquerda)
            linha += obter_salto(limite_inferior, limite_superior)
        elif bomb_dir == "DL":
            limite_superior = linha + 1
            limite_direita = coluna - 1
            coluna -= obter_salto(limite_direita, limite_esquerda)
            linha += obter_salto(limite_inferior, limite_superior)
        else:
            print("Wrong command.")


        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)


        # the location of the next window Batman should jump to.
        print(coluna, linha)