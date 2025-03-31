from keres import *
class Hanoi_problema(Feladat):
    def __init__(self,ke, c ):
        self.kezdő = ke
        self.cél = c

    def célteszt(self, allapot):
        return allapot == self.cél

    def rákövetkező(self,a):
        gyerekek = list()

        for melyiket in range(0,3):
            for hova in ['P','Q','R']:
                alkalmazható = True
                if a[melyiket] != hova:
                    for i in range(0,melyiket):
                        if a[i] != a[melyiket] and a[i] != hova:
                            alkalmazható =True
                        else:
                            alkalmazható = False
                            break

                else:
                    alkalmazható = False

                if alkalmazható:
                    tmp = list(a)
                    tmp[melyiket] = hova
                    uj_allapot = tuple(tmp)
                    gyerekek.append(("operator HF", uj_allapot))

        return gyerekek








if __name__ == "__main__":
    h = Hanoi_problema(('P','P','P'), ('R','R','R'))
    csúcs = szélességi_fakeresés(h)
    ut = csúcs.út()
    ut.reverse()
    print(ut)
