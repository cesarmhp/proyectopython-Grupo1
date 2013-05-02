
#======================================COMIENZA FUNCION DE PROCESO DE INICIO DE SESIÓN===========================================
def login():
    acceso = 0
    intento = 0
    while acceso == 0:
        archLeer = open("usuariocontraseña.txt","r")#Abro el archivo de texto #Comienza editado de Juan Mireles
        articulos = (archLeer.readlines())#Guardo su contenido en una variable #El archivo en el cual se guarde el usuario y contraseña
        archLeer.close()#Cierro el archivo #Debe de llamarse "usuariocontraseña" y solo puede contener como maximo
        articulos2 = []#Creo variable en blanco #2 nombres de usuario con su respectiva contraseña
        for i in range(len(articulos)):#Elimino los \n que me apareceran # Y tambien la contraseña debe de estar separada por un espacio despues del usuario
            articulos2.append(articulos[i][0:len(articulos[i])-1]) #en la misma linea que esta. Ejem: Usuario contraseña
        palabras = "" # Usuario2 contraseña2
        for i in range(len(articulos2)):
            palabras = palabras+articulos[i]
        palabras = palabras.split()
        usuario = input("Usuario: ")
        password = input("Password: ")

        while intento <= 3:
            if usuario==palabras[0] and password==palabras[1] or usuario==palabras[2] and password==palabras[3]: #Termina editado de Juan Mireles.
                print("")
                return True
            else:
                intento = intento + 1
                print("")
                print("Datos incorrectos")
                print("")
            break;
        if intento >= 3:
            print("")
            print(" * Las cuentas se han bloqueado porque has intentado mas de 3 veces *")
            return False
            break;
            
#===================================TERMINA FUNCION DE PROCESO DE INICIO DE SESIÓN=================================================
