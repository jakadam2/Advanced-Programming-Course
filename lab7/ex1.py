"""Esercizio su metodi statici e di classe"""
class Employee:

    nr_of_instances = 0

    def __init__(self) -> None:
        Employee.nr_of_instances += 1

    @classmethod
    def print_instances(cls):
        print(cls.nr_of_instances)


class Technition(Employee):

    nr_of_instances = 0

    def __init__(self) -> None:
        Technition.nr_of_instances += 1
        super().__init__()
        

class Admin(Employee):

    nr_of_instances = 0

    def __init__(self) -> None:
        Admin.nr_of_instances += 1
        super().__init__()


a = Admin()
b = Admin()
c = Technition()
d = Technition()
e = Employee()
Admin.print_instances()
Technition.print_instances()
Employee.print_instances()
#DZIALA !!!