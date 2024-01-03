'''slajd10'''

class Child:

    def __init__(self) -> None:
        self.print = self._print1

    def _print1(self):
        print('1')
        
    def _print2(self):
        print('2')

    def _print3(self):
        print('3')

    def _print4(self):
        print('4')

    @property
    def state(self):
        if self.print == self._print1:
            return 1
        elif self.print == self._print2:
            return 2
        elif self.print == self._print3:
            return 3
        else:
            return 4

    @state.setter
    def state(self,state):
        if state == 1:
            self.print = self._print1
        elif state == 2:
            self.print = self._print2
        elif state == 3:
            self.print = self._print3
        elif state == 4:
            self.print = self._print4

a = Child()
a.state = 2
a.print()