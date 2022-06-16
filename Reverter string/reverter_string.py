string = str(input("Digite uma string: "))
nova_str = ""

for i in range(1,len(string)+1):
	nova_str += string[-i]

print("Nova string é ",nova_str)