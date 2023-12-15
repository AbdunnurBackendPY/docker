class Figure:
    def __init__(self,x):
        self.x = []
        for k in x:
            self.x.append(int(k))


    def perim(self, edges):
        pass



class Triangle(Figure):
    def p(self):
        pass

    def Squared(self):
        p = 0
        for k in x:
            p +=int(k)
        p = p/2
        s= p*(p - float(x[0]))*(p -float(x[1]))*(p - float(x[2]))
        print(s**0.5)





class Tetragon(Figure):
    pass
class Square(Tetragon):
    def squared(self):
        P = sum(self.x) / 2
        a = int(self.x[0])

        squared = a ** 2
        return squared
class Rectangle(Tetragon):
    def squared(self):
        a = int(self.x[0])
        b = int(self.x[1])
        S = a * b
        return S


x = input("Введите сторон").split()
if len(x) == 1:
    fig = Square(x)

elif len(x) == 2:
    fig = Rectangle(x)
elif len(x) == 3:
    fig = Triangle(x)
print(fig.squared())