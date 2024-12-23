'''''2.求1+(1+2)+...+(1+2+...+n)之和有以下3种解法。
解法1：采用两重迭代，依次求出后累加。
解法2：采用一重迭代，利用求和后再累加。
解法3：直接利用公式求和。
编写一个Python程序，利用上述3种解法求n=50000时的结果，并给出各种解法的执行时间。
本题要求设计1个类，包括5个方法，对应构造方法、3种解法和输出方法。
'''

import time

class Exp:
    def __init__(self, n):
        self.n = n
        self.ans = 0
        self.tm= 0

    def solve1(self):
        t1 = time.time()
        self.ans = 0
        for i in range(1, self.n + 1):
            for j in range(1, i + 1):
                self.ans += j
            
        t2 = time.time()
        self.tm = t2 - t1

    def solve2(self):
        t1 = time.time()
        s = 0
        self.ans = 0
        for i in range(1, self.n + 1):
            s += i
            self.ans += s
        t2 = time.time()   
        self.tm = t2 - t1

    def solve3(self):
        t1 = time.time()
        n = self.n
        self.ans = n * (n + 1) * (n + 2) // 6
        t2 = time.time()
        self.tm = t2 - t1

    def print(self):
       print("数据规模是:%d,数列的和是:%d,运行时间是:%d秒"%(self.n,self.ans,self.tm))

# 主程序测试
e = Exp(10000)
e.solve1()
e.print()
e.solve2()
e.print()
e.solve3()
e.print()