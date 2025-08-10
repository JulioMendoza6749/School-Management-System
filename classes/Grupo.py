class Grupo():
    def __init__(self):
        self.__IDGrupo = 0
        self.__IDCarrera = 0
        self.__Grupo = ""
        self.__Semestre = 0
        self.__Fecha = ""
        self.__Cupo = 0
        self.__CuposDisponibles = 0

    def set_IDGrupo(self,data):
        self.__IDGrupo = data
    def get_IDGrupo(self):
        return self.__IDGrupo
    
    def set_IDCarrera(self,data):
        self.__IDCarrera = data
    def get_IDCarrera(self):
        return self.__IDCarrera
    
    def set_Grupo(self,data):
        self.__Grupo = data
    def get_Grupo(self):
        return self.__Grupo
    
    def set_Semestre(self,data):
        self.__Semestre = data
    def get_Semestre(self):
        return self.__Semestre
    
    def set_Fecha(self,data):
        self.__Fecha = data
    def get_Fecha(self):
        return self.__Fecha
    
    def set_Cupo(self,data):
        self.__Cupo = data
    def get_Cupo(self):
        return self.__Cupo
    
    def set_CupoDisponibles(self,data):
        self.__CuposDisponibles = data
    def get_CupoDisponibles(self):
        return self.__CuposDisponibles
    
    def __str__(self):
        return self.__Grupo