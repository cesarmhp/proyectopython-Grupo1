#Proyecto final
#===========================================EMPIEZA PARTE DE LECTURA DEL ARCHIVO Y CONVERTIRLO A DICCIONARIO=========

try:
    productos = []
    numproducto = []
    inventario = open("inventario.txt","r")
    productos = inventario.readlines()
    inventario.close
    inventario = {}
except IOError:
    print ("El archivo no se encuentra")

#Se separa el artículo de la ccantidad
for i in range(len(productos)):
    separador = productos[i].split(" ")
    productos[i] = separador

#Se le quita el \n a el número de artículos y se convierte a enteros, queda guardado en una lista llamada numproducto
for i in range(len(productos)-1):
    numproducto.append(productos[i][1])
    numproducto[i] = numproducto[i][:len(numproducto[i])-1]
    numproducto[len(numproducto)-1] = numproducto[len(numproducto)-1][:len(numproducto[len(numproducto)-1])]
    numproducto[i] = int(numproducto[i])
numproducto.append(productos[len(productos)-1][1])
numproducto[len(numproducto)-1] = int(numproducto[len(numproducto)-1])

#Se elimina el número de productos de la lista original quedando sólo el nombre
for i in range(len(productos)):
    productos[i] = productos[i][0]  

#Se integran las dos listas (productos y numproducto) en un diccionario llamado inventario.
for i in range(len(productos)):
    inventario[productos[i]] = numproducto[i]

#=========================================TERMINA LECTURA DEL ARCHIVO Y CONVERSIÓN A DICCIONARIO======================

#======================================COMIENZA PROCESO DE INICIO DE SESIÓN===========================================
def login():
    acceso = 0
    intento = 0
    while acceso == 0:
        archLeer = open("usuariocontraseña.txt","r")#Abro el archivo de texto            #Comienza editado de Juan Mireles
        articulos = (archLeer.readlines())#Guardo su contenido en una variable           #El archivo en el cual se guarde el usuario y contraseña
        archLeer.close()#Cierro el archivo                                               #Debe de llamarse "usuariocontraseña" y solo puede contener como maximo
        articulos2 = []#Creo variable en blanco                                          #2 nombres de usuario con su respectiva contraseña 
        for i in range(len(articulos)):#Elimino los \n que me apareceran                 # Y tambien la contraseña debe de estar separada por un espacio despues del usuario
            articulos2.append(articulos[i][0:len(articulos[i])-1])                       #en la misma linea que esta. Ejem: Usuario contraseña
        palabras = ""                                                                    #                                 Usuario2 contraseña2
        for i in range(len(articulos2)):
            palabras = palabras+articulos[i]
        palabras = palabras.split()
        usuario = input("Usuario: ")
        password = input("Password: ")

        while intento <= 3:
            if usuario==palabras[0] and password==palabras[1] or usuario==palabras[2] and password==palabras[3]:   #Termina editado de Juan Mireles.
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
            print(" *  Las cuentas se han bloqueado porque has intentado mas de 3 veces   *")
            return False
            break;
            
#===================================TERMINA PROCESO DE INICIO DE SESIÓN=================================================


def menu (): #Se imprimira un menu con las diferentes opciones que tendra el usuario, de las cuales elegira la que sea mejor para el
    print("==============MENU===============")
    print("0.-Salir ")
    print("1.-Cargar archivo de inventario ")
    print("2.-Agregar artículos ")
    print("3.-Eliminar artículos ")
    print("4.-Generar archivo de inventario")
    print("5.-Imprimir inventario ")
    print("¿Cuál opción eliges?")
    try:
        while True:
            opcion=int(input(":_"))
            if opcion<0 or opcion>4: #Si la opción no se encuentra en el rango marcara error
                input("Opción no válida")
            else:
                break;
    except ValueError:
        input("Sólo se aceptan números del 0 al 4 como opciones")
    return o


log = login()
if log == True:
    print("Bienvenido")
    print()

#*******************************AQUI EMPIEZA EL PROGRAMA***************************************************************
while True:
    opcion=menu()

    if opcion == 0:
        print ("Adios!! (:")
        break
      
    if opcion == 2:
            llave = input("¿Qué artículo deseas agregar?: ")
            valor = int(input("¿Cuántos artículos deseas agregar?: "))
            llave = llave[0].upper()+ llave[1:].lower()
            if llave in inventario:
                for i in range(len(inventario)):
                    valor = sum(valor,inventario[valor]) #Aquí me falta agregar que se sumen los artículos en caso de que se quieran agregar más del mismo
            if llave not in inventario:
                inventario[llave] = valor
                    
    if opcion == 3:
        c = input("¿Qué articulo deseas eliminar?: ")
        c = c[0].upper() + c[1:].lower()
        try:
            if c in inventario:
                print("Actualmente hay", inventario[c], c)
                x = int(input("¿Cuántos deseas eliminar?: "))
            print(inventario([cx])) #Aquí me falta hacer que se resten los artículos en caso de que no se eliminen todos
        except KeyError as c:
            print("Error", c, "no se encuentra en el inventario")
        except ValueError:
            print("Escribe sólo el nombre del artículo")
            
    if opcion == 4:
        try:
            archiescri = open("inventario.txt","w")
            for i in lista:
                archiescri.write(str(i)+"\n")
            archiescri.close()
            print ("El inventario se ha guardado en el archivo")
        except IOError:
            print("Error. No se puede escribir en el archivo")
        print("\n")
                
    if opcion == 5:
        print("===================")
        print(" ARTICULO - #")
        print("===================")
        for i in (inventario):
            print(i," - ",inventario[i])



