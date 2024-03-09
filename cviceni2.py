""" from typing import List

class Fronta:
    def __init__(self, pole: List) -> None:
        self._pole = pole

    @property
    def front(self):
        return self._pole[0]

    @property
    def rear(self):
        return self._pole[-1]

    @property
    def isEmpty(self):
        if len(self._pole) == 0:
            return True
        elif len(self._pole) >= 1:
            return False
    @property
    def size(self):
        return len(self._pole)

    @property
    def pole(self):
        return self._pole

    def enqueue(self, value):
        self._pole.append(value)

    def dequeue(self):
        self._pole.pop(0)
    

fronticka = Fronta([1,3,5,6,7])

fronticka.enqueue(5)
fronticka.dequeue()
print(fronticka.pole)
 """

from typing import List
class Zasobnik:
    def __init__(self, pole: List) -> None:
        assert len(pole) >= 1, "Seznam musí mít alespoň jeden prvek!"
        self._pole = pole
    
    def push(self, value):
        self._pole.insert(0, value)
    
    def pop(self):
        self._pole.pop(0)
    
    @property
    def peek(self):
        return self._pole[0]
    
    @property
    def isEmpty(self):
        if len(self._pole) <= 0:
            return True
        elif len(self._pole) >= 1:
            return False
 
    @property    
    def size(self):
        return len(self._pole)
    
    def vyrovnane_zavorky(self):
        for element in self._pole:
            if element in "[]()":
                self.push(element)

zasobnicek = Zasobnik("[[())]]]")

zasobnicek.vyrovnane_zavorky()
