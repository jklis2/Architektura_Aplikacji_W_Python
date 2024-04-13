class LoggingDescriptor:
    def __init__(self, name=None):
        self.name = name
        self.value = None

    def __get__(self, obj, objtype):
        if obj is not None:
            print(f"Dostęp do odczytu {self.name}, wartość = {self.value}")
        return self.value

    def __set__(self, obj, value):
        print(f"Dostęp do zapisu {self.name}, nowa wartość = {value}")
        self.value = value

class Uzytkownik:
    imie = LoggingDescriptor('imie')
    wiek = LoggingDescriptor('wiek')
    
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
