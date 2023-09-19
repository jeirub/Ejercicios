print ("Bienvenidos")

ingreso = (input("Ingresa una lista de palabras: "))

palabras = ingreso.split()

letra = input ("Ingrese una letra para filtrar las palabras: ")

print (f"palabras que comiencen con '{letra}': ")

for palabra in palabras:
    if palabra.startswith(letra):
        print (palabra)

