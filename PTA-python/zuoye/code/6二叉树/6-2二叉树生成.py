class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTrees(n):
    if n == 0:
        return []
    return generate(1, n)

def generate(start, end):
    if start > end:
        return [None]
    all_trees = []
    for i in range(start, end + 1):
        left_trees = generate(start, i - 1)
        right_trees = generate(i + 1, end)
        for l in left_trees:
            for r in right_trees:
                current_tree = TreeNode(i)
                current_tree.left = l
                current_tree.right = r
                all_trees.append(current_tree)
    return all_trees

def printTree(node, prefix="", isLeft=True):
    if node is not None:
        print(prefix + ("|-- " if isLeft else "\\-- ") + str(node.val))
        printTree(node.left, prefix + ("|   " if isLeft else "    "), True)
        printTree(node.right, prefix + ("|   " if isLeft else "    "), False)

# 测试程序
n = int(input("请输入节点数: "))
trees = generateTrees(n)
print(f"Number of unique BSTs with {n} nodes: {len(trees)}")

for i, tree in enumerate(trees):
    print(f"\nTree {i + 1}:")
    printTree(tree)