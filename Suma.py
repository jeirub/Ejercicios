print ("Bienvenidos")
ingreso = (input("Ingrese los numeros a sumar dejando espacio entre ellos: "))


numeros = [float (numero) for numero in ingreso.split()]

suma = sum(numeros)

  
print(f"La suma de los numeros es:  {suma}")
