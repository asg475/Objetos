'''Obejetos  Empleado'''
import random

class Empleado:
    id_previa = 1

    def __init__(self,name, surname):
        
        self.id =  Empleado.id_previa
        self.name = name
        self.surname = False
        self.email = name +"."+ surname + "@email.com"
        self.pay = random.randint(1500, 2200)

        Empleado.id_previa +=  1
        
sergio = Empleado("sergio", "pesquera")
print(sergio.id)
print(sergio.name)
print(sergio.surname)
print(sergio.email)
print(sergio.pay)
