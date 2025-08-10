class Edificio():
    def __init__(self):
        self.__IDEdificio = 0
        self.__Edificio = ""

    def set_IDEdificio(self,data):
        self.__IDEdificio = data
    def get_IDEdificio(self):
        return self.__IDEdificio
    
    def set_Edificio(self,data):
        self.__Edificio = data
    def get_Edificio(self):
        return self.__Edificio
    
    def __str__(self):
        return self.__Edificio