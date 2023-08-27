#FUNCION AREA DEL CUADRADO.
def area_cuadrado(lado):
    area = lado * lado
    return area

#FUNCION AREA DEL TRIANGULO.
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
#-------------------------------------------------------------------------------

while True:
    print("1. Area cuadrado")
    print("2. Area triangulo.")
    print("3. Salir.")
    
    respuesta = int(input("¿Que desea hacer?: "))

    if respuesta == 1:
        lado = int(input("Ingrese el valor del lado: "))
        area = area_cuadrado(lado)
        print("El area del cuadrado es:",area)
        print("")
    elif respuesta == 2:
        base = int(input("Ingrese cuanto mide la base del triangulo: "))
        altura = int(input("Ingrese cuanto mide la altura del triangulo: "))
        area = area_triangulo(base, altura)
        print("El area del triangulo es:",area)
        print("")

    if respuesta == 3:
        print("")
        print("Programa finalizado.")
        break