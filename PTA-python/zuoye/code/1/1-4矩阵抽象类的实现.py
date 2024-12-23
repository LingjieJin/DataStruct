"""
类型名称：Matrix
数据对象集：一个 的矩阵 A。
操作集：对于任意矩阵A、B、C   Matrix，以及正整数i、j、M、N，以下仅列出几项有代表性的操作。
1）__init__(self,m,n,a)：构造方法，用列表a返回一个 的矩阵；
2）getMatRow(self)：返回矩阵的总行数；
3）getMatCol(self)：返回矩阵的总列数；
4）print(self)：输出矩阵a；
5）getEntry(self,i,j)：返回矩阵的第i行、第j列的元素；
6）add(self,b)：如果当前矩阵和b是同型矩阵（行数、列数相同），则返回矩阵c=a+b，否则返回错误标志；
7）mul(self,b)：如果当前矩阵的列数等于b的行数，则返回矩阵c = ab，否则返回错误标志；

"""

class Matrix:
    def __init__(self, m, n, a=[]):
        self.m = m
        self.n = n
        self.a = [[0 for i in range(n)] for j in range(m)]
        x = len(a)
        if x < m * n:
            a.extend([0] * (m * n - x))
        else:
            a = a[:m * n]
        for i in range(self.m):
            for j in range(self.n):
                self.a[i][j] = a[i * n + j]

    def getMatRow(self):
        return self.m

    def getMatCol(self):
        return self.n

    def print(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.a[i][j], end=" ")
            print()

    def getEntry(self, i, j):
        if 0 <= i < self.m and 0 <= j < self.n:
            return self.a[i][j]
        else:
            return "Index out of range"

    def add(self, b):
        """
        将两个相同大小的矩阵相加。

        参数:
            b (Matrix): 要相加的矩阵。

        返回:
            Matrix: 一个新的矩阵，是两个矩阵的和。
            str: 如果矩阵大小不同，则返回错误信息。
        """
        if self.m != b.m or self.n != b.n:
            return "Matrices are not of the same size"
        c = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                c.a[i][j] = self.a[i][j] + b.a[i][j]
        return c

    def mul(self, b):
        """
        实现矩阵乘法。

        参数:
        - b: 另一个矩阵对象，当前矩阵将与之相乘。

        返回:
        - 如果矩阵的列数与b矩阵的行数不相等，返回错误信息。
        - 否则，创建一个新的矩阵对象，其大小为当前矩阵的行数乘以b矩阵的列数，并返回该矩阵对象。
        """
        if self.n != b.m:
            return "Matrices cannot be multiplied"
        c = Matrix(self.m, b.n)
        for i in range(self.m):
            for j in range(b.n):
                for k in range(self.n):
                    c.a[i][j] += self.a[i][k] * b.a[k][j]
        return c

    def transpose(self):
        """
        转置矩阵。

        返回:
            Matrix: 一个新的矩阵，是原矩阵的转置矩阵。
        """
        c = Matrix(self.n, self.m)
        for i in range(self.m):
            for j in range(self.n):
                c.a[j][i] = self.a[i][j]
        return c

# 主程序
a = Matrix(2, 3, [1, 2, 3, 4, 5, 6])
b = Matrix(2, 3, [6, 5, 4, 3, 2, 1])
c = Matrix(3, 2, [1, 2, 3, 4, 5, 6])

print("Matrix A:")
a.print()
print("Matrix B:")
b.print()
print("Matrix C:")
c.print()

print("A + B:")
d = a.add(b)
if isinstance(d, Matrix):
    d.print()
else:
    print(d)

print("A * C:")
e = a.mul(c)
if isinstance(e, Matrix):
    e.print()
else:
    print(e)

print("Transpose of A:")
f = a.transpose()
f.print()