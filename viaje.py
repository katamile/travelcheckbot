class Viaje:
    def __init__(self, aerolinea, origen, destino, duracion,precio,fecha1,fecha2,npersona,cod):
        self.__aerolinea = aerolinea
        self.__origen = origen
        self.__destino = destino
        self.__duracion = duracion
        self.__fecha1= fecha1
        self.__fecha2=fecha2
        self.__npersona=npersona
        self.__precio=precio
        self.__cod=cod


# /get
    @property
    def aerolinea(self):
        return self.__aerolinea
# /set
    @aerolinea.setter
    def aerolinea(self, valor):
        self.__aerolinea = valor


# /get
    @property
    def origen(self):
        return self.__origen
# /set
    @origen.setter
    def origen(self, valor):
        self.__origen = valor


# /get
    @property
    def destino(self):
        return self.__destino
# /set
    @destino.setter
    def destino(self, valor):
        self.__destino= valor


# /get
    @property
    def duracion(self):
        return self.__duracion
# /set
    @duracion.setter
    def duracion(self, valor):
        self.__duracion = valor

    @property
    def fecha1(self):
        return self.__fecha1

    # /set
    @fecha1.setter
    def fecha1(self, valor):
        self.__fecha1 = valor

    @property
    def fecha2(self):
        return self.__fecha2

    # /set
    @fecha2.setter
    def fecha2(self, valor):
        self.__fecha2 = valor

    @property
    def precio(self):
        return self.__precio
     # /set
    @precio.setter
    def precio(self, valor):
        self.__precio = valor

        # /get

    @property
    def npersona(self):
        return self.__npersona

    # /set
    @npersona.setter
    def npersona(self, valor):
        self.__npersona = valor

    # /get
    @property
    def cod(self):
            return self.__cod

    # /set
    @cod.setter
    def cod(self, valor):
            self.__cod = valor

    #/def __str__(self):
       #/ cadena=
     #/   return cadena

   # def __str__(self) :
    #    return self.__aerolinea,self.__origen,self.__destino,self.__duracion,self.__escala,self.__clase,self.__precio



