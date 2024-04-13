import re
import logging

logging.basicConfig(level = logging.INFO)

class EmailValidator: 
    def __set__(self, instance, value):
        if re.match("^[^\s@]+@wsei.edu.pl$", value):
            instance.__dict__['email'] = value
            #return self
            logging.info("Correct email")
        else:
            raise ValueError("Invalid Email")


class Student: 
    email = EmailValidator() 

    def __init__(self, imie, nazwisko, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email


Student("Jan", "Kowalski", 'jan.kowalski@wsei.edu.pl')