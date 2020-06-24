# Permiso{ codigo, conductor, modelo, marca, placa, ciudad, fecha_solicitud, motivo, habilitado}
from datetime import datetime
class Permiso:
    def __init__(self):
        self.codigo=[]
        self.conductor=[]
        self.modelo=[]
        self.marca=[]
        self.placa=[]
        self.ciudad=[]
        self.fecha_solicitud = []
        self.motivo=[]
        self.habilitado = []
    
    def menu(self):
        print("""
        SISTEMA DE PERMISOS UPCTIC
        1.- Mostrar todos los permisos solicitados
        2.-Habilitar permisos realizados hasta el mes de Mayo
        3.-Mostrar permisos habilitados
        4.-Mostrar permisos no-habilitados
        """)
        seleccion = int(input("Seleccione una opcion: \n"))
        if seleccion == 1 :
            self.mostrarLista()
            self.menu()
        elif seleccion == 2 :
            self.habilitarPermiso()
            self.menu()
        elif seleccion == 3 :
            self.mostrarListaHabilitacion(1)
            self.menu()
        elif seleccion == 4 :
            self.mostrarListaHabilitacion(0)
            self.menu()
        elif seleccion == 5:
            print("Gracias por utilizar el sistema")
        else:
            print("Elija una opcion valida")
            self.menu()
        pass
    def guardar(self,  codigo, conductor, modelo, marca, placa, ciudad, fecha_solicitud, motivo, habilitado):   
        self.codigo.append(codigo)
        self.conductor.append(conductor)
        self.modelo.append(modelo)
        self.marca.append(marca)
        self.placa.append(placa)
        self.ciudad.append(ciudad)
        self.fecha_solicitud.append(fecha_solicitud) 
        self.motivo.append(motivo)
        self.habilitado.append(habilitado) 


    def mostrarLista(self):
        for i in range(len(self.codigo)):
            self.detalle(i)
        pass
    def detalle(self, posicion):
        print("***PERMISO NRO: {} ****".format(self.codigo[posicion]))
        print("CONDUCTOR: {}".format(self.conductor[posicion]))
        print("MODELO: {}".format(self.modelo[posicion]))
        print("MARCA: {}".format(self.marca[posicion]))
        print("PLACA: {}".format(self.placa[posicion]))
        print("CIUDAD: {}".format(self.ciudad[posicion]))
        print("FECHA DE SOLICITUD: {}".format(self.fecha_solicitud[posicion]))
        print("MOTIVO: {}".format(self.motivo[posicion]))
        print("HABILITADO: {}".format(self.habilitado[posicion]))
        print("-----------------------------------")
        pass
    def habilitarPermiso(self):
        fecha_l=input("Digite la fecha limite: ej:d/m/a \n")
        fecha_limite = datetime.strptime(fecha_l, "%d/%m/%Y")
        for i in range(len(self.codigo)):
            fecha = datetime.strptime(self.fecha_solicitud[i], "%d/%m/%Y")
            if fecha <= fecha_limite:
                self.habilitado[i]=1
        self.mostrarListaHabilitacion(1)
        pass
    def mostrarListaHabilitacion(self, valor):
        if valor: 
            print("*****LISTA DE PERMISOS HABILITADOS*****")
        else:
            print("*****LISTA DE PERMISOS NO HABILITADOS*****")
        for i in range(len(self.codigo)):
            if self.habilitado[i] == valor:
                self.detalle(i)
        pass 



permisos = Permiso()
permisos.guardar(1, 'JOSE MERCADO', 'COROLLA', 'TOYOTA', '2504TDA', 'SANTA CRUZ', '15/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(2, 'ALBERTO MERCADO', 'HILUX', 'TOYOTA', '2640SDA', 'TARIJA', '12/04/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(3, 'GABRIEL MELGAR', 'SENTRA', 'NISSAN', '3204NTS', 'BENI', '30/05/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(4, 'CARLA MEDINA', 'LANCER', 'MITSUBISHI', '2207SBA', 'CHUQUISACA', '02/05/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(5, 'PABLO AGUILAR', 'ACCORD', 'HONDA', '3504ATD', 'COCHABAMBA', '09/04/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(6, 'CARLOS MONTERO', 'CIVIC', 'HONDA', '2804STA', 'SANTA CRUZ', '10/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)
permisos.guardar(7, 'PABLO ALEMAN', 'YARIS', 'TOYOTA', '2054PDA', 'LA PAZ', '22/06/2020', 'PERMISO PARA IR AL TRABAJO', 0)

permisos.menu()