#AREA DE CUADRADO FUNCION
def area_cuadrado(lado):
    area = lado * lado 
    return area

#AREA DE TRIANGULO FUNCION
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

while True:
    print("")
    print("1. Cuadrado.")
    print("2. Triangulo.")
    print("3. Exit.")
    answer = int(input("Choose one: "))

    if answer == 1:
        lado = int(input("Input the side: "))
        resp = area_cuadrado(lado)
        print(resp)
    elif answer == 2:
        base = int(input("Input the base: "))
        altura = int(input("Input the highest: "))
        resp = area_triangulo(base, altura)
        print(resp)
    elif answer == 3:
        print("Exit. ")
        break
    else:
        print
        print("Insert a correct option. ")