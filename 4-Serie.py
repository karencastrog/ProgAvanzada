def serie(n):
    # Definir los primeros dos términos de la serie
    a = 1
    b = 1
    # Acumulador "suma" que almacena la suma de términos
    suma = 0
    # Ciclo para sumar los n términos de la serie
    for i in range(n):
        # Agregar el término "a" al acumulador "suma"
        suma += a
        # variable para guardar el siguiente término de la serie
        siguiente_valor = a + b
        # asignar a "a" el valor de "b"
        a = b
        # ahora "b" toma el valor de la suma "a+b" que se guardó en "siguiente_valor"
        b = siguiente_valor
    return suma

# Pedir al usuario que ingrese un número n 
n = int(input("Ingrese la cantidad 'n' de términos que desea sumar: "))

# Llamar la función y mostrar el resultado
print("La suma de los primeros", n, "términos de la serie es:", serie(n))