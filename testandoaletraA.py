def verificar_letra_a(string):
    string = string.lower()
    if 'a' in string:
        quantidade = string.count('a')
        return f"A letra 'a' está presente na string e ocorre {quantidade} vezes."
    else:
        return "A letra 'a' não está presente na string."

string = input("Informe uma string: ")
print(verificar_letra_a(string))