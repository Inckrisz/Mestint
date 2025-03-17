class Hanoi_problema:
    def __init__(self, ke, c):
        self.kezdo = ke
        self.cel = c

    def celteszt(self, allapot):
        return allapot == self.cel

    def rakovetkezo(self,a):
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
                    gyerekek.append(("operator HF", uj_allapot))

        return gyerekek
    def __str__(self):
    return f"Kezdő állapot: {self.kezdo}, Cél állapot: {self.cel}"


if __name__ == "__main__":
    h = Hanoi_problema(("P","P","P"), ("R","R","R"))
