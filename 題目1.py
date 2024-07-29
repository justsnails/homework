"""
寫一個function來找出清單中的最大數

function的參數：

    a_list：用來傳遞進去一個清單

function的回傳：

    回傳找到的最大值，如果清單是空的則回傳0



期望的執行結果：

    print(find_max([1, 2, 3]))   應該要印出 3，這行的意思是把清單[1, 2, 3]傳遞進去find_max()，然後把執行完所回傳的東西印出來

    print(find_max([1, -1, -5]))   應該要印出 1

    print(find_max([]))   應該要印出 0

"""


def find_max(a_list):
    if a_list == []: 
        return 0 
    else:
        big = 0
        for max in a_list:
            if max > big:
                big = max
        return big
   


        

print(find_max([1, 2, 3])) 

print(find_max([1, -1, -5]))

print(find_max([])) 