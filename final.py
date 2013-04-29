#Proyecto final


def login():
    acceso=0
    intento=0
    while acceso==0:
        archLeer=open("usuariocontraseña.txt","r")#Abro el archivo de texto            #Comienza editado de Juan Mireles
        articulos=(archLeer.readlines())#Guardo su contenido en una variable           #El archivo en el cual se guarde el usuario y contraseña
        archLeer.close()#Cierro el archivo                                             #Debe de llamarse "usuariocontraseña" y solo puede contener como maximo
        articulos2=[]#Creo variable en blanco                                          #2 nombres de usuario con su respectiva contraseña 
        for i in range(len(articulos)):#Elimino los \n que me apareceran.              # Y tambien la contraseña debe de estar separada por un espacio despues del usuario
            articulos2.append(articulos[i][0:len(articulos[i])-1])                     #en la misma linea que esta. Ejem: Usuario contraseña
        palabras=""                                                                     #                                 Usuario2 contraseña2
        for i in range(len(articulos2)):
            palabras=palabras+articulos[i]
        palabras=palabras.split()
        usuario=input("Usuario: ")
        password=input("Password: ")

        while intento <= 3:
            if usuario==palabras[0] and password==palabras[1] or usuario==palabras[2] and password==palabras[3]:   #Termina editado de Juan Mireles.
                print("")
                return True
            else:
                intento=intento+1
                print("")
                print("Datos incorrectos")
                print("")
            break
        if intento>=3:
            print("")
            print(" *  Las cuentas se han bloqueado porque has intentado mas de 3 veces.   *")
            return False
            break

def menu ():  
    while True:
        print("""==============MENU===============|
|0.-Salir                        |
|1.-Cargar archivo de inventario |
|2.-Agregar artículos            |
|3.-Eliminar artículos           |
|4.-Generar archivo de inventario|""")
        print("¿Qué eliges?")
        try:
            opcion=input(":_")
            if opcion<0 and opcion>4:
                input("Opción no válida")
            else:
                break;
        except ValueError:
            input("Sólo se aceptan números del 0 al 4 como opciones")
        return opcion
        #Esta es la funcion de opciones del menu

log=login()

if log==True:
    print("Bienvenido")
    print()
    #AQUI ADENTO DEL "IF" VA TODO EL PROGRAMA
    menu()
    
    if opcion == 3:
    try:
        c = input("\n¿Qué articulo deseas eliminar?\n>>")
        del inventario[c]
        print("El artículo ha sido removido del inventario")
