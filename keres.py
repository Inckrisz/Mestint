import sys
from seged import *


class Feladat:

    def __init__(self, kezdő, cél=None):
        self.kezdő = tuple(kezdő)  # Lista helyett tuple
        self.cél = tuple(cél) if cél else None

    def rákövetkező(self, állapot):
        raise NotImplementedError

    def érték(self):
        raise NotImplementedError

    def célteszt(self, állapot):
        return állapot == self.cél

    def útköltség(self, c, állapot1, lépés, állapot2):
        return c + 1


class Csúcs:

    def __init__(self, állapot, szülő=None, lépés=None, útköltség=0):
        self.állapot = tuple(állapot)  # Lista helyett tuple
        self.szülő = szülő
        self.lépés = lépés
        self.útköltség = útköltség
        if szülő:
            self.mélység = szülő.mélység + 1
        else:
            self.mélység = 0

    def __repr__(self):
        return "<Csúcs: %s>" % (self.állapot, )

    def út(self):
        x, válasz = self, [self]
        while x.szülő:
            válasz.append(x.szülő)
            x = x.szülő
        return válasz

    def megoldás(self):
        utam = self.út()
        utam.reverse()
        return [csúcs.lépés for csúcs in utam[1:]]

    def kiterjeszt(self, feladat):
        for (művelet, következő) in feladat.rákövetkező(self.állapot):
            if tuple(következő) not in [csúcs.állapot for csúcs in self.út()]:
                yield Csúcs(tuple(következő), self, művelet,
                            feladat.útköltség(self.útköltség, self.állapot, művelet,
                                              következő))


def fakereső(feladat, perem):
    perem.append((Csúcs(feladat.kezdő)))
    while perem:
        csúcs = perem.pop()
        if feladat.célteszt(csúcs.állapot):
            return csúcs
        else:
            perem.extend(csúcs.kiterjeszt(feladat))
            
    return None


def gráfkereső(feladat, perem):
    perem.append((Csúcs(feladat.kezdő)))
    kifejtési_sor = set()
    while perem:
        csúcs = perem.pop()
        if feladat.célteszt(csúcs.állapot):
            return csúcs

        if csúcs.állapot not in kifejtési_sor:
            kifejtési_sor.add(csúcs.állapot)
            perem.extend(csúcs.kiterjeszt(feladat))

    return None


def szélességi_gráfkereső(feladat):
    return gráfkereső(feladat, Sor())


def mélységi_gráfkereső(feladat):
    return gráfkereső(feladat, Verem())


def szélességi_fakereső(feladat):
    return fakereső(feladat, Sor())


def mélységi_fakereső(feladat):
    return fakereső(feladat, Verem())


def best_first(feladat, h):
    return gráfkereső(feladat, RendezettLista(h))


def a_csillag(feladat, h):
    def f(n):
        return n.útköltség + h(n)

    return best_first(feladat, f)
