import json

def excluir_vazios(faturamento_mensal):
    faturamento_mensal_limpo = [diario for diario in faturamento_mensal if diario.get("valor") > 0]
            
    return faturamento_mensal_limpo
 
def obter_media_mes(faturamento_mensal):
    somatorio, peso = 0, 0

    faturamento_mensal_limpo = excluir_vazios(faturamento_mensal)

    for diario in faturamento_mensal_limpo:
        somatorio += diario.get("valor") 
        peso += 1
        
    return somatorio / peso

def dias_faturamento_acima_media(faturamento_mensal):
    dias = []

    try:
        media = obter_media_mes(faturamento_mensal)
    except TypeError:
        print("Dados do faturamento mensal recebidos no tipo errado.")
    except ZeroDivisionError:
        print("Dados do faturamento mensal recebidos estão vazios.")
    except:
        print("Não foi possível obter média para cálculo.")
    else:
        dias = [diario.get("dia") for diario in faturamento_mensal if diario.get("valor") > media]           
        
    return dias

def obter_menor_valor(faturamento_mensal):
    novos_faturamento_mensal = excluir_vazios(faturamento_mensal)
    menor_valor = novos_faturamento_mensal[0].get("valor")
    
    
    for diario in novos_faturamento_mensal:
        valor_atual = diario.get("valor")
        if valor_atual < menor_valor:
            menor_valor = valor_atual 

    return menor_valor

def obter_maior_valor(faturamento_mensal):
    maior_valor = 0

    for diario in faturamento_mensal:
        valor_atual = diario.get("valor")

        if valor_atual > maior_valor:
            maior_valor = valor_atual
            
    return maior_valor

if __name__ == '__main__': 
    f = open('dados.json',)
      
    faturamento_mensal = json.load(f)

    dias = dias_faturamento_acima_media(faturamento_mensal)

    print("Média é ", obter_media_mes(faturamento_mensal))
    print("Menor valor é ", obter_menor_valor(faturamento_mensal))
    print("Maior valor é ", obter_maior_valor(faturamento_mensal))
    print(len(dias), " dias de faturamento acima da média, estes foram ", dias)
  
    f.close()