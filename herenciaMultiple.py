class Persona:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.estado = 1
    def saludar(self):
        return "Hola soy la clase persona, mi nombre es {}".format(self.nombre)
class Supervisor(Persona):
    def __init__(self, nombre, apellido, carnet, area):
        Persona.__init__(self, nombre, apellido, carnet)
        self.area=area
        self.estadoSupervisor=1
    def saludarSupervisor(self):
        return "Hellow, I'm supervisor class, my name is {}".format(self.nombre)
class Especialidad:
    def __init__(self, titulo, especialidad):
        self.titulo = titulo
        self.especialidad=especialidad
    def saludarEspecialidad(self):
        return "Soy la clase base Especialidad y me reg. con el nombre {}".format(self.titulo)
class LiderArea(Supervisor, Especialidad):
    def __init__(self, nombre, apellido, carnet, area, titulo, especialidad, obra):
        Supervisor.__init__(self, nombre, apellido, carnet, area)
        Especialidad.__init__(self, titulo, especialidad)
        self.obra=obra
    def saludarLiderArea(self):
        print("***LIDER DE AREA***")
        print("NOMBRE: {}".format(self.nombre))
        print("APELLIDO: {}".format(self.apellido))
        print("CARNET: {}".format(self.carnet))
        print("AREA: {}".format(self.area))
        print("TITULO: {}".format(self.titulo))
        print("ESPECIALIDAD: {}".format(self.especialidad))
        print("OBRA: {}".format(self.obra))
        pass

pedro = LiderArea("Pedro", "Mercado", "7712450", "Concreto", "Ing Civil", "Construcción", "Remanzo")
pedro.saludarLiderArea()
