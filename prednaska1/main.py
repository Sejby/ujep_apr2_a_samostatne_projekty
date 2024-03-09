from random import choice,random
from math import isclose

def cumsum(xs: list) -> None:
    suma = xs[0]
    for i in range(1, len(xs)):
        suma += xs[i]
        xs[i] = suma


def random_choice(items: list, probabilities: list):
    assert len(items) == len(probabilities), "Délka seznamů je jiná"
    sumarum = sum(probabilities)
    for idx in range(len(probabilities)):
        probabilities[idx] /= sumarum
    assert isclose(sum(probabilities), 1.0)
    cumsum(probabilities)
    probabilities[-1] = 1.0
    r = random()
    for i in range(len(probabilities)):
        if r<= probabilities[i]:
            return items[i]

if __name__ == "__main__": #je to spuštěno jako hlavní modul
    test = ["Frodo", "Gandalf", "Honza"]
    print(random_choice(test, [0.5, 0.3, 0.2]))

    test2 = list(range(1,7))
    print(random_choice(test2, [0.6/4, 0.6/4, 0.6/4, 0.6/4,0.2,0.2]))


