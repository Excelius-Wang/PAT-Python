"""
《算法笔记》4.4 简单贪心 问题 B 出租车费

三段计费：
    1. x <= 4 km, 10 元
    2. 4 < x <= 8, 2 元/km
    3. x > 8, 2.4 元/km

贪心策略：
    根据题目分析可以得到，8 km 是最便宜的，这里的贪心策略就是把行程划分为尽可能
    的 8 km 段，最后剩余的行程为 0 - 8 km；
    如果是 0 - 4 km, 用 2.4 计算；
    如果是 4 - 8 km, 用 10 + (x - 2) * 2 计算。
"""


def min_cost(n):
    _ans = 0

    if n <= 4:
        # 当路程为 0 - 4 km
        _ans += 10
    elif n <= 8:
        # 当路程为 4 - 8 km
        _ans += 10 + (n - 4) * 2
    else:
        # 当路程 > 8 km, 按照 8 km 进行分段
        _ans += int(int(n) / 8) * 18;
        n %= 8

        # 剩余不足 8 km 的部分分两段：
        # < 4 km, 用 2.4 km 算
        # 4 - 8 km, 用 10 + (x - 2) * 2 算
        if 0 < n <= 4:
            # 如果剩余行程 <= 4，当作 2.4 来算
            _ans += n * 2.4
        elif 4 < n < 8:
            # 如果剩余行程 4 < x <= 7, 当作 10 + 2 来算
            _ans += 10 + (n - 4) * 2

    return _ans


while True:
    # 输入公里数, 0 退出循环
    distance = int(input())
    if distance == 0:
        break

    # 对于每个公里数，都进行计算
    ans = min_cost(distance)
    # 根据结果格式化输出
    print("{:.1f}".format(ans) if isinstance(ans, float) else ans)
