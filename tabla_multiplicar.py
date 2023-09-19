print ("Bienvenido")

numero = int (input("Ingrese el numero para la tabla de multiplicacion: "))

print (f"Tabla de multiplicar del {numero}: ")

for i in range (1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")