"""
寫一個function來做商品計數， function會接收一個data清單中裝著 '麥香奶茶 2'  這樣的字串，字串中空格分開商品名稱跟數量，特別注意，商品名稱可以重複，重複時請把數量累加上去計數。請看下面function的參數的例子。

function的參數：
    data：一個清單裝著字串，例如 ['麥香奶茶 2', '御飯糰 1', '可可 10', '麥香奶茶 1']  <- 這只是範例喔

function的回傳：
    字典裝著計數完的結果，例如 {'麥香奶茶': 3, '御飯糰': 1, '可可': 10} 
"""

data = ['麥香奶茶 2', '御飯糰 1', '可可 12', '麥香奶茶 1']

def count_products(data):
    dic = {}
    for line in data:
        key = line.split()[0]
        value = int(line.split()[1])
        if key not in dic:
            dic[key] = value
        elif key in dic:
            dic[key] += value
    print(dic)


count_products(data)