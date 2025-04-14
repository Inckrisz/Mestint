from keres import *


class n_kiralyno_problema(Feladat):
    def __init__(self,k,c):
        self.kezdő = k
        self.cél  = c
        self.N = len(k) -1

    def célteszt(self,a):
        return a[self.N]  == self.cél

    def rákövetkező(self,a):
        gyereke = []
        s= a[self.N]

        for j in range(0,self.N):
            alkalmazhato = True
            for m in range(0,s):
                if a[m] != j and abs(m-s) != abs(a[m]-j):
                    #alkalmazhato = True
                    pass
                else:
                    alkalmazhato = False
                    break

            if alkalmazhato:
                tmp = list(a)
                tmp[s] = j
                tmp[self.N] = s+1
                uj_allapot = tuple(tmp)
                gyereke.append((str(s)+" -> "+str(j),uj_allapot))

        return gyereke


def heurisztika(csúcs):
    """A támadásban lévő királynők számát adja vissza."""
    állapot = csúcs.állapot[:-1]  # Az utolsó érték az elhelyezett királynők száma, nem kell
    N = len(állapot)
    ütközések = 0

    for i in range(N):
        for j in range(i + 1, N):
            if állapot[i] == állapot[j] or abs(állapot[i] - állapot[j]) == abs(i - j):
                ütközések += 1

    return ütközések


if __name__ == "__main__":
    h = n_kiralyno_problema((-1,-1,-1,-1,-1,-1,-1,-1,0),8)

    csúcs = best_first(h, heurisztika)
    megoldas = csúcs.út()
    megoldas.reverse() # visszafele kell olvasni a megoldáshoz
    print(megoldas)
    print(csúcs.megoldás())
    # csucs = szélességi_fakeresés(h)

    # megoldas = csucs.út()
    # megoldas.reverse()

    # print(megoldas)
