class Mascota:
    def __init__(self):
        self.codigo = []
        self.nombre = []
        self.edad = []
        self.animal = []
        self.raza = []
        self.vacuna = []
        self.estado = []
    def menu(self):
        opciones = """
        *******SISTEMA DE MASCOTAS*******
        1.- Registrar Mascotas
        2.- Kardex de Mascotas
        3.- Vacunar Mascota
        4.- Salir
        """
        print(opciones)
        eleccion = int(input("Elija una opcion del menu: \n"))
        if(eleccion == 1):
            print(self.agregarMascota())
            self.menu()
        elif (eleccion == 2):
            print(self.kardex())
            print(self.verMenu())
        elif (eleccion ==3):
            print(self.agregarVacuna())
            print(self.verMenu())
        elif(eleccion==4):
            print("Transacciones realizadas correctamente")
        else:
            print("***DIGITE UNA OPCION DEL MENU***")
            self.menu()

    def verMenu(self):
        eleccion = input("Desea volver al menu: s/n \n")
        if (eleccion == 's' or eleccion == 'S'):
            self.menu()
        else:
            return "Transacciones realizadas correctamente"

    def agregarMascota(self):
        print("***AGREGAR MASCOTAS***")
        code = input("Ingrese el codigo para la mascota: \n")
        name = input("Ingrese el nombre su mascota: \n")
        age = int(input("Ingrese la edad en meses: \n"))
        animal = input("Ingrese el tipo de animal de su mascota: \n")
        type = input("Ingrese la raza: \n")
        print(self.guardarMascota(code, name, age, animal, type))
        agregarOtro = input("Desea registrar mascota.? s/n \n")
        if ( agregarOtro == 's' or agregarOtro == 'S'):
            self.agregarMascota()
        return "Mascota(s) registrada(s) correctamente.!"

    def guardarMascota(self, codigo, nombre, edad, animal, raza):
        self.codigo.append(codigo)
        self.nombre.append(nombre)
        self.edad.append(edad)
        self.animal.append(animal)
        self.raza.append(raza)
        self.vacuna.append(0)
        self.estado.append(1)
        return "La mascota {} fue registrada exitosamente.!".format(nombre)
    def kardex(self):
        if (self.codigo):
            for posicion in range(len(self.nombre)):
                self.descripcion(posicion)
            return "Kardex cargado correctamente"
        else:
            return "Todavia no hay datos registrados"


    def descripcion(self, posicion):
        print("****MASCOTA {}***".format(self.codigo[posicion]))
        print("Nombre: {} ".format(self.nombre[posicion]))
        print("Edad: {} meses".format(self.edad[posicion]))
        print("Tipo Animal: {}".format(self.animal[posicion]))
        print("Raza: {}".format(self.raza[posicion]))
        if (self.vacuna[posicion] == 1 ):
            print("Vacunado: SI".format(self.vacuna[posicion]))
        else:
            print("Vacunado: NO".format(self.vacuna[posicion]))
        pass
    def buscarMascota(self):
        codigo = input("Ingrese el codigo de la mascota: \n")
        posicion = self.codigo.index(codigo)
        return posicion

    def agregarVacuna(self):
        posicion = self.buscarMascota()
        return self.vacunarMascota(posicion)

    def vacunarMascota(self, posicion):
        self.vacuna[posicion] = 1
        return "La mascota {} fue vacunada exitosamente.!".format(self.nombre[posicion])

mascotas = Mascota()
mascotas.menu()
