import bisect
import random
import functools
import heapq
from collections import deque


class Várólista:
    def __init__(self):
        pass

    def extend(self, elemek):
        for elem in elemek: self.append(elem)


def Verem():
    return []


class Sor(Várólista):
    def __init__(self):
        self.A = [];
        self.kezd = 0

    def append(self, elem):
        self.A.append(elem)

    def __len__(self):
        return len(self.A) - self.kezd

    def extend(self, elemek):
        self.A.extend(elemek)

    # class Sor(Várólista):
    #     def __init__(self):
    #         self.heap = []
    #         self.counter = 0

    #     def append(self, elem):
    #         heapq.heappush(self.heap, (self.counter, elem))
    #         self.counter += 1

    #     def __len__(self):
    #         return len(self.heap)

    #     def pop(self):
    #         if not self.heap:
    #             raise IndexError("A sor üres!")
    #         return heapq.heappop(self.heap)[1]

    def pop(self):
        # e = self.A[self.kezd]
        # self.kezd += 1
        # if self.kezd > 5 and self.kezd > len(self.A)/2:
        #     self.A = self.A[self.kezd:]
        #     self.kezd = 0
        # return e

        e = self.A[0]
        self.A = self.A[1:]  # Minden hívásnál levágjuk az első elemet
        return e


class RLElem:
    def __init__(self, érték, elem):
        self.értékem = érték
        self.elemem = elem

    def __lt__(self, másik):
        return self.értékem < másik.értékem

    def érték(self):
        return self.értékem

    def elem(self):
        return self.elemem


class RendezettLista(Várólista):
    def __init__(self, f):
        self.A = []
        self.f = f

    def append(self, elem):
        pár = RLElem(self.f(elem), elem)
        bisect.insort(self.A, pár)

    def __len__(self):
        return len(self.A)

    def pop(self):
        return self.A.pop(0).elem()


def argmin(lista, fv):
    legjobb = lista[0];
    legjobb_érték = fv(legjobb)
    for x in lista[1:]:
        x_érték = fv(x)
        if x_érték < legjobb_érték:
            legjobb, legjobb_érték = x, x_érték
    return legjobb
