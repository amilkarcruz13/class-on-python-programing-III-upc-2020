from datetime import datetime
class Ventas:
    def __init__(self, cliente):
        self.cliente = cliente
        self.producto = []
        self.precio = []
    def menu(self):
        opciones = """
        ***********MENU SUPERMERCADO**************
        1.- Agregar al Carrito
        2.- Mostrar Carrito
        3.- Mostrar Total a Pagar
        4.- Salir
        """
        print(opciones)
        eleccion = int(input('Elija una opcion: \n'))
        if eleccion == 1:
            print(self.agregarCarrito())
            self.menu()
        elif eleccion == 2:
            print(self.mostrarCarrito())
            self.menu()
        elif eleccion == 3:
            print("{}".format(self.totalAPagarSum()))
            self.menu()
        elif eleccion == 4:
            print("Fin de la transacción")
        else:
            print("Elija una opcion del menu.!!")
            self.menu()

    def mostrarCarrito(self):
        if  self.producto:
            print("**********DETALLE DE VENTA****************************")
            print("CLIENTE: {}".format(self.cliente))
            print("FECHA: {}".format(datetime.now()))
            print("**********LISTA DE PRODUCTOS DEL CARRITO**************")
            print("--PRODUCTO--      --PRECIO--")
            i = 0
            while i < len(self.producto):
                print("{}          {} Bs.".format(self.producto[i], self.precio[i]))
                i = i +1
            print("--EL TOTAL A PAGAR ES: {} Bs.--".format(self.totalAPagarSum()))
            return "*********LISTA DE PRODUCTOS DEL CARRITO***********"
        else:
            return "{} NO AGREGO TODAVIA PRODUCTOS AL CARRITO".format(self.cliente)
    def totalAPagar(self):
        total = 0
        i = 0
        while i < len(self.precio):
            total = total + self.precio[i]
            i = i + 1
        return total
    def totalAPagarSum(self):
        return sum(self.precio)

    def agregarCarrito(self):
        producto = input("Ingresar producto: \n")
        precio = int(input("Ingresar precio: \n"))
        print(self.guardarCarrito(producto, precio))
        agregarOtro = input("Desea agregar mas productos al carrito? y/n: \n")
        if agregarOtro == 'y':
            self.agregarCarrito()
        return "Productos agregados al carrito exitosamente"

    def guardarCarrito(self, producto, precio):
        self.producto.append(producto)
        self.precio.append(precio)
        return "Producto {} agregado correctamente".format(producto)


pedro = Ventas("Pedro Perez")
pedro.menu()