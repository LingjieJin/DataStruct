def check(formula):  
    stack = []  # 用于存储左括号位置的栈  
    position = 0  # 当前字符位置（从1开始计数，不包括空格）  
    # 用于计算实际字符位置的索引  
    actual_index = 0  

    # 遍历公式的每一个字符  
    for char in formula:  
        actual_index += 1  # 实际字符索引增1  
        if char != ' ':  # 忽略空格  
            position += 1  # 更新位置（1-based index）  
        
        if char == '(':  
            # 遇到左括号，将位置入栈  
            stack.append(position)  
        elif char == ')':  
            # 遇到右括号  
            if not stack:  
                # 如果栈为空，说明没有匹配的左括号  
                return f"位置{position}的括号不匹配"  
            # 有匹配的左括号，弹出栈顶元素  
            stack.pop()  

    # 遍历结束后，检查栈是否还有未匹配的左括号  
    if stack:  
        return f"位置{stack[-1]}的括号不匹配"  

    return "括号匹配"  
    
formula = input()
print(check(formula))