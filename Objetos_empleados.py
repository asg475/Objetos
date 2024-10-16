'''Obejetos  Empleado'''
import random


class Empleado:
    id_previa = 1

    def __init__(self, name, surname):
        
        self.id = Empleado.id_previa
        self.name = name
        self.surname = surname
        self.email = f"{name}.{surname}@email.com"
        self.pay = random.randint(1500, 2200)

        Empleado.id_previa += 1

    def pay_raise(self):
        """ Esta funcion proporciona un aumento del 15%
        a un elemento construido con la clase Empleado.

        Returns:
            El string: aumento realizado
        """
        self.pay = int( self.pay * 1.15)
        return "aumento realizado"

    def __str__(self):
        """Esta funcion devuelve un string al hacer un print
        de un elemento creado con la clase Empleado

        Returns:
            string:con el nombre del empleado y su sueldo
        """
        return f"El empleado {self.name} cobra {self.pay}"
    
    def __add__(self, otro):
        """Suma el sueldo de dos empleados

        Args:
            otro (Empleado): el segundo empleado con el que se quiere sumar el sueldo

        Returns:
            string: Dice la cuanto combran ambos empleados juntos
        """
        return f"Juntos combran {self.pay + otro.pay}"
    
    @classmethod
    def from_string(cls, cadena: str):
        """permite crear un empleado cuando todos los datos se 
        encuentran en un unico string

        Args:
            cadena (str): string que contien el nombre y el apellido separado por una coma

        Returns:
            Empleado: devuelve directamente un elemento con todos los atributos de Empleado
        """
        name, surname = cadena.split(", ")
        return cls(name, surname)


class CEO(Empleado):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.empleados_a_cargo = []
    
    def add_employee(self, empleado):
        """Añade a la lista de empleados_a_cargo
        propia de cada CEO un nuevo empleado

        Args:
            empleado (Empleado)
        """
        if isinstance(empleado, Empleado):
            self.empleados_a_cargo.append(empleado)
            print(f"{empleado.name} {empleado.surname} ha sido añadido a la lista de empleados a cargo.")

    def remove_employee(self, empleado):
        """Elimina de la lista de empleados_a_cargo
        propia de cada CEO  empleado

        Args:
            empleado (Empleado)
        """
        if empleado in self.empleados_a_cargo:
            self.empleados_a_cargo.remove(empleado)
            print(f"{empleado.name} {empleado.surname} ha sido eliminado de la lista de empleados a cargo.")
        else:
            print(f"{empleado.name} {empleado.surname} no está en la lista de empleados a cargo.")

    def listar_empleados(self):
        """Devuelve por pantalla los empleado que tiene a su cargo cada CEO
        """
        if not self.empleados_a_cargo:
            print("No hay empleados a cargo.")
        else:
            print("Empleados a cargo:")
            for emp in self.empleados_a_cargo:
                print(f"- {emp.name} {emp.surname}, Sueldo: {emp.pay}")




sergio = Empleado("sergio", "pesquera")
print(sergio.id)
print(sergio.name)
print(sergio.surname)
print(sergio.email)
print(sergio.pay)
miguel = Empleado("miguel", "Betegon")
print(miguel.id)
print(miguel.surname)
sergio.pay_raise()
print(sergio.pay)
print(sergio)
print(sergio + miguel)
a = "jaled, moustafa"
jaled = Empleado.from_string(a)
print(jaled)

ceo1 = CEO("jaled", "moustafa")
ceo2 = CEO("sergio", "pesquera")
print(ceo1)
ceo1.add_employee(miguel)
ceo1.listar_empleados()
ceo1.remove_employee(miguel)
ceo1.listar_empleados()