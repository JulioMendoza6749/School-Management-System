class Materia():
    def __init__(self):
        self.__IDMateria = 0
        self.__Asignatura = ""
        self.__Creditos = 0
    
    def set_IDMateria(self, data):
        self.__IDMateria = data
    def get_IDMateria(self):
        return self.__IDMateria
    
    def set_Asignatura(self, data):
        self.__Asignatura = data
    def get_Asignatura(self):
        return self.__Asignatura
    
    def set_Creditos(self, data):
        self.__Creditos = data
    def get_Creditos(self):
        return self.__Creditos
    
    def get_ID(self):
        return self.__IDMateria

    def __str__(self):
        return self.__Asignatura