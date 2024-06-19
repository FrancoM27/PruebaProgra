
sectores = ['centro', 'norte', 'sur'] 


def registrar_pedido(pedido): 
    cliente = input("ingrese nombre y apellido: ")
    direccion = input("ingrese direccion: ")
    sector = input("ingrese sector(centro, norte, sur): ") 
    while sector not in sectores:
        print("ingreso invalido, intente otra vez")
        sector = input("ingrese sector(centro, norte, sur): ")
    
    while True:
        npaqueteP = int(input("ingrese numero paquetes pequeños: "))
        if npaqueteP == str:
            print("ingreso invalido, intente otra vez")
        else:
            break
           
    while True:
        nPaqueteM = int(input("ingrese numero paquetes medianos: ")) 
        if nPaqueteM == str:
            print("ingreso invalido, intente otra vez")
        else:
            break    
        
    while True:
        npaqueteG = int(input("ingrese numero paquetes grandes: ")) 
        if npaqueteG == str:
            print("ingreso invalido, intente otra vez")
        else:
            break 

    pedido.append({
        'cliente':cliente,
        'direccion':direccion,
        'sector':sector,
        'paquete pequeño':npaqueteP,
        'paquete mediano':nPaqueteM,
        'paquete grande':npaqueteG 

    })

 
def listar_pedido(pedido): 
    for pedidos in pedido:
        print(pedidos) 


def imprimir_hoja(pedido):
    pedidos_a_impiimir = input("imprimir todo presione enter")
    if pedidos_a_impiimir == "":
        pedidos_a_impiimir = pedido
        nombre_archivo = 'pedidos_a_imprimir.txt'  

    
    

    with open(nombre_archivo, 'w') as archivo: 
        for pedido in pedidos_a_impiimir:
            archivo.write(f'nombre y apellido: {pedido['cliente']}\n')  
            archivo.write(f'Direcciones: {pedido['direccion']}\n') 
            archivo.write(f'Sectores: {pedido['sector']}\n') 
            archivo.write(f'pauetes pequeños: {pedido['paquete pequeño']}\n') 
            archivo.write(f'paquetes medianos: {pedido['paquete mediano']}\n') 
            archivo.write(f'paquetes grandes: {pedido['paquete grande']}\n\n')  
