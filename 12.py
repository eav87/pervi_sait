class Trg:
    a = 0
    b = 0
    c = 0
    def __init__(self,a,b,c,):
        self.a = a
        self.b = b
        self.c = c
    def PERIMETR(self):
        return self.a + self.b + self.c
    def plochad(self):
        return self.a * self.b * self.c


asd = Trg(2,3,4)
dsa = Trg(5,7,9)
print(asd.PERIMETR())
for i in (asd,dsa):
    #print(i.__dict__)
    print(i.plochad())

