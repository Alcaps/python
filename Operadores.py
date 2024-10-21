#Operadores de comparacion
#Ejemplos practicos de operaciones de comparacion
# 1) == igual a
a = 8
b = 7

if a == b:
    print("a es igual a b")

elif a != b :
    print("a no es igual a b")

else:
    print("")
# 2) != diferente de

a = 7
b = 6

if a != b :
    print("a es diferente de b")
# 3) > mayor que

a = 8
b = 7

if a > b :
    print("a es mayor que b")
# 4) < menor que 

a = 6
b = 10

if a < b :
    print("a es menor que b")
# 5) >= mayor o igual que 

a = 6
b = 4

if a >= b :
    print("a es mayor o igual que b")
# 6) <= menor o igual que

a = 6
b = 15

if  a <= b :
    print("a es menor o igual que b")

#Operadores Logicos
# and : verdadero solamente si ambas condiciones son verdaderas
a = 5
b = 10

if a < b and b > 3:
    print("Ambas condiciones son verdaderas")

# or  : Verdadero si alguna de las condiciones es verdadera

a = 5
b = 3

if a > 10 or b < 5:
    print("al menos una de las condiciones es verdadera")

# # not : invierte el valor de verdad de la condicion

a = False

if not a:
    print("a es falso", a)
else:
    print("a es verdadero")


#Condicionales: Nos ayudan a ejecutar diferentes bloques de codigo segun se cumpla o no ciertas condiciones

edad= 17
if edad > 18 :
    print("Eres menor de edad")
    # Bloque de codigo a ejecutarse si la condicion se cumple

elif edad == 18:
    print("Tienes 18 años") 
    #si la otra condicion es verdadera
  
else:
    print("Eres mayor de edad")
    #bloque de codigo si ninguna de las condiciones anteriores es verdadera
  



