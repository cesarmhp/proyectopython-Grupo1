#Proyecto final

#======================================COMIENZA FUNCION DE PROCESO DE INICIO DE SESIÓN===========================================
from login import login            
#===================================TERMINA FUNCION DE PROCESO DE INICIO DE SESIÓN=================================================


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


#===============================EMPIEZA FUNCION DEL MENU===============================================================
def menu (): #Se imprimira un menu con las diferentes opciones que tendra el usuario, de las cuales elegira la que sea mejor para el
    print("==============MENU===============")
    print("0.-Salir ")
    print("1.-Agregar artículos")
    print("2.-Eliminar artículos ")
    print("3.-Generar archivo de inventario ")
    print("4.-Imprimir inventario")
    print("¿Cuál opción eliges?")
    while True:
        try:
            opcion=int(input(":_"))
            if opcion<0 or opcion>5: #Si la opción no se encuentra en el rango marcara error
                input("Opción no válida")
            else:
                break;
        except ValueError:
            input("Sólo se aceptan números del 0 al 4 como opciones")
    return opcion

#================================================TERMINA FUNCION DEL MENU==========================================

#*******************************AQUI EMPIEZA EL PROGRAMA***************************************************************

log = login()
if log == True:
    print("Bienvenido")
    print()
    while True:
        opcion=menu()

        if opcion == 0:#=========================TERMINADO============
            input ("\nPresione ENTER para salir")
            break
      
        if opcion == 1:#===============================TERMINADO======
                llave = input("¿Qué artículo deseas agregar?: ")
                valor = int(input("¿Cuántos artículos deseas agregar?: "))
                llave = llave[0].upper()+ llave[1:].lower()
                if llave in inventario:
                    inventario[llave] = inventario[llave]+ valor
                if llave not in inventario:
                    inventario[llave] = valor
                    
        if opcion == 2:
            c = input("¿Qué articulo deseas eliminar?: ")
            c = c[0].upper() + c[1:].lower()
            try:
                if c in inventario:
                    print("Actualmente hay", inventario[c], c)
                    x = int(input("¿Cuántos deseas eliminar?: "))
                    inventario[c]=inventario[c]-x
                    if inventario[c] <= 0:
                        del inventario[c]
                        print("Ya no se encuentra en el inventario")
                print(inventario[c],c) #Ya esta que se elimine el numero de productos que se deee (Daniel Fdz y Emanuel Valdez)
            except KeyError as c:
                print("Error", c, "no se encuentra en el inventario")
            except ValueError:
                print("Escribe sólo el nombre del artículo")
            #Ya elimina el producto del inventario, pero sigue diciendo lo del error en la excepcion pero dijo el profe que estaba bien
            #Opcion 3 TERMINADA NO!! le muevan
        if opcion == 3:
            try:
                archiescri = open("inventario.txt","w")
                for i in inventario:
                    archiescri.write(str(i)+" "+str(inventario[i])+"\n")
                archiescri.close()
                print ("El inventario se ha guardado en el archivo")
            except IOError:
                print("ERROR. NO SE PUEDE ESCRIBIR EN EL ARCHIVO")
            print("\n")
                
        if opcion == 4:#================TERMINADO==============
            print("\n===================")
            print(" ARTICULO - #")
            print("===================")
            for i in (inventario):
                print(i," - ",inventario[i])




