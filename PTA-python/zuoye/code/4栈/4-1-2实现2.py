# 顺序栈
class SqStack:
    # 0.构造方法,初始化为空栈
    def __init__(self):
        self.data = []

    # 1.入栈
    def push(self, x):
        self.data.append(x)

    # 2.出栈
    def pop(self):
        assert len(self.data) > 0
        return self.data.pop()

    # 3.取栈顶元素
    def getTop(self):
        assert len(self.data) > 0
        return self.data[-1]

    # 4.判断栈是否为空
    def empty(self):
        return len(self.data) == 0

# r必须是在[2,36], x为正整数，除以r倒取余法，用栈实现逆序
def d2R(x, r):
    # 1.定义空栈
    s = SqStack()
    # 2.入栈
    while x > 0:
        t = x % r
        s.push(chr(t - 10 + ord('A')) if t >= 10 else str(t))
        x //= r
    # 3.出栈
    while not s.empty():
        print(s.getTop(), end="")
        s.pop()
    print()

# 处理多组测试数据
while True:
    try:
        x, r = map(int, input().split())
        d2R(x, r)
    except:
        break