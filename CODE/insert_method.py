# 插入排序
# 优于冒泡排序

# 原始数据 
# [80,70,30,50,60,78,90,100,65,88]

def insert(value):
    for i in range(1,len(value)):
        tmp = value[i]
        position = i
        for j in range(i-1,-1,-1):
            if value[j] > tmp:
                value[j+1] = value[j]
                position = j
            else:
                position = j + 1
                break
        value[position] = tmp

if __name__ == '__main__':
    value = [80,70,30,50,60,78,90,100,65,88]
    insert(value)
    print('排序后',value)