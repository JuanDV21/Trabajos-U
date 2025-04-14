"""Foro semana 5.
Estudiante:
Juan Stiven Marcillo Diaz
FACULTAD DE INGENERIA EN SISTEMAS"""

inventario= []

#Funcion para registrar los productos by Juan
def registrarProductos(): 
    cantidad=int(input("Cuantos productos desea ingresar: ")) 
    for i in range(cantidad): 
        print(f"\n Ingrese los datos del producto No. {i+1}") 
        codigo = input("Codigo: ") 
        nombre = input("Nombre del producto: ") 
        precio = float(input("Precio del producto: "))
        stock = int(input("Stock disponible: ")) 
        producto = { 
        "codigo":codigo, 
        "nombre": nombre, 
        "precio": precio, 
        "stock": stock,
        "vendidos":0 
        } 
        inventario.append(producto)
    print("\n Producto registrado correctamente")

#Funcion para verificar si un producto esta disponible en el inventario
def verificarDisponiblidad(codigo): 
    for producto in inventario: 
        if producto["codigo"] == codigo: 
            if producto["stock"]>0: 
                print(f"Disponible: {producto ['nombre']} existen {producto ['stock']} unidades") 
            else: 
                print(f"{producto ['nombre']} Agotado!!") 
            return 
    print("Producto no encontrado!!")

#Funcion para calcular una compra
def calcularTotalCompra(): 
    if not inventario: 
        print("No hay productos registrados") 
        return
    total = 0.0 
    while True: 
        codigo= input("\n Ingrese el codigo del producto (o 'terminar' para terminar): ")
        if codigo.lower() == 'terminar': 
            break 
        cantidad=int(input("Ingrese la cantidad: "))
        encontrado = False 
        for producto in inventario: 
            if producto ["codigo"] == codigo: 
                encontrado = True 
                if producto["stock"]>=cantidad: 
                    subtotal = producto ["precio"] *cantidad 
                    total +=subtotal #se guarda los productos en subtotal para que cuando el usuario ingrese la palabra "terminar" le arroje el total de la compra
                    producto["stock"] -= cantidad
                    producto["vendidos"] += cantidad
                    print(f"Añadido a su compra el producto : {producto['nombre']} X {cantidad}= {subtotal}")
                else:
                    print(f"Stock insuficiente solo quedan de ese producto {producto['stock']} unidades")
                    break
        if not encontrado:
            print("Codigo del producto incorrecto o no encontrado")
    print(f"\n El Total de la compra es ${total:.2f}")

#Funcion para el informe de los productos mas vendidos 
def generarInformeMasVendido():
    if not inventario: 
        print("No hay productos registrado") 
        return 
    
    print("\n Productos mas vendidos") 
    for producto in inventario: 
        if producto ["vendidos"] ==0: 
            continue 
        print(f"Del {producto['nombre']} hay {producto['vendidos']} unidades vendidas")

#Funcion para mostrar los productos del inventario
def mostrarProductos():
    if not inventario: 
        print("No hay productos registrado") 
        return         

    print("Listo de productos") 
    print("-"*60) 
    print(f"{'Codigo':<10}{'Nombre':<15}{'Precio':<10}{'Stock':<10}{'vendidos':<10}")
    print("-"*60) 
    for producto in inventario: 
        print(f" {producto ['codigo']:<10}{producto['nombre']:<15}{producto['precio']:<10}{producto['stock']:<10}{producto['vendidos']:<10}")
    print("-"*60)

#Funcion para desplegar un menu para el usuario                                                                                         
def menu(): 
    while True: 
        print("\n === MENU PRINCIPAL ===")
        print("1. Registrar Productos") 
        print("2. Verificar Disponibilida") 
        print("3. Realizar Compra") 
        print("4. Ver productos mas Vendidos") 
        print("5. Mostrar productos") 
        print("6. Salir") 
        opcion = int(input("Seleccione la opcion: ")) 
        if opcion ==1: 
          registrarProductos() 
        elif opcion ==2: 
            if not inventario: 
                print("No hay productos Registrados") 
            else: 
                codigo=input("Ingrese el codigo del producto a verificar: ")
                verificarDisponiblidad(codigo)
        elif opcion ==3:
            calcularTotalCompra()
        elif opcion==4:
             generarInformeMasVendido()
        elif opcion==5:
             mostrarProductos()            
        elif opcion ==6:
            print("Hasta pronto y gracaias por su compra!!") 
            break
        else:
            print("Opcion ivalida, intente de nuevo")
menu()              