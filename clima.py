class Clima:
    def __init__(self):
        self.codigo = []
        self.ciudad = []
        self.temp_minima = []
        self.temp_maxima = []
        self.zona = []

    def menu(self):
        opciones = """
            SISTEMA DE GESTION DE CLIMA
            1.- PROMEDIO DE LA TEMP. MIN. DE LA ZONA VALLE
            2.- TEMP. MIN. DE LA ZONA DEL LLANO
            3.- TEMP. MAX. DE LA ZONA DEL ALTIPLANO
            4.- SALIR
        """
        print(opciones)
        eleccion = int(input("Seleccion una opcion: \n"))
        if (eleccion == 1):
            print(self.mostrarTempPromedioMin())
            self.menu()
        elif(eleccion == 2):
            print(self.mostrarTempExtrema())
            self.menu()
        elif (eleccion == 3):
            print(self.mostrarTempExtrema())
            self.menu()
        elif (eleccion == 4):
            print("**Sistema de Gestión del Clima v1.0.1**")
        else:
            print("Elija correctamente una opcion del menu")
            self.menu()
    def guardar(self, cod, ciudad, tmin, tmax, zona):
        self.codigo.append(cod)
        self.ciudad.append(ciudad)
        self.temp_minima.append(tmin)
        self.temp_maxima.append(tmax)
        self.zona.append(zona)
        return "Ciudad {} registrada correctamente".format(ciudad)
    def tempPromedioMinValle(self):
        sumaMin=0
        contador=0
        for i in range(len(self.ciudad)):
            if (self.zona[i]=='Valle'):
                sumaMin = sumaMin + self.temp_minima[i]
                contador = contador + 1
        promedioTM= sumaMin / contador
        print("La temperatura promedio es: {} grados".format(int(promedioTM)))
    def tempPromedioMin(self, p_zona):
        l_tempMin = []
        for i in range(len(self.ciudad)):
            if (self.zona[i]== p_zona):
                l_tempMin.append(self.temp_minima[i])
        promedio = round(sum(l_tempMin) / len(l_tempMin), 2)

        return promedio

    def mostrarTempPromedioMin(self):
        # zona = input("Elija una zona: \n")
        zona = "Valle"
        return print("La temperatura promedio Minima de la zona del {} es {} Centigrados".format(zona, self.tempPromedioMin(zona)))

    def descripcion(self, posicion):
        print("Ciudad {}".format(self.ciudad[posicion]))
        print("Min: {} Centigrados".format(self.temp_minima[posicion]))
        print("Max: {} Centigrados".format(self.temp_maxima[posicion]))
        print("Zona: {} de Bolivia".format(self.zona[posicion]))
        print("*********************************************")
        pass

    def tempMasBaja(self, p_zona):
        temperaturaBaja = 100
        posicion = 0
        for i in range(len(self.ciudad)):
            if (self.zona[i] == p_zona):
                t_min = self.temp_minima[i]
                if (t_min < temperaturaBaja):
                    temperaturaBaja = t_min
                    posicion = i
        return posicion



    def tempMasAlta(self, p_zona):
        temperaturaAlta = -100
        posicion = 0
        for i in range(len(self.ciudad)):
            if (self.zona[i] == p_zona):
                t_max = self.temp_minima[i]
                if (t_max > temperaturaAlta):
                    temperaturaAlta = t_max
                    posicion = i
        return posicion

    def mostrarTempExtrema(self):
        posicionEncontrada = False
        zona = input("Elija una zona: \n")
        if (zona == 'Altiplano' or zona == 'Valle' or zona == 'Llano'):
            tipo = input("Seleccione el tipo de clima: Alta/Baja \n")
            if (tipo == 'Alta' or tipo == 'alta' or tipo == 'ALTA'):
                posicion = self.tempMasAlta(zona)
                posicionEncontrada = True
            elif(tipo == 'Baja' or tipo == 'baja' or tipo == 'BAJA'):
                posicion = self.tempMasBaja(zona)
                posicionEncontrada = True
            else:
                print("Seleccione una opcion valida")
                self.mostrarTempExtrema()

            if(posicionEncontrada == True):
                print("***La ciudad con la temperatura mas {} de la zona del {} es:***".format(tipo, zona))
                self.descripcion(posicion)
        else:
            print("Dgite correctamente la Zona.!!")
            self.mostrarTempExtrema()
        pass




clima = Clima()

clima.guardar(1, "SANTA CRUZ", 15, 29, "Llano")

clima.guardar(2, "BENI", 17, 31,"Llano")

clima.guardar(3, "PANDO", 18, 30,"Llano")

clima.guardar(4, "LA PAZ", 1, 13,"Altiplano")

clima.guardar(5, "ORURO", 2, 15,"Altiplano")

clima.guardar(6, "POTOSI", 2, 14,"Altiplano")

clima.guardar(7, "CBBA", 5, 18, "Valle")

clima.guardar(8, "SUCRE", 9, 23, "Valle")

clima.guardar(9, "TARIJA", 10, 25, "Valle")

clima.menu()


