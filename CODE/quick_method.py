# 快速排序

def quick(value):
    if len(value) < 2:
        return value
    mark = value[0]
    small = [x for x in value if x < mark]
    equal = [x for x in value if x == mark]
    big = [x for x in value if x > mark]

    # 递归排序
    return quick(small) + equal + quick(big)

if __name__ == '__main__':
    value = [80,70,30,50,60,78,90,100,65,88]
    value = quick(value)
    print('排序后',value)