#Menu de opciones 
#1. ingresar producto de bodega
#2. verificar los productos en bodega
#3. buscar un producto en la bodega
#4. editar un producto en la bodega
#5. retirar un producto bodega 

#producto:nombre,codigo,descripcion,foto,precio, cantidaenbodega,fechaEntradaBodega

opcion=0
print("TIENDA EL GANGAZO")
print("1.Ingresa el producto")
print("2.Verificar los productos")
print("3.Buscar un producto")
print("4. Editar un producto ")
print("5. Retira un producto")
print("6. Salir")
print("******************")

Producto = []

while(opcion != 6):
    Producto = {}
    opcion=int(input("Digita la opcion deseada:  "))
    if opcion==1:
        Producto["Nombre"] = input("Digita el nombre del producto: ")
        Producto["codigo"] = int(input("Digita el codigo del producto: "))
        Producto["Descripcion"] = input("Digita la descripcion del producto: ")
        Producto["Foto"] = input("Digita el url de la foto: ")
        Producto["Precio"] = float(input("Digita el precio del producto: "))
        Producto["stock"] = int(input("Digita el stock del producto: "))
        Producto["fechaEntradaBodega"] = input("Digita la fecha de entrada : ")
        
    elif opcion==2:
        for productoSelecionado in Productos:
            print(f"Codigo ={productoSelecionado['Codigo']}")
            print(f"Nombre ={productoSelecionado['Nombre']}")
            print(f"Descripcion ={productoSelecionado['Descripcion']}")
            print(f"Foto ={productoSelecionado['Foto']}")
            print(f"Precio ={productoSelecionado['Precio']}")
            print(f"Cantida en bodega ={productoSelecionado['Stock']}") 
            print(f"Fecha de entrada ={productoSelecionado['FechaEntradaBodega']}")
   
    elif opcion==3:
    elif opcion==4:
    elif opcion==5:
    elif opcion==6:

else:
    print("Opcion invalida, vuelve a intentarlo")


