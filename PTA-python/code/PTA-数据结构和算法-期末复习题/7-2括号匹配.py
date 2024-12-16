"""
给定一串字符，不超过100个字符，可能包括括号、数字、字母、标点符号、空格，编程检查这一串字符中的( ) ,[ ],{ }是否匹配。

输入格式:
输入在一行中给出一行字符串，不超过100个字符，可能包括括号、数字、字母、标点符号、空格。

输出格式:
如果括号配对，输出yes，否则输出no。

输入样例1:
sin(10+20)
输出样例1:
yes
输入样例2:
{[}]
输出样例2:
no
"""

def is_matching_parentheses(s):  
    """检查字符串中的括号是否匹配"""  
    # 定义一个栈用于存储开括号  
    stack = []  

    # 定义一个映射，表示每种开括号对应的闭括号  
    matching_bracket = {')': '(', ']': '[', '}': '{'}  

    # 遍历字符串中的每个字符  
    for char in s:  
        # 如果是开括号，压入栈中  
        if char in matching_bracket.values():  
            stack.append(char)  
        # 如果是闭括号  
        elif char in matching_bracket:  
            # 如果栈为空或者栈顶元素与当前闭括号不匹配  
            if not stack or stack[-1] != matching_bracket[char]:  
                return "no"  
            # 匹配成功，弹出栈顶元素  
            stack.pop()  

    # 如果栈为空，则所有括号都匹配，否则不匹配  
    return "yes" if not stack else "no"  


if __name__ == "__main__":  
    # 读取输入行  
    input_string = input().strip()  
    
    # 检查括号是否匹配  
    result = is_matching_parentheses(input_string)  
    
    # 输出结果  
    print(result)