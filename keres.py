import sys
from seged import *


class Feladat:

    def __init__(self, kezdő, cél=None):
        self.kezdő = kezdő;
        self.cél = cél

    def rákövetkező(self, állapot):
        raise NotImplementedError

    def érték(self):
        raise NotImplementedError

    def célteszt(self, állapot):
       #return állapot == self.cél
       raise NotImplementedError

    def útköltség(self, c, állapot1, lépés, állapot2):
        return c + 1


class Csúcs:

    def __init__(self, állapot, szülő=None, lépés=None, útköltség=0):
        self.állapot = állapot
        self.szülő = szülő
        self.lépés = lépés
        self.útköltség = útköltség
        if szülő:
            self.mélység = szülő.mélység + 1
        else:
            self.mélység = 0

    def __repr__(self):
        return "<Csúcs: %s>" % (self.állapot, )

        #return "%s" % (list(self.állapot),)

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
            if következő not in [csúcs.állapot for csúcs in self.út()]:
                yield Csúcs(következő, self, művelet,
                            feladat.útköltség(self.útköltség, self.állapot, művelet,
                                              következő))



def fakereső(feladat, perem):
    perem.append(Csúcs(feladat.kezdő))
    while perem:
        csúcs = perem.pop()
        if feladat.célteszt(csúcs.állapot):
            return csúcs
        else:
            perem.extend(csúcs.kiterjeszt(feladat)) # ha nem cél állapot belerakjuk a perembe a gyermekeit a csúcsnak

    return None # nincs megoldás

def szélességi_fakereső (feladat, perem):
    




