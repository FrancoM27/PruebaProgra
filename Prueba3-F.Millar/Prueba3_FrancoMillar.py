import FnPrueba3_FrancoMillar as fun 

pedido = [] 



while True:
    print("MENU")
    print("1) registrar pedido")
    print("2) listar todos los pedidos")
    print("3) imprimir hoja de ruta")
    print("4) salir") 

    opcion = int(input("ingrese opcion: "))

    if opcion == 1:
        fun.registrar_pedido(pedido) 
    elif opcion == 2:
        fun.listar_pedido(pedido)  
    elif opcion == 3:
        fun.imprimir_hoja(pedido) 
    elif opcion == 4:
        print("Saliendo...")
        break
    else:
        print("opcion invalida, intente ota vez") 
