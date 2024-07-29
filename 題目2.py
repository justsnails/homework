"""
寫一個function來印出誰的成績是第二高，如果超過一個人分數都是第二高，請把人名一行一行印出來。

function的參數：
    students：一個二維清單，例如 [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]] 

function的回傳：
    不須回傳

期望的執行結果：
    例如 有個清單是 students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]  
    second_highest(students)  的執行結果應該要印出：
    Tom
    Harsh

重要提示：
不一定要，但可以使用sorted這個function來排列清單，

例如 
x = [3, 1, 4, 5, 2]
x = sorted(x) # 排列x (由小到大)
print(x) # 印出 [1, 2, 3, 4, 5]

如果要顛倒排列也可以，只要多加reverse=True

x = [3, 1, 4, 5, 2]
x = sorted(x, reverse=True) # 排列x (由大到小)
print(x) # 印出 [5, 4, 3, 2, 1]
"""
students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]

def second_highest(students):  
    f = {student[1] for student in students} #將數字放進集合裡面 ※重複的數字只會出現一次
    big_num = max(f) # 找出第一大的數字
    f.remove(big_num) # 刪除第一大的數字，成為新的清單
    second_num = max(f) # 找出次高的分數
    score = []
    for line in students:
        if line[1] == second_num: # 找出跟次高分數相同的清單
            score.append(line) # 增加進新的清單
    for answer in score:
        print(answer[0]) # 列印出name

second_highest(students)