class Horario():
    def __init__(self):
        self.__IDHorario = 0
        self.__IDCarrera = 0
        self.__IDMateria = 0
        self.__IDMaestro = 0
        self.__IDSalon = 0
        self.__Dias = ""
        self.__Horas = ""
        self.__Disponibilidad = 0

    def set_IDHorario(self,data):
        self.__IDHorario = data
    def get_IDHorario(self):
        return self.__IDHorario
    
    def set_IDCarrera(self,data):
        self.__IDCarrera = data
    def get_IDCarrera(self):
        return self.__IDCarrera
    
    def set_IDMateria(self,data):
        self.__IDMateria = data
    def get_IDMateria(self):
        return self.__IDMateria
    
    def set_IDMaestro(self,data):
        self.__IDMaestro = data
    def get_IDMaestro(self):
        return self.__IDMaestro
    
    def set_IDSalon(self,data):
        self.__IDSalon = data
    def get_IDSalon(self):
        return self.__IDSalon
    
    def set_Dias(self,data):
        self.__Dias = data
    def get_Dias(self):
        return self.__Dias
    
    def set_Horas(self,data):
        self.__Horas = data
    def get_Horas(self):
        return self.__Horas
    
    def set_Disponibilidad(self,data):
        self.__Disponibilidad = data
    def get_Disponibilidad(self):
        return self.__Disponibilidad
    
    def __str__(self):
        return self.__IDHorario