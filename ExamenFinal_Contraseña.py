def nivel_contraseña(contraseña):
    if len(contraseña) < 8:
        print("La contraseña es debil.")
    elif len(contraseña) > 8 and len(contraseña) < 15:
        print("La contraseña es media.")
    elif len(contraseña) > 15:
        print("La contraseña es fuerte.")
    else:
        print("Ingrese una contraseña correcta.")

contraseña = input("Ingrese su contraseña: ")
nivel = nivel_contraseña(contraseña)
print(nivel)