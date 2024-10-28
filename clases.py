# clases (class) son parte fundamental de la POO (Progamacion oriantada a objetos)

# 1 )Defincion de una clase: se define utilizando la pálabra clave "class", seguido del nombre de la clase. 
# por convecion el nombre de la clase comienza con una letra mayuscula, las clases son plantillas que nos permiten
# crear objetos.

class MiClase:
    pass

# 2 ) atributos : son variables que pertenecen a la clase, se pueden definir con 
#el metodo especial " init " qie se llama cuando se crea una instancia de clase

# 3 ) Metodos: son funciones que pertenecen a la clase y pueden operar sobre los atributos
#de la clase. el primer parametro de un metodo debe ser self que se refiere a la instancia actual de la clase

class Persona:
    def __init__(self, nombre , edad, estatura, peso):
        self.nombre = nombre # Atributo nombre
        self.edad = edad # Atributo edad
        self.estatura = estatura # Atributo estatura
        self.peso = peso # Atributo peso

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años, mido {self.estatura}cm y peso {self.peso} ")

#4) Instanciacion: para crear un objeto de una clase, se llama a la clase como si fuera una funcion
alejandro = Persona("Alejandro", 26 , 1.75, "80 kg")
carlos = Persona("Carlos", 21 , 1.84, "70 kg")

print("Tu edad es: ",alejandro.edad)
print("Tu nombre es:",alejandro.nombre)
print("Tu estatura es: ",alejandro.estatura)
print("Tu peso es: ",alejandro.peso)
    
alejandro.saludar()
carlos.saludar()

# Herencia : las clases pueden heredar atributos y metodos de otra clase, lo que nos permite crear
# Jerarquias y reutilizar codigo

class Trabajador(Persona):
    def __init__(self, nombre, edad, estatura, peso, trabajo):
        super().__init__(nombre, edad, estatura, peso) # LLama al constructor de la clase base (Persona)
        self.trabajo = trabajo # Atributo curso de la clase Estudiante

    def trabajar(self):
        print(f"{self.nombre} esta trabajando en la empresa {self.trabajo}")

estudiante1 = Trabajador("Alejandro", 26 , 173, 80, "ITBC group")

estudiante1.saludar()
estudiante1.trabajar()


# Ejemplo de clases aplicado en situaciones de la vida real

# 1. sistema de gestion de estudiantes


class Estudiante(Persona): 
    def __init__(self, nombre, edad, estatura ,peso , grado):
        super().__init__(nombre,edad,estatura,peso)
        self.grado = grado # Atriburo grado de la clase Estudiante
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        # sum(1,2,3) 1+2+3 = 6 / len(longitud)de self.notas = 3 
        return sum(self.notas) / len(self.notas) if self.notas else 0
    
# Usabilidad

estudiante1 = Estudiante("Andres", 17 , 1.75 , 80 ,"5to año")
estudiante1.agregar_nota(15)
estudiante1.agregar_nota(20)
estudiante1.agregar_nota(12)

print(f"Promedio de {estudiante1.nombre} fue de: {estudiante1.promedio()}")

# 2. Sistema de gestion de inventario

class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    def actualizar_stock(self, cantidad):
        self.cantidad += cantidad

    def vender(self, cantidad):
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        else:
            print("Stock insuficiente")
            return False
        
# uso 

producto1 = Producto("Laptop", 1200, 10)
producto1.vender(2)
print(f"Stock de {producto1.nombre}: {producto1.cantidad}")

# 3. Sistema de gestion bancaria
# 1. crear la clase
# 2. Crear 2 metodos (Depositar, retirar)
# 3. Que me diga si tengo fondos suficientes para retirar o no.


    



