
class Cliente:
    def __init__(self,nome):
        self.__nome = nome


    @property #propriedade
    def nome(self):
        print("--------------Proprety------------ Nome CP3")
        return self.__nome.title()

    @nome.setter
    def nome(self,nome):
        self.__nome = nome