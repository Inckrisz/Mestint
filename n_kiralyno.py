class n_kiralyno_problema:
    def __init__(self, k, c):
        self.kezdő = k
        self.cél = c
        self.N = len(k) - 1

    def célteszt (self, a):
        return a[self.N] == self.cél

    def rákövetkező (self, a):
        gyereke = []
        s = a[self.N]

        for j in range(0, self.N):
            alkalmazhato = True
            for m in range (0, s):
                if a[m] != j and abs(m-s) != abs(a[m]-j):
                    #alkalmazhato = True
                    pass
                else:
                    alkalmazhato = False
                    break

            if alkalmazhato:
                tmp = list(a)
                tmp[s] = j
                tmp[self.N] = s + 1
                uj_allapot = tuple(tmp)
                gyereke.append ((s+" -> "+j, uj_allapot))


        return gyereke




if __name__=="__main__":
    h = n_kiralyno_problema((-1,-1,-1,-1,-1,-1,-1,-1,0), 8)
