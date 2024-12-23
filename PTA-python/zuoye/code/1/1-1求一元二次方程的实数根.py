'''''
编写一个Python程序，求一元二次方程的实数根，并采用相关数据测试。
本题要求设计一个类Equ，包含:
1）4个对象属性a,b,c和ans，a,b,c对应一元二次方程的系数，ans对应方程的解，可用列表类型；
2）3个对象方法，包括构造方法，求解方法solve和输出方法print。
3）主程序给出3组测试数据，对应无实数根，有1个实数根和2个实数根。
'''

import math

class Equ:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.ans = []

    def solve(self):
        delta = self.b ** 2 - 4 * self.a * self.c
        if delta > 0:
            root1 = (-self.b + math.sqrt(delta)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(delta)) / (2 * self.a)
            self.ans = [root1, root2]
        elif delta == 0:
            root = -self.b / (2 * self.a)
            self.ans = [root]
        else:
            self.ans = []

    def print(self):
        if len(self.ans) == 0:
            print("无实数根")
        elif len(self.ans) == 1:
            print(f"有一个实数根: {self.ans[0]}")
        else:
            print(f"有两个实数根: {self.ans[0]} 和 {self.ans[1]}")


def test():
    # 主程序测试
    test_cases = [
        (1, 2, 3),  # 无实数根
        (1, -2, 1), # 有一个实数根
        (1, -3, 2)  # 有两个实数根
    ]

    for a, b, c in test_cases:
        equation = Equ(a, b, c)
        equation.solve()
        equation.print()

equation = Equ(1, -2, -3)
equation.solve()
equation.print()