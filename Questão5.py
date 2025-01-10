# Definir a string a ser invertida
string_original = "String"

# Inverter os caracteres da string
string_invertida = ""
for char in string_original:
    string_invertida = char + string_invertida

# Exibir a string invertida
print("String original:", string_original)
print("String invertida:", string_invertida)