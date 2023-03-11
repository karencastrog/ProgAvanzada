entrada = input("Ingrese una palabra o frase: ")
# pasar la entrada a minúsculas
entrada = entrada.lower()
# quitar los espacios en blanco
entrada_sin_espacios = entrada.replace(' ', '')
# invertir la entrada antes de comparar
entrada_invertida = entrada_sin_espacios[::-1]
# comparar para saber si es palíndromo
if entrada_sin_espacios == entrada_invertida:
    print(entrada, "SI es un palíndromo")
else:
    print(entrada, "NO es un palíndromo")
