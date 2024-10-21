# numeros

#enteros (int)
entero = 42

print("El tipo de variable es:",type(entero))

#flotantes(float)

flotante = 3.14

print("El tipo de variable es:",type(flotante))

#Complejos

complejo = 2 + 3j

print("El tipo de variable es:",type(complejo))

#cadena de texto o string (str)

cadena = "Hola, Mundo!"

print("El tipo de variable es:",type(cadena))

#booleanos (valores verdadero o falso)

verdadero = True
falso = False

print(type(verdadero))
print(type(falso))


#listas (Colecciones ordenadas y mutables de elementos, puede tener elementos de diferentes tipos.)

lista = [1,2,3,4,5,6]

print(lista[2])

lista[3] = 6

print(lista)
print("la longitud o cantidad de elementos de mis lista es : ", len(lista))

# tuplas (Colecciones ordenadas e INMUTABLES de elementos, al igual que las listas pueden contenter elementos de diferentes tipos)

tupla = (1,2,3,"Cuatro", 5.2)

print(type(tupla))
print(len(tupla))
print(tupla[-1]) #n-2 donde "n" es la longitud o el numero total de elementos que contiene mi tupla

#tupla[1] =2

#print("Tratando de mutar o alterar la tupla",tupla)

#Diccionarios (Colecciones de pares clave-valor) en donde cada clave es unica y son utilizadas para acceder a su valor

diccionario = {
    "nombre": "Alejandro",
    "edad": 26,
    "altura" : 1.75
    }

print(type(diccionario))
print(diccionario)
print(diccionario["altura"])
print(diccionario.get("nombre"))


usuarios = [
    {
        "cedula": 26619384,
        "nombre": "Alejandro",
        "edad": 26,
        "altura" : 1.75
    },
    {
        "cedula": 18345654,
        "nombre": "Amdres",
        "edad": 35,
        #"altura" : 1.85 
    }
]

print(usuarios[0].get("altura", "no disponible"))
print(usuarios[1].get("altura", "el valor de altura no esta disponible en el indice 1"))


