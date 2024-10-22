#Ciclos o bucles

# Son estructuras de control que permiten ejecutar un bloquye de codigo repetidamente mientras se cumpla una condicion

# hay 2 tipos principales de ciclos en pyhton "for " y "While"

#Ciclo For

frutas = ["manzana", "cereza", "pera", "parchita"]

for fruta in frutas:
    print(fruta) #Imprime por consola cada fruta de la lista

for i in range(5):#Imprime los numeros del 0 al 4
    print(i)

#calculando los numeros pares hasta el 100

for numero in range(101):
    if numero % 2 == 0:
        print(numero, "Es par")
    elif numero % 1 == 0:
        print(numero,"Es impar")


# 2. Ciclo "While" se va a ejecutar un bloque de codigo mientras una condicion sea verdadera

contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1
