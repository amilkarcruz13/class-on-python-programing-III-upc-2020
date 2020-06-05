from datetime import datetime


class Persona:
    def __init__(self, p_nombre, p_apellido, p_celular, p_direccion, p_fecha_nac):
        self.nombre = p_nombre
        self.apellido = p_apellido
        self.celular = p_celular
        self.direccion = p_direccion
        self.fecha_nac = p_fecha_nac
        self.estado = 1

    def saludar(self):
        respuesta = ""
        if (self.estado == 1):
            respuesta = "Soy %s %s vivo en %s" % (
                self.nombre, self.apellido, self.direccion)
        return respuesta

    def estadoSistema(self):
        if (self.estado == 1):
            return "Soy %s , Estoy Habilitado/a en el sistema" % (self.nombre)
        else:
            return "Soy %s , No Estoy Habilitado/a  en el sistema" % (self.nombre)

    def darBaja(self):
        self.estado = 0
        return "Ahora %s esta de Baja en el sistema" % (self.nombre)

    def darAlta(self):
        if (self.estado == 1):
            return "Advertencia.! , %s ya esta de Alta" % (self.nombre)
        else:
            self.estado = 1
            return "Ahora %s esta de Alta en el sistema" % (self.nombre)

    def obtenerEdad(self):
        fecha_nacimiento = datetime.strptime(self.fecha_nac, "%d/%m/%Y")
        hoy = datetime.now()
        fecha_edad = hoy - fecha_nacimiento
        edad = int(fecha_edad.days / 365)
        return "{} tiene {} años".format(self.nombre, edad)


pedro = Persona("Pedro", "Perez", "76352140",
                "Zona Primer Anillo", "01/01/1980")
pablo = Persona("Pablo", "Mercado", "76365210",
                "Zona Norte 2do anillo", "12/12/1984")
vilma = Persona("Vilma", "Torrez", "69365210",
                "Zona Primer anillo", "28/04/1985")
betty = Persona("Betty", "Cardozo", "76365210",
                "Zona Norte 2do anillo", "18/06/1987")
print("******************************")
print(betty.fecha_nac)
print(betty.obtenerEdad())
print(pablo.fecha_nac)
print(pablo.obtenerEdad())
print(pedro.fecha_nac)
print(pedro.obtenerEdad())
print(vilma.fecha_nac)
print(vilma.obtenerEdad())
print("******************************")
# print(pedro.estadoSistema())
# print(pablo.estadoSistema())
# print(pablo.estado)
# print(vilma.estadoSistema())
# print(betty.estadoSistema())

# print(pablo.darBaja())
# print(pablo.estado)
# print(pablo.estadoSistema())

# print(pedro.saludar())
# print(pablo.saludar())
# print(vilma.saludar())
# print(betty.saludar())

# print(pedro.darAlta())
# print(pablo.darAlta())
# print(vilma.darAlta())
# print(betty.darAlta())
# print("*******Nuevo Saludo*********")
# print(pedro.saludar())
# print(pablo.saludar())
# print(vilma.saludar())
# print(betty.saludar())
