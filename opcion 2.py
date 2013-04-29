if op == 2:
        a = input("cual articulo quieres agregar?")
        b = input("cuantos son?")
        if a in inventario:
            print("ya cuento con ese articulo")
        else:
            inventario[a]=b
        print(inventario)
