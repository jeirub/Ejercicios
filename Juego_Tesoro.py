print("Bienvenido al juego 'En Busca del Tesoro Perdido'\n")
nombre = input("Ingresa tu nombre: \n")

print(f"Hola, {nombre}! Has llegado a una isla misteriosa en busca de un tesoro legendario.")
print("Se cree que el tesoro está escondido en algún lugar de la isla.\n")

print("Elige tu personaje:")
print("1. Hombre")
print("2. Mujer")

personaje = input("Ingresa el número correspondiente a tu personaje (1/2): ")

if personaje == "1":
    personaje = "Hombre"
elif personaje == "2":
    personaje = "Mujer"
else:
    print("Opción no válida. Seleccionaste un personaje por defecto.")
    personaje = "Aventurero/a"

print(f"¡Eres un {personaje} valiente!\n")

print("Ahora, vamos a explorar la selva...\n")

explorar_selva = input("Has encontrado un pergamino antiguo que parece ser un mapa. ¿Deseas ver el mapa? (si/no): ")

if explorar_selva.lower() == "si":
    print("El mapa muestra que el tesoro se encuentra cerca de una palma con la imagen de un Loro en ella.")
    print("¡Estás en el camino correcto!\n")

    buscar_tesoro = input("¿Quieres seguir buscando el tesoro? (si/no): ")

    if buscar_tesoro.lower() == "si":
        print("El tesoro se encuentra cerca a una palma donde veras la imagen de un Loro en ella!\n\n")
        print("Vas por el camino correcto pero se presenta un terreno de tierra movedizas\n\n")


        opcion = input("Hay 2 caminos por donde dirigirte (derecha/izquierda) \n En la izquierda tendras una selva tenebrosa y en la derecha un hermoso camino: ")
        
        if opcion.lower() == "izquierda":
            print ("La selva tenebrosa")
            print ("Perfecto te encuentras en la selva donde puedes guiarte por una pista que dejaron los piratas\n\n")
            print("Pista A veces los caminos fáciles no siempre llevan a la meta\n\n")
            print("Encuentras unas huellas donde llegas a una cueva, allí esta una botella con un mensaje adentro\n\n")
        

            deseo = input("Deseas abrir la botella? (si/no): ")
            if deseo.lower() == "si":
                    print ("El mensaje en la botella es un acertijo\n\n")
                    print ("En un lugar donde el sol nunca descansa, Bajo las ramas de un árbol antiguo, avanza Tres pasos al norte, y uno al oriente, Allí encontrarás lo que tu corazón siente")

                    acertijo = input ("Deseas hacer caso al acertijo? (si/no): ")
                    if acertijo.lower() == "si":
                        print("Felicitaciones has llegado a la palmera, ahora cava rápidamente antes que salgan los piratas de entre los muertos\n\n")
                        print("Felicitaciones !!Has logrado obtener el Tesoro!!")

                        if acertijo.lower() == "no":
                            print("En esta ocasión el acertijo tenia razón, ahora no encontraras el tesoro. Game over")



            if deseo.lower() == "no":
                print ("Morirás en la cueva, nunca encontraras el tesoro Game over ")


        if opcion.lower() == "derecha":
            print ("El rio por aguas cristalinas donde hay un bote")
            print("Lo sentimos este bote esta dañado y has caído a las profundidadesGame over")


    
    else:
        print("Decidiste no buscar el tesoro. ¡Fin del juego!")
else:
    print("Lo siento, pero nunca encontrarás el tesoro. ¡Game over!")

print("Fin del juego.")
