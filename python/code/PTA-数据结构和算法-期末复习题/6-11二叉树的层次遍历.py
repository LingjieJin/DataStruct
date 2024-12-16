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
            
#定义抽象类型队列Queue，FIFO（First In,First Out)
class Queue:
    #1.构造方法,定义一个空的列表
    def __init__(self):
        self.items = []
    #2.入队,队尾（列表尾部）入队
    def push(self,item):
        self.items.append(item)
    #3.出队，队首（列表头部）出队
    def pop(self):
        return self.items.pop(0)
    #4.判断队列是否为空
    def isEmpty(self):
        return self.items == []
    #5.取队首
    def getFront(self):
        return self.items[0]
    #6.求队列大小
    def getSize(self):
        return len(self.items)
    
def layerOrder(T):  
    if T is None:  
        return  
    
    queue = Queue()  # 创建一个队列  
    queue.push(T)    # 将根节点入队  
    result = []      # 用于存储遍历结果  

    while not queue.isEmpty():  
        current_node = queue.pop()  # 出队一个节点  
        result.append(current_node.getRoot())  # 将节点值添加到结果中  
        
        # 将子节点按照顺序入队  
        if current_node.getLeft() is not None:  
            queue.push(current_node.getLeft())  
        if current_node.getRight() is not None:  
            queue.push(current_node.getRight())  

    print(' '.join(result)+" ")  # 输出结果，节点值之间用空格分隔  


def createBT():
    pass

T = createBT()   #创建二叉树，实现细节不表
layerOrder(T)      #输出层次遍历

#你的代码将被嵌在这里
