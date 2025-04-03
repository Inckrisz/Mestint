from keres import *


class Hanoi_problema(Feladat):
    def __init__(self, ke, c):
        self.kezdő = ke
        self.cél = c

    def célteszt(self, allapot):
        return allapot == self.cél

    def rákövetkező(self,a):
        gyerekek = list()

        for melyiket in range (0,3):
            for hova in ["P","Q","R"]:
                alkalmazhato = True
                if a[melyiket] != hova:
                    for i in range (0, melyiket):
                        if a[i] != a[melyiket] and a[i] != hova:
                            alkalmazhato = True
                        else:
                            alkalmazhato = False
                            break
                else:
                    alkalmazhato = False

                if alkalmazhato:
                    tmp = list(a)
                    tmp[melyiket] = hova
                    uj_allapot = tuple(tmp)
                    gyerekek.append((f"{melyiket+1}->{hova}", uj_allapot))

        return gyerekek
    def __str__(self):
        return f"Kezdő állapot: {self.kezdő}, Cél állapot: {self.cél}"

def heurisztika(csúcs):
    """A helytelen helyen lévő korongok számát adja vissza."""
    jelenlegi = csúcs.állapot
    cél = ("R", "R", "R")  # Minden korong a cél állapotban van
    return sum(1 for i in range(len(jelenlegi)) if jelenlegi[i] != cél[i])



if __name__ == "__main__":
    h = Hanoi_problema(("P","P","P"), ("R","R","R"))
    #csúcs = szélességi_fakereső(h)

    csúcs = best_first(h, heurisztika)
    megoldas = csúcs.út()
    megoldas.reverse() # visszafele kell olvasni a megoldáshoz
    print(megoldas)
    print(csúcs.megoldás())
    # megoldás = csúcs.út()
    # megoldás.reverse()
    # print(megoldás)
