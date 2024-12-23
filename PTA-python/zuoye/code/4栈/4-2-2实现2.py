# 链式栈
# 结点
class LinkNode:
    # 构造方法
    def __init__(self, x=None):
        self.data = x       # 数据域
        self.next = None    # 指针域

class LinkStack:
    # 0.构造方法,初始化为空栈
    def __init__(self):
        self.top = None   # 空栈

    # 1.入栈,头插法
    def push(self, x):
        p = LinkNode(x)         # 创建新结点
        p.next = self.top
        self.top = p

    # 2.出栈
    def pop(self):
        assert self.top is not None
        p = self.top
        self.top = self.top.next
        return p.data

    # 3.取栈顶元素
    def getTop(self):
        assert self.top is not None
        return self.top.data

    # 4.判断栈是否为空
    def empty(self):
        return self.top is None

# 检查括号匹配
def isValid(s: str) -> bool:
    dc = {")": "(", "]": "[", "}": "{"}  # 字典，右括号到左括号的映射
    st = LinkStack()    # 定义链栈
    # 遍历字符串
    for c in s:
        # 左括号入栈
        if c in "([{":
            st.push(c)
        # 右括号出栈
        elif c in ")]}":
            if st.empty():  # 栈为空
                return False
            if st.getTop() != dc[c]:  # 匹配失败
                return False
            st.pop()
    return st.empty()  # 栈为空匹配成功

# 处理多组测试数据
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if line:
            print("yes" if isValid(line) else "no")

if __name__ == "__main__":
    main()