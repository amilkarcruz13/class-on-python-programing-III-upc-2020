class Persona:
    def __init__(self):
        self.nombre=[]
        self.apellido=[]
        self.genero=[]
        self.telefono=[]
        self.estado=[]
    def menuPersona(self):
        print("""
        MENU DE GESTION DE PERSONAS
        1.- LISTA PERSONA
        2.- DES-HABILITAR REGISTRO
        """)
        eleccion = int(input("Seleccione una opcion: \n"))
        if eleccion ==1:
            self.listarPersona()
            self.menuPersona()
        elif eleccion ==2:
            self.deshabilitar()
            self.menuPersona()
        pass
    def listarPersona(self):
        if self.nombre:
            print("*****LISTADO DE PERSONAS*******")
            for i in range(len(self.nombre)):
                self.detallePersona(i)
        else:
            print("TODAVIA NO SE REGISTRARON PERSONAS.!!")
        pass
    def detallePersona(self, posicion):
        print("NOMBRE: {} {}".format(self.nombre[posicion], self.apellido[posicion]))
        print("GENERO: {}".format(self.genero[posicion]))
        print("TELEFONO: {}".format(self.telefono[posicion]))
        print("ESTADO: {}".format(self.estado[posicion]))
        pass
    def deshabilitar(self):
        self.listarPersona()
        dato = input('Elija una persona de la lista: \n')
        posicion = self.nombre.index(dato)
        self.estado[posicion]=0
        return 'El registro fue dado de baja'

    def saludar(self):
        return "Hola soy la clase persona"
class Obrero(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.especialidad=[]
        self.area=[]

    def menu(self):
        print("""
            MENU DEL MODULO DE GESTION DE OBREROS
            1.- REGISTRAR
            2.- MOSTRAR
            3.- MENU PERSONA
        """)
        eleccion = int(input("Seleccione una opcion: \n"))
        if eleccion == 1:
            print(self.registrar())
            self.menu()
        elif eleccion==2:
            self.listar()
            self.menu()
        elif eleccion==3:
            print(self.menuPersona())
            self.menu()
        elif eleccion == 4:
            print("Gracias por utilizar el sistema")
        else:
            print("Seleccione una opcion valida")
            self.menu()
    def registrar(self):
        nombre = input("Digite el nombre: \n")
        apellido = input("Digite el apellido: \n")
        genero = input("Digite el genero: \n")
        telefono = input("Digite el telefono: \n")
        especialidad = input("Digite el especialidad: \n")
        area = input("Digite el area: \n")
        print(self.guardar(nombre, apellido, genero, telefono, especialidad, area))
        agregarOtro=input("Desea agregar mas registros? s/n \n")
        if agregarOtro == 's' or agregarOtro =='S':
            self.registrar()
        return 'Obreros registrados correctamente.!'
    def guardar(self, nombre, apellido, genero, telefono, especialidad, area):
        self.nombre.append(nombre)
        self.apellido.append(apellido)
        self.genero.append(genero)
        self.telefono.append(telefono)
        self.especialidad.append(especialidad)
        self.area.append(area)
        self.estado.append(1)
        return '{} registrado exitosamente.!!'.format(nombre)
    def listar(self):
        if self.nombre:
            print("*****LISTADO DE OBREROS*******")
            for i in range(len(self.nombre)):
                self.detalle(i)
        else:
            print("TODAVIA NO SE REGISTRARON DATOS.!!")
        pass
    def detalle(self, posicion):
        print("NOMBRE: {} {}".format(self.nombre[posicion], self.apellido[posicion]))
        print("GENERO: {}".format(self.genero[posicion]))
        print("TELEFONO: {}".format(self.telefono[posicion]))
        print("ESPECIALIDAD: {}".format(self.especialidad[posicion]))
        print("AREA: {}".format(self.area[posicion]))
        print("ESTADO: {}".format(self.estado[posicion]))
        pass
obreros = Obrero()
obreros.menu()



