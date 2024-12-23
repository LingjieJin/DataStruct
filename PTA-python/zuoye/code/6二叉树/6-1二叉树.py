# 二叉树的存储-二叉链表
class BTree:
    # 构造方法
    def __init__(self, x=None):
        self.root = x  # 树根
        self.lchild = None  # 左子树初始化为空
        self.rchild = None  # 右子树初始化为空

# 根据补空法字符串s创建二叉树
def create(s):
    if s[0] == '#':
        s.pop(0)
        return None
    T = BTree(s[0])
    s.pop(0)
    T.lchild = create(s)
    T.rchild = create(s)
    return T

# 先序遍历二叉树T
def preOrder(T):
    if T is None:  # 递归出口 not T 或 T == None
        return
    print(T.root, end="")  # 输出树根的值
    preOrder(T.lchild)  # 递归访问左子树
    preOrder(T.rchild)  # 递归访问右子树

# 中序遍历二叉树T
def inOrder(T):
    if T is None:  # 递归出口 not T 或 T == None
        return
    inOrder(T.lchild)  # 递归访问左子树
    print(T.root, end="")  # 输出树根的值
    inOrder(T.rchild)  # 递归访问右子树

# 后序遍历二叉树T
def postOrder(T):
    if T is None:  # 递归出口 not T 或 T == None
        return
    postOrder(T.lchild)  # 递归访问左子树
    postOrder(T.rchild)  # 递归访问右子树
    print(T.root, end="")  # 输出树根的值

# 层次遍历二叉树
def layerOrder(T):
    if T is None:
        return
    queue = [T]
    while queue:
        node = queue.pop(0)
        print(node.root, end="")
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)

# 求二叉树T的高度
def getHeight(T):
    if not T:  # 空树的树高为0
        return 0
    lmax = getHeight(T.lchild)  # 左子树的树高
    rmax = getHeight(T.rchild)  # 右子树的树高
    ans = lmax + 1 if lmax > rmax else rmax + 1
    return ans

# 求二叉树T的叶子数
def getLeafCount(T):
    if T is None:
        return 0
    if T.lchild is None and T.rchild is None:
        return 1
    return getLeafCount(T.lchild) + getLeafCount(T.rchild)

# 求二叉树T的结点数
def getNodeCount(T):
    if T is None:
        return 0
    return 1 + getNodeCount(T.lchild) + getNodeCount(T.rchild)

# 测试程序
T = create(list("AB##C##"))
print("先序遍历：", end="")
preOrder(T)
print("\n中序遍历：", end="")
inOrder(T)
print("\n后序遍历：", end="")
postOrder(T)
print("\n层次遍历：", end="")
layerOrder(T)
print("\n二叉树高度：", getHeight(T))
print("二叉树叶子数：", getLeafCount(T))
print("二叉树结点数：", getNodeCount(T))