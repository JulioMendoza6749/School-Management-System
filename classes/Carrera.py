class Carrera():
    def __init__(self):
        self.__CarreraID = 0
        self.__Clave = ""
        self.__Carrera = ""
        self.__Semestres = 0

    def set_CarreraID(self,data):
        self.__CarreraID = data
    def get_CarreraID(self):
        return self.__CarreraID
    
    def set_Clave(self,data):
        self.__Clave = data
    def get_Clave(self):
        return self.__Clave
    
    def set_Carrera(self,data):
        self.__Carrera = data
    def get_Carrera(self):
        return self.__Carrera
    
    def set_Semestres(self,data):
        self.__Semestres = data
    def get_Semestres(self):
        return self.__Semestres
    
    def get_ID(self):
        return self.__CarreraID
    
    def __str__(self):
        return self.__Clave