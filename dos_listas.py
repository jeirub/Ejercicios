print ("Bienvenidos")

lista_uno = (input("Lista 1 Ingresa una lista de numeros: "))

lista_dos=(input("Lista 2 Ingresa una lista de numeros: "))


lista1 = [float(numero) for numero in lista_uno.split()]
lista2 = [float(numero) for numero in lista_dos.split()]


if len (lista1) != len(lista2):
    print ("Las listas deben de tener la misma longitud")

else:
    suma_lista = []

    for i in range (len(lista1)):
        suma = lista1[i] + lista2[i]
        suma_lista.append(suma)

        print("Lista de suma de elementos en la misma posicion: ")
        print(suma_lista)