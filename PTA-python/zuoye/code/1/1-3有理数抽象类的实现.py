"""
类型名称：Rational
数据对象集：一个有理数，a/b
操作集：对于任意有理数x Rational，以及自然数a和b，以下仅列出几项有代表性的操作。
1）__init__(self,a,b)：构造方法，返回一个a/b的最简有理数
2）__gcd__(self,a,b):私有方法，求a和b的最大公约数
3）__simple__(self):私有方法，化简分数
4）getFz(self)：返回分子；
5）getFm(self)：返回分母；
6）print(self)：输出有理数；
7）add(self,x)：求当前有理数与有理数x的和；
8）sub(self,x)：求当前有理数与有理数x的差；
9）mul(self,x)：求当前有理数与有理数x的积；

"""

class Rational:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__simple__()

    def __gcd__(self, a, b):
        if b == 0:
            return a
        return self.__gcd__(b, a % b)

    def __simple__(self):
        c = self.__gcd__(self.a, self.b)
        self.a //= c
        self.b //= c

    def getFz(self):
        return self.a

    def getFm(self):
        return self.b

    def print(self):
        print("%d/%d" % (self.a, self.b))

    def add(self, x):
        n = self.b * x.b // self.__gcd__(self.b, x.b)
        self.a = self.a * n // self.b + x.a * n // x.b
        self.b = n
        self.__simple__()

    def sub(self, x):
        n = self.b * x.b // self.__gcd__(self.b, x.b)
        self.a = self.a * n // self.b - x.a * n // x.b
        self.b = n
        self.__simple__()


    def mul(self, x):
        self.a *= x.a
        self.b *= x.b
        self.__simple__()

    def div(self, x):
        self.a *= x.b
        self.b *= x.a
        self.__simple__()

# 主程序
r1 = Rational(2, 4)
r2 = Rational(5, 15)
r1.print()
r2.print()
r1.add(r2)
r1.print()
r1.sub(r2)
r1.print()
r1.mul(r2)
r1.print()
r1.div(r2)
r1.print()