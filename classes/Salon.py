class Salon():
    def __init__(self):
        self.__IDSalon = 0
        self.__IDEdificio = 0
        self.__Nombre = ""

    def set_IDSalon(self,data):
        self.__IDSalon = data
    def get_IDSalon(self):
        return self.__IDSalon
    
    def set_IDEdificio(self,data):
        self.__IDEdificio = data
    def get_IDEdificio(self):
        return self.__IDEdificio
    
    def set_Nombre(self,data):
        self.__Nombre = data
    def get_Nombre(self):
        return self.__Nombre
    
    def get_ID(self):
        return self.__IDSalon
    
    def __str__(self):
        return self.__Nombre