"""
学生成绩管理程序，参考附件2的代码完成。
    编写一个简单的学生成绩管理程序，每个学生记录包含学号、姓名、课程和分数，采用顺序表存储，完成以下功能：
1）屏幕显示所有学生记录；
2）输入一个学生记录；
3）按学号和课程删除一个学生记录；
4）按学号排序并输出所有学生记录；
5）按课程排序，对于一门课程，学生按分数递减排序。

"""
class stuList:
    # 存放学生记录的列表
    def __init__(self):
        self.data = []

    def add(self):  # 输入一个学生的记录
        s = input("请输入一个学生记录（学号，姓名，课程，成绩）：").split()
        no = int(s[0])      # 学号
        name = s[1]         # 姓名
        course = s[2]       # 课程
        score = int(s[3])   # 成绩
        self.data.append([no, name, course, score])

    # 输出所有学生记录,注意格式
    def print(self):
        n = len(self.data)
        if n <= 0:
            print("成绩表为空")
            return
        print("========================================================")
        print("\t学号\t\t姓名\t\t课程\t\t成绩")
        for i in range(n):
            print("\t%d\t\t%s\t\t%s\t\t%d" % (self.data[i][0], self.data[i][1], self.data[i][2], self.data[i][3]))
        print("========================================================")

    # 根据学号和课程删除指定学生的记录
    def erase(self, no, course):
        for i in range(len(self.data)):
            if self.data[i][0] == no and self.data[i][2] == course:
                del self.data[i]
                print(f"已删除学号为{no}，课程为{course}的记录")
                return
        print(f"未找到学号为{no}，课程为{course}的记录")

    # 按学号排序并输出
    def sort1(self):
        self.data.sort(key=lambda s: s[0])
        self.print()

    # 按课程和分数递减排序并输出
    def sort2(self):
        self.data.sort(key=lambda s: (s[2], -s[3]))
        self.print()

# 主程序
s = stuList()
while True:
    print("1.显示全部记录\n2.输入\n3.删除\n4.按学号排序\n5.课程排序\n0.退出")
    ch = int(input())
    if ch == 0:
        print("欢迎下次使用，系统即将退出！")
        break
    elif ch == 1:
        s.print()
    elif ch == 2:
        s.add()
    elif ch == 3:  # 删除一个学生
        no = int(input("请输入删除的学号："))
        course = input("请输入删除的课程：")
        s.erase(no, course)
    elif ch == 4:
        s.sort1()
    elif ch == 5:
        s.sort2()
    else:
        print("你的选择有误，请重新输入！")