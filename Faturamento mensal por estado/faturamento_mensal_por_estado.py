def obter_percentual_por_estado(faturamentos):
	percentual = 0
	percentuais_faturamento = {}

	try:
		total = calcular_total_faturamento(faturamentos.values())
	except:
		print("Erro em obter total dos faturamentos")
	else:
		for estado, valor in faturamentos.items():	
			percentual = 100 * valor / total
			percentuais_faturamento[estado] = percentual

	return percentuais_faturamento

def calcular_total_faturamento(valores):
	return sum(valores)	

if __name__ == '__main__': 

	faturamentos = {
        "sp":67836.43,
        "rj":36678.66,
        "mg":29229.88,
        "es":27165.48,
        "outros":19849.53
	    }

	print("Total líquido de faturamentos: ", calcular_total_faturamento(faturamentos.values()))
	print("percentuais de faturamentos por estado: ", obter_percentual_por_estado(faturamentos))

