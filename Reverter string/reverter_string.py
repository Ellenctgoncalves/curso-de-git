def reverter_string(string):
	nova_str = ""
	for i in range(1,len(string)+1):
		nova_str += string[-i]

	return nova_str

if __name__ == '__main__':
	string = input("Digite uma string: ")
	print("Nova string é ",reverter_string(string))