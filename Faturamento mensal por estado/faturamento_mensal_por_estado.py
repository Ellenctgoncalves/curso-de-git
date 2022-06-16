def porcetagem_faturamento_por_mes(faturamentos):
	total = calcular_total_faturamento(faturamentos)
	percent = 0

	for local in faturamentos:
		percent = 100*faturamentos[local]/total
		print(percent)

def calcular_total_faturamento(faturamentos):
	total = 0
	for local in faturamentos:		
		total += faturamentos[local]

	print(total)
	return total	

if __name__ == '__main__': 

	faturamentos = {
		"sp":67836.43,
		"rj":36678.66,
		"mg":29229.88,
	    "es":27165.48,
	    "outros":19849.53
	    }

	porcetagem_faturamento_por_mes(faturamentos)

