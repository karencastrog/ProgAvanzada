def verificar_anagrama(palabra1, palabra2):
    """
    Método que verifica si dos palabras son anagramas

    Parámetros:
    palabra1 (str): primera palabra
    palabra2 (str): segunda palabra
    """
    # Si una de las palabras es nula o tienen diferente tamaño, no son anagramas
    if palabra1 is None or palabra2 is None or len(palabra1) != len(palabra2):
        return "NO es anagrama"
    # Si tienen el mismo tamaño pasar las palabras a minúsculas antes de compararlas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    # Se ordenan las letras de las palabras y si tienen las mismas letras pero en diferente orden, son anagramas
    return "SI es anagrama" if sorted(palabra1) == sorted(palabra2) else "NO es anagrama"

# Pedir dos palabras
palabra1 = input("Ingrese la palabra 1: ")
palabra2 = input("Ingrese la palabra 2: ")

# Mostrar el resultado del método verificar_anagrama
print(palabra1, verificar_anagrama(palabra1, palabra2), "de", palabra2)

