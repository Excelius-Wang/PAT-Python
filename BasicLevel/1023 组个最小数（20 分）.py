# 获得给定的数字个数
inputs = list(map(int, input().split()))

# 从小到大把所有数字依次添加到 nums
nums = list()
for i in range(10):
    for j in range(inputs[i]):
        nums.append(i)

ans = ""

# 添加第一个最小的非零数字
for num in nums:
    if num != 0:
        ans += str(num)
        # 从 nums 中删除这个数字（remove() 函数只删除第一个匹配的数字）
        nums.remove(num)
        break

# 按顺序把所有数字添加到 ans 即可
for num in nums:
    ans += str(num)

print(ans)
