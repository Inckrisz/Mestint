class n_kiralyno_problema:
    def __init__(self, k, c):
        self.kezdo = k
        self.cel = c
        self.N = len(k) - 1

    def celteszt (self, a):
        return a[self.N] == self.cel

    def rakovetkezo (self, a):
        gyerekek = []
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
                gyerekek.append ((s+" -> "+j, uj_allapot))
                

        return gyerekek 




if __name__=="__main__":
    h = n_kiralyno_problema((-1,-1,-1,-1,-1,-1,-1,-1,0), 8)
