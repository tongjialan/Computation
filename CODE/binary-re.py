# 二分查找

# 原始数据 value - [1,2,3,4,5,6,7,8,9,10,11,12,13]
# 待查找数据 key - 9
# 每次查找范围的左侧下标值 left
# 每次查找范围的右侧下标值 right
def binary(value, key, left, right):
    # 递归退出条件
    if left > right: 
        # 查找失败,返回-1
        return -1

    # 获取中间元素对应下标值
    middle = (left + right) // 2
    # 对比中间元素值与指定查找值
    # 如果两者相同
    if value[middle] == key:
        # 查找成功,返回对应下标值
        return middle
    # 如果指定值小于中间值
    elif value[middle] > key:
        # 则在左侧继续查找
        # 查找范围减半:左侧下标值不变
        # 而右侧下标值为中间值的前一位置
        return binary(value, key, left, middle-1)
    # 如果指定值大于中间值
    else:
        # 则在右侧继续查找
        # 查找范围减半:右侧下标值不变
        # 而左侧下标值为中间值的后一位置
        return binary(value, key, middle+1, right)


if __name__ == "__main__":
    # 原始数据 - 有序
    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    # 待查找数据
    key = 9

    # 二分查找
    res = binary(value, key, 0, len(value)-1)
    if res == -1:
        # 查找失败
        print("查找失败")
    else:
        # 查找成功
        print("查找成功,对应下标值:", res)






