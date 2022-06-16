import json
 
def achar_media_mes(dados):
    somatorio,peso = 0,0

    novos_dados = excluir_vazios(dados)

    for elemento in novos_dados:
        somatorio += elemento["valor"] 
        peso += 1
        
    return somatorio/peso

def dias_faturamento_acima_media(dados):
    media = achar_media_mes(dados)
    dias = []
    for elemento in dados:
        if elemento["valor"] > media:
            dias.append(elemento["dia"])

    return dias


def excluir_vazios(dados):
    novos_dados = []

    for elemento in dados:
        valor_atual = elemento["valor"] 

        if valor_atual > 0:
            novos_dados.append(elemento)

    return novos_dados


def achar_menor_valor(dados):
    novos_dados = excluir_vazios(dados)
    valor_atual =  novos_dados[0]["valor"]
    menor_valor = valor_atual
    
    for elemento in novos_dados:
        valor_atual = elemento["valor"] 

        if valor_atual < menor_valor:
             menor_valor = valor_atual

    return menor_valor

def achar_maior_valor(dados):
    maior_valor = 0

    for elemento in dados:
        valor_atual = elemento["valor"] 

        if valor_atual > maior_valor:
            maior_valor = valor_atual
    return maior_valor



if __name__ == '__main__': 
    f = open('dados.json',)
      
    dados = json.load(f)

    #print(" 1. Média \n 2. Menor valor \n 3. Maior valor \n 4. Dias de faturamento acima da média")
    #opcao = int(input(""))
    dias = dias_faturamento_acima_media(dados)

    print("Média é ", achar_media_mes(dados))
    print("Menor valor é ", achar_menor_valor(dados))
    print("Maior valor é ", achar_maior_valor(dados))
    print(len(dias), " dias de faturamento acima da média, estes foram ", dias)




  
f.close()