class Cliente():
    def __init__(self):
        self.__Nombre = ""
        self.__APaterno = ""
        self.__AMaterno = ""
        self.__Username = ""
        self.__Password = ""
        self.__Perfil = ""
    
    def set_Nombre(self, data):
        self.__Nombre = data
    def get_Nombre(self):
        return self.__Nombre
    
    def set_APaterno(self, data):
        self.__APaterno = data
    def get_APaterno(self):
        return self.__APaterno
    
    def set_AMaterno(self, data):
        self.__AMaterno = data
    def get_AMaterno(self):
        return self.__AMaterno
    
    def set_Username(self, data):
        self.__Username = data
    def get_Username(self):
        return self.__Username
    
    def set_Password(self, data):
        self.__Password = data
    def get_Password(self):
        return self.__Password
    
    def set_Perfil(self,data):
        self.__Perfil = data
    def get_Perfil(self):
        return self.__Perfil