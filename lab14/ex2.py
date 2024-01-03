'''slajd9 na 2 prezentacji'''

class Observer:
    def update(self,x):
        print(x)


class Student:
    def __init__(self) -> None:
        self._ects = 0
        self._notes = {}
        self.observers = []

    def notify_observers(self,ects):
        for observers in self.observers:
            observers.update(ects)
    
    @property
    def ects(self):
        return self._ects

    @ects.setter
    def ects(self,number):
        self._ects = number
        self.notify_observers(number)
