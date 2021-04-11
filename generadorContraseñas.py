import random 

def insertNum():
    numero=str(random.randint(0,9))
    return numero

def insertLetra():
    codigoLetter=random.randint(97,122)
    return chr(codigoLetter)

def insertLetraMayuscula():
    codigoLetter=random.randint(65,90)
    return chr(codigoLetter)

def generador(tam, may):
    password=""
    # los numeros van del 48 al 59
    # las letras minusculas van del 97 al 122
    # las letras mayusculas van del 65 al 90
    # elegimos la cantidad de numeros que debe de tener la password
    for i in range (tam):
        tipo=random.randint(1,3)
        if(tipo%3==0):
            password= password +insertNum()
        else:
            if(tipo%3==1):
                password= password +insertLetra()
            else:
                if(may=="s" or may =="S"):
                    password= password +  insertLetraMayuscula()
                else:
                    password= password +insertLetra()
    return password

print("-------Generador de passwords @rh -------")
salir="f"
while(salir!="s" and salir !="S"):
    salir=input("Para salir pulse s/S, para continuar pulse n/N para generar la contraseña seguido de enter \n")
    if(salir !="s" and salir !="S"):
        try:
            tamanio=int(input("Introduzca el tamanio de la password seguido de enter \n"))
            mayus=input("Para agregar mayusculas a la password pulse s/S para continuar pulse n/N para no agregar mayusculas seguido de enter \n")
            password=generador(tamanio,mayus)
            print("Password: "+password)
        except ValueError:
            print("No has introducido un valor numerico")



