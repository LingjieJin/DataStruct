"""
给定一棵二叉树的前序遍历序列和中序遍历序列，要求计算该二叉树的高度。

输入格式:
输入首先给出正整数 n（≤50），为树中结点总数。随后 2 行先后给出前序和中序遍历序列，均是长度为 n 的不包含重复英文字母（区别大小写）的字符串。

输出格式:
输出为一个整数，即该二叉树的高度。

输入样例:
9
ABDFGHIEC
FDHGIBEAC
输出样例:
5
"""

class TreeNode:  
    """二叉树节点类"""  
    def __init__(self, value):  
        self.left = None  
        self.right = None  
        self.value = value  

def build_tree(preorder, inorder):  
    """根据前序和中序遍历构建二叉树"""  
    if not preorder or not inorder:  
        return None  
    
    root_value = preorder[0]  # 前序的第一个元素是根节点  
    root = TreeNode(root_value)  
    root_index = inorder.index(root_value)  # 在中序遍历中找到根节点的位置  

    # 递归构建左子树和右子树  
    root.left = build_tree(preorder[1:1 + root_index], inorder[:root_index])  
    root.right = build_tree(preorder[1 + root_index:], inorder[root_index + 1:])  

    return root  

def tree_height(node):  
    """计算二叉树的高度"""  
    if not node:  
        return 0  
    left_height = tree_height(node.left)  
    right_height = tree_height(node.right)  
    
    return max(left_height, right_height) + 1  

if __name__ == "__main__":  
    # 读取输入  
    n = int(input().strip())  
    preorder = input().strip()  
    inorder = input().strip()  
    
    # 构建二叉树  
    root = build_tree(preorder, inorder)  
    
    # 计算并输出树的高度  
    height = tree_height(root)  
    print(height)