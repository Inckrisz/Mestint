from keres import *
from keres import best_first
from seged import *


class kancso_feladat(Feladat):
    def __init__(self, ke, c):
        self.kezdő = ke
        self.cél = c
        self.MAX1 = 3
        self.MAX2 = 5
        self.MAX3 = 8

    def célteszt(self, allapot):
        return allapot[0] == self.cél or allapot[1] == self.cél or allapot[2] == self.cél

    def rákövetkező(self, allapot):
        a1, a2, a3 = allapot
        gyerekek = []
        MAXS = [self.MAX1, self.MAX2, self.MAX3]
        i = 0
        while i < 3:
            if allapot[i] == 0:
                i += 1
                continue
            j = 0
            while j < 3:
                if i == j:
                    j += 1
                    continue
                if 0 <= allapot[j] < MAXS[j]:
                    text = f"{i + 1}->{j + 1}"
                    uj_allapot = [a1, a2, a3]
                    T = min(MAXS[j] - allapot[j], allapot[i])
                    uj_allapot[i] = allapot[i] - T
                    uj_allapot[j] = allapot[j] + T
                    gyerekek.append((text, uj_allapot))
                j += 1
            i += 1

        return gyerekek

        # megnézzük melyik kancsot tudjuk tölteni
        # megnézzük melyik kancsot tudjuk üríteni
        # megnézzük hova tudok átönteni

        # a1, a2, a3 = allapot

        # gyerekek = []
        # #tolt 1->2:
        # if a1 != 0 and a2 != self.MAX2:
        #     T= min(a1, self.MAX2 - a2)
        #     uj_allapot = (a1 - T, a2 + T, a3)
        #     gyerekek.append(("1->2", uj_allapot))

        # # tolt 1->3:
        # if a1 != 0 and a3 != self.MAX3:
        #     T = min(a1, self.MAX3 - a3)
        #     uj_allapot = (a1 - T, a2, a3 + T)
        #     gyerekek.append(("1->3", uj_allapot))

        # # tolt 2->1:
        # if a2 != 0 and a1 != self.MAX1:
        #     T = min(a2, self.MAX1 - a1)
        #     uj_allapot = (a1 + T, a2 - T, a3)
        #     gyerekek.append(("2->1", uj_allapot))

        # # tolt 2->3:
        # if a2 != 0 and a3 != self.MAX3:
        #     T = min(a2, self.MAX3 - a3)
        #     uj_allapot = (a1, a2 - T, a3 + T)
        #     gyerekek.append(("2->3", uj_allapot))

        # # tolt 3->1:
        # if a3 != 0 and a1 != self.MAX1:
        #     T = min(a3, self.MAX1 - a1)
        #     uj_allapot = (a1 + T, a2, a3 - T)
        #     gyerekek.append(("3->1", uj_allapot))

        # # tolt 3->2:
        # if a3 != 0 and a2 != self.MAX2:
        #     T = min(a3, self.MAX2 - a2)
        #     uj_allapot = (a1, a2 + T, a3 - T)
        #     gyerekek.append(("3->2", uj_allapot))
        # return gyerekek

def heurisztika(csúcs):
    a = csúcs.állapot
    return min([abs(a[0]-4), abs(a[1]-4), abs(a[2]-4)])


if __name__ == "__main__":
    kancso = kancso_feladat((0, 0, 8), 4)
    #print(kancso.rákövetkező((0, 5, 3)))

    #csúcs = szélességi_fakeresés(kancso)
    csúcs = best_first(kancso, heurisztika)
    megoldas = csúcs.út()
    megoldas.reverse() # visszafele kell olvasni a megoldáshoz
    print(megoldas)
    print(csúcs.megoldás())
