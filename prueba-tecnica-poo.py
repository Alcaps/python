# Implementacion de una lista musical Utilizando clases. (Playlist)

class Cancion:
    def __init__(self, name,artist):
        self.name = name
        self.artist = artist
       #self.gender = gender
        
class Playlist:
    def __init__(self):
        self.list = {}

    def agregar_cancion(self, cancion):
        if cancion.artist in self.list:
            #Verificamos que la cancion existe para ese artista
            if cancion.name not in self.list[cancion.artist]:
                self.list[cancion.artist].append(cancion.name)
                print(f"La cancion {cancion.name} ha sido agregada a {cancion.artist}")
            else:
                print(f"La cancion {cancion.name} ya existe en la lista de {cancion.artist}")
        else:
            #Si el artista no existe, lo agregamos con la cancion
            self.list[cancion.artist] = [cancion.name]
            print(f"El artista {cancion.artist} ya se agrego a la lista con la cancion {cancion.name}.")

    def mostrar_lista(self):
        print("--------------------------------------------------------------------------")
        print("MY LIST: ")
        print()
        if not self.list:
            print("La lista musical esta vacia")
            return
        for artist,canciones in self.list.items():
            #Imprimir las canciones directamente accediendo a los atributos
            print(f"{artist}: {', '.join(canciones)}")



#Ejemplo de uso

lista_musical = Playlist()

#Crear algunas canciones

cancion1 = Cancion("Despacito", "Luis Fonsi")
cancion2 = Cancion("Incondicional", "Luis Miguel")
cancion3 = Cancion("Historia de un amor", "Luis Miguel")
cancion4 = Cancion("Hey Jude", "The Beatles")
cancion5 = Cancion("Get Back", "The Beatles")
cancion6 = Cancion("7 Years", "Lukes Graham")
cancion7 = Cancion("Incondicional", "Luis Miguel")
cancion8 = Cancion("Yellow Submarine","The Beatles")

#Agregar cancion a la lista musical

lista_musical.agregar_cancion(cancion1)
lista_musical.agregar_cancion(cancion2)
lista_musical.agregar_cancion(cancion3)
lista_musical.agregar_cancion(cancion4)
lista_musical.agregar_cancion(cancion5)
lista_musical.agregar_cancion(cancion6)
lista_musical.agregar_cancion(cancion7)
lista_musical.agregar_cancion(cancion8)

# Mostrar la lista musical

lista_musical.mostrar_lista()