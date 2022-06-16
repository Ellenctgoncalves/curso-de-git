import random

def calcular_fibonacci(numero):
    sequencia = [0,1]
    proximo_numero = 0

    while proximo_numero <= numero:
        ultimo = sequencia[-1]
        penultimo = sequencia[-2]
        proximo_numero = ultimo + penultimo
        
        if proximo_numero <= numero:
        	sequencia.append(proximo_numero)
        else:
        	break

    return sequencia

def consta_em_fibonacci(numero):
	sequencia_fibonacci = calcular_fibonacci(numero)

	if sequencia_fibonacci.count(numero) > 0:
		return "consta em Fibonacci"
	else:
		return "não consta em Fibonacci"

if __name__ == '__main__':
    
    numero = int(input("Digite um número inteiro: "))

    print(consta_em_fibonacci(numero))