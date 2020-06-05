class RegistroMateria:
    def __init__(self, p_estudiante, p_apellido, p_carrera):
        self.estudiante = p_estudiante
        self.apellido = p_apellido
        self.carrera = p_carrera
        self.materias = []
    def presentarse(self):
        print("****************Presentacion de {} {}****************".format(self.estudiante, self.apellido))
        for i in self.materias:
            print(i)
        return "Soy el est: {} de la carrera de {}".format(self.estudiante, self.carrera)
    def registrarMateria(self):
        print("Gestión de registro de materias")
        materia = input('Digite la materia: ')
        self.materias.append(materia)
        print( "Materia {} registrada exitosamente.!".format(materia))
        adicional = input("Desea registrar una materia adicional?: y/n: ")
        if (adicional == 'y'):
            self.registrarMateria()
        else:
            return "Materias registradas exitosamente.!!"
    def menu(self):
        opciones = """
        Menu de la aplicación
        1.- Registrar Materias
        2.- Presentarse
                    """
        print(opciones)
        eleccion = int(input('Elija una opción:'))
        if(eleccion == 1):
            print(self.registrarMateria())
            self.menu()
        elif(eleccion == 2):
            print(self.presentarse())
            self.menu()
        else:
            print("Elija del opcion del menu")
            self.menu()


pedro = RegistroMateria("Pedro", "Perez", "Ingeniería de Sistemas")
pablo = RegistroMateria("Pablo", "Mercado", "Ingeniería Comercial")
print(pedro.menu())

