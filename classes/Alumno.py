class Alumno():
    def __init__(self):
        self.__IDAlumno = 0
        self.__Nombre = ""
        self.__Paterno = ""
        self.__Materno = ""
        self.__FechaNacimiento = ""
        self.__Username = ""
        self.__Password = ""
        self.__IDCarrera = 0
        self.__IDGrupo = 0
    
    def set_IDAlumno(self, data):
        self.__IDAlumno = data
    def get_IDAlumno(self):
        return self.__IDAlumno
    
    def set_Nombre(self, data):
        self.__Nombre = data
    def get_Nombre(self):
        return self.__Nombre
    
    def set_Paterno(self, data):
        self.__Paterno = data
    def get_Paterno(self):
        return self.__Paterno
    
    def set_Materno(self, data):
        self.__Materno = data
    def get_Materno(self):
        return self.__Materno
    
    def set_FechaNacimiento(self, data):
        self.__FechaNacimiento = data
    def get_FechaNacimiento(self):
        return self.__FechaNacimiento
    
    def set_Username(self, data):
        self.__Username = data
    def get_Username(self):
        return self.__Username
    
    def set_Password(self, data):
        self.__Password = data
    def get_Password(self):
        return self.__Password
    
    def set_IDCarrera(self, data):
        self.__IDCarrera = data
    def get_IDCarrera(self):
        return self.__IDCarrera
    
    def set_IDGrupo(self, data):
        self.__IDGrupo = data
    def get_IDGrupo(self):
        return self.__IDGrupo
    
    def toString(self):
        result = self.__Paterno + " " +self.__Materno + " " + self.__Nombre
        return result