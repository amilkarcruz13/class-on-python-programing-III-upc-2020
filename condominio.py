class Condominio:
    def __init__(self):
        self.codigo = []
        self.departamento = []
        self.piso = []
        self.dimension = []
        self.ocupado = []
        self.tipoArrendamiento = []
        self.precioAlquiler = []
        self.precioAnticretico = []
        self.precioVenta = []

    def menu(self):
        opciones = """
            ***MENU DEL SISTEMA***
            1.- REGISTRAR
            2.- KARDEX
            3.- VER DEPARTAMENTOS DISPONIBLES
            4.- VER PRECIO VENTA
            5.- VER PRECIO ANTICRETICO
            6.- VER PRECIO DE ALQUILER
            7.- SALIR
        """
        print(opciones)
        eleccion = int(input("Seleccione una opcion: \n"))
        if (eleccion == 1):
            print(self.agregarDpto())
            self.volverMenu()
        elif (eleccion == 2):
            self.mostrarListado()
            self.volverMenu()
        elif (eleccion == 3):
            self.verDptoDisponibles()
            self.volverMenu()
        elif (eleccion == 4):
            self.verPrecioVenta()
            self.volverMenu()
        elif (eleccion == 5):
            self.verPrecioAnticretico()
            self.volverMenu()
        elif (eleccion == 6):
            self.verPrecioAlquiler()
            self.volverMenu()
        elif (eleccion == 7):
            print("Gracias por utilizar el sistema")
        else:
            print("Seleccione una opcion correcta")
            self.volverMenu()
        pass

    def obtenerCodTipoArrendamiento(self, v_tipo_arrendamiento):
        if (v_tipo_arrendamiento == 'al' or v_tipo_arrendamiento == 'AL'):
            return 1
        elif (v_tipo_arrendamiento == 'an' or v_tipo_arrendamiento == 'AN'):
            return 2
        elif (v_tipo_arrendamiento == 've' or v_tipo_arrendamiento == 'VE'):
            return 3

    def obtenerCodOcupado(self, v_ocupado):
        if (v_ocupado == 's' or v_ocupado == 'S'):
            return 1
        elif (v_ocupado == 'n' or v_ocupado == 'N'):
            return 0

    def obtenerValorOcupado(self, ocupado):
        if (ocupado == 1):
            return "Si"
        elif (ocupado == 0):
            return "No"

    def obtenerValorArrendamiento(self, tipoArrendamiento):
        if (tipoArrendamiento == 0):
            return "Disponible"
        elif (tipoArrendamiento == 1):
            return "Alquiler"
        elif (tipoArrendamiento == 2):
            return "Anticretico"
        elif (tipoArrendamiento == 3):
            return "Venta"

    def agregarDpto(self):
        departamento = int(input('Ingrese el numero de Dpto: \n'))
        piso = int(input("Ingrese el Piso: \n"))
        dimension = int(input("Ingrese la Dimensión en mts2: \n"))
        v_ocupado = input("Seleccione si esta ocupado: s/n \n")
        ocupado = self.obtenerCodOcupado(v_ocupado)
        if (ocupado == 1):
            v_tipo_arrendamiento = input(
                "Seleccione el tipo de arrendamiento: al/an/ve \n")
            tipo_arrendamiento = self.obtenerCodTipoArrendamiento(
                v_tipo_arrendamiento)
        elif (ocupado == 0):
            tipo_arrendamiento = 0
        p_al = int(input("Ingrese el precio de aquiler en Dolares $: \n"))
        p_an = int(input("Ingrese el precio de anticretico en Dolares $: \n"))
        p_v = int(input("Ingrese el precio de venta en Dolares $: \n"))
        print(self.guardarDpto(departamento, piso,
                               dimension, ocupado, tipo_arrendamiento, p_al, p_v, p_an))
        agregarMas = input("Desea registrar mas Dptos: s/n \n")
        if (agregarMas == 's' or agregarMas == 'S'):
            self.agregarDpto()
        return "Dptos registrados correctamente"

    def guardarDpto(self, dpto, piso, dim, ocupado, t_a, p_al, p_v, p_an):
        cod = "{}-{}".format(piso, dpto)
        self.codigo.append(cod)
        self.departamento.append(dpto)
        self.piso.append(piso)
        self.dimension.append(dim)
        self.ocupado.append(ocupado)
        self.tipoArrendamiento.append(t_a)
        self.precioAlquiler.append(p_al)
        self.precioVenta.append(p_v)
        self.precioAnticretico.append(p_an)
        self.listarDpto()
        return " El dpto {} fue registrado con el codigo {} exitosamente".format(dpto, cod)

    def listarDpto(self):
        for i in range(len(self.departamento)):
            self.detalle(i)
        pass

    def detalle(self, posicion):
        print("***DEPARTAMENTO {}***".format(self.codigo[posicion]))
        print("Numero de Dpto: {}".format(self.departamento[posicion]))
        print("Piso: {}".format(self.piso[posicion]))
        print("Dimensión: {} mts2".format(self.dimension[posicion]))
        valorOcupado = self.obtenerValorOcupado(self.ocupado[posicion])
        print("Ocupado: {}".format(valorOcupado))
        valorTipoArrendamiento = self.obtenerValorArrendamiento(
            self.tipoArrendamiento[posicion])
        print("Tipo de Arrendamiento: {}".format(valorTipoArrendamiento))
        print("Precio de Alquiler: {} $".format(self.precioAlquiler[posicion]))
        print("Precio de Anticretico: {} $".format(
            self.precioAnticretico[posicion]))
        print("Precio de Venta: {}$".format(self.precioVenta[posicion]))
        print("----------------------------")
        pass


condominio = Condominio()
condominio.menu()
# CONDOMINIO DE 60 DPTOS, DE 5 PISOS, EN CADA PISO EXISTEN 12 DPTOS, 1-1 - 1-12
# DPTO 2-13 -> 2-24
