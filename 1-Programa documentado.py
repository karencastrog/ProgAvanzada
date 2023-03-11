class Animal:
    def __init__(self, nombre, edad):
        """
        Esta clase representa un animal
        - nombre (string): es el nombre del animal
        - edad (int): es la edad del animal
        """
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self, sonido):
        """
        Método para que el animal haga un sonido
        - sonido (string): es el sonido que hace el animal
        """
        self.sonido = sonido

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        """
        Clase que representa un perro y hereda atributos de la clase Animal
        Se agrega atributo raza porque ya heredó nombre y edad
        - raza (string): es la raza del perro
        """
        super().__init__(nombre, edad)
        self.raza = raza
    
    def hacer_sonido(self):
        """
        Método que muestra el sonido que hace el perro
        """
        print("El perro hace guau guau")

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        """
        Clase que representa un gato y hereda atributos de la clase Animal
        Se agrega atributo color porque ya heredó nombre y edad
        - color (string): color del gato
        """
        super().__init__(nombre, edad)
        self.color = color
    
    def hacer_sonido(self):
        """
        Método que muestra el sonido que hace el gato
        """
        print("El gato hace miau")

# Para crear los objetos 
perro1 = Perro("Mono", 2, "criollo")
gato1 = Gato("Michi", 3, "negro con blanco")

# Traer los atributos del objeto y llamar el método
print(f"Mi perro se llama {perro1.nombre}, tiene {perro1.edad} años y es un {perro1.raza}")
perro1.hacer_sonido()

print(f"Mi gato se llama {gato1.nombre}, tiene {gato1.edad} años y es de color {gato1.color}")
gato1.hacer_sonido()