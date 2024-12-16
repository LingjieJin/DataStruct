#二叉树的存储-二叉链表
class BinaryTree:
    #1.构造方法
    def __init__(self,newValue):
        self.key = newValue     #树根
        self.left = None        #左子树初始化为空
        self.right = None       #右子树初始化为空
    #2.访问左子树
    def getLeft(self):
        return self.left
    #3.访问右子树
    def getRight(self):
        return self.right
    #4.修改树根的值
    def setRoot(self,newValue):
        self.key = newValue
    #5.访问树根的值
    def getRoot(self):
        return self.key


def leafCount(node):
    if not node:
        return 0
    
    if not node.getLeft() and not node.getRight():
        return 1
    
    return leafCount(node.getLeft()) + leafCount(node.getRight())

def createBT():
    pass

T = createBT()   #创建二叉树，实现细节不表
print(leafCount(T))

#你的代码将被嵌在这里
