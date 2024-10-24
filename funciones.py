# Funciones sin parametros

def saludar():
    print("Hola")

a = 5
b = 6
c = a + b

print(c)

#Funciones con parametros

def sumar(num1, num2):
    print("El resultaod de la suma es:",num1 + num2)
    #return num1 + num2

#resultado = sumar(2,4)

#print("El resultado de la suma con funcion asignado a una variable es: ", resultado)
#print("El resultado de la suma con funcion asignado a una variable es: ", resultado)

sumar(2,45)
sumar(15,245)
sumar(23,25)

def resta(num1, num2):
    print("El resultado de la resta es", num1 - num2)

a = 3
b = 2

resta(2, 4)
resta(a, b)

def despedir(nombre= "Pedro"):
    if nombre is None:
        print("Adios Amigo")
    else:
        print(f"Adios {nombre} Ten lindo dia!")

despedir()
despedir("Alejandro")
despedir(None)

print("---------------------------------------")

# *args
#Funciones con numero variable de argumentos (No conocemos la cantidad de arguemntos que vamos a necesitar)

def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
    print("----------------------------------------------------------------------------------")

listarNombres("Alejandro", "Pedro", "Enrique")
listarNombres("Alejandro", "Pedro", "Enrique", "Pablo", "Lionel")
listarNombres("Alejandro", "Pedro", "Enrique", "Pablo", "Lionel", "Karim", "Cristiano") 


# **kwargs -> kw= "Keyword" args = Argumentos

#Funciones conm un numero de arguemntos variables pero se recibe un conjunto de pares clave-valor

def mostrarInfo(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")


mostrarInfo(nombre="pedro",edad=30, ciudad="Madrid")


# Funciones lambda (Funciones sin nombre)

# 1) Se utilizan cuando necesitamos realizar operaciones simples de una sola linea
# 2) Usarlas como argumentos para funciones de orden superior, como: map(), filter(), sorted()

multiplicar = lambda x,y: print("Resultado de la funcion lambda es: ", x * y)
sumando = lambda x: print("Resultado de la funcion lambda es: ",sum(x))

multiplicar(3,3)
sumando([1,2,4,8,12,16])


#Funciones anidadas

def funcionExterna(x): # x en este punto vale 3, Tiene un scope Global
    def funcionInterna(y): #Scope local
        return y ** 2
    resultado = funcionInterna(x) # LLamando a la funcion interna
    return resultado + 1 #Sumando 1 al resultado de la funcion interna

resultadoFinal =funcionExterna(3)
print("El resultado final de la funcion anidada es: ",resultadoFinal)


# Recursividad.
# Contiene 2 conceptos

# 1) el caso base : es la condicion que va a detener la recursion. 
# sin un caso base , la funcion  se estaria llamando a si misma indefinidamente 
# lo que nos llevaria a un desbordamiento de pila (Stack Overflow)

#2) caso recursivo: esta es la parte de la funcion donde se llama a si misma, 
# pero con un argumento modificado que eventualmente alcanzara al caso base

# Factorial de un numero: es el producto de todos los numeros enteros desde el 1 hasta n

#1....n si n = 5 entonces seria : 1*2*3*4*5 = 120

# factorial iterativo

def factorialIterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i # resultado = resultado * i
    return resultado


n = 5
print(f"El factorial de {n} es",factorialIterativo(5))


def factorialRecursivo(n):
    #caso base
    if n == 0:
        return 1
    #caso recursivo
    else:
        return n * factorialRecursivo(n -1)


print(f"factorial recursivo de {n} es:", factorialRecursivo(n))







