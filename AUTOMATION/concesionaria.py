# 5 clientes van  a pedir un auto
# Preguntar nombre de pila, marca, puertas, color
# ford 100k, chevrolet 120k, fiat 80k
# puertas 2 50k, 4 65k, 5 78k
# blanco 10 k, azul 20k, negro 30k
# imprimir los datos de cada compra + e precio total

# Funciones
def precio_marca(marca):
    if marca == "Ford":
        p1 = 100000
    elif marca == "Chevrolet":
        p1 = 120000
    elif marca == "Fiat":
        p1 = 80000
    return p1

def precio_puertas(puertas):
    if puertas == 2:
        precio = 50000
    elif puertas == 4:
        precio = 65000
    elif puertas == 5:
        precio = 78000
    return precio

def precio_color(color):
    precio
    if color == "blanco":
        precio = 10000
    elif color == "azul":
        precio = 20000
    elif color == "negro":
        precio = 30000
    return precio

def precio_auto(marca, puertas, color):
    return precio_marca(marca) + precio_puertas(puertas) + precio_color(color)

def imprimir_ticket(nombre, apellido, marca, puertas, color):
    print("Cliente: " + nombre +" "+ apellido,
    "Auto: ",
    "Marca: " + marca + " = " + str(precio_marca(marca)),
    "Cantidad de puertas: " + puertas + " = " + str(precio_puertas(puertas)),
    "Color: " + color + " = " + str(precio_color(color)),
    "Total: ")# + str(precio_auto(marca, puertas, color)))

# Pedir Datos
nombre_cliente = input("Nombre: ")
apellido_cliente = input("Apellido: ")
marca = input("Desea Ford, Chevrolet, o Fiat?: ")
puertas = input("Cuantas puertas? 2, 4 o 5: ")
color = input("Color deseado entre blanco, negro y azul: ")

# Imprimir el ticket
imprimir_ticket(nombre_cliente, apellido_cliente, marca, puertas, color)

# Se puede hacer con For in.... pero.... em... where does it say...
# Contador(while) vs acumulador(for)