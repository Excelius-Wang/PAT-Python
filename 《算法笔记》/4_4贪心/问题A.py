"""
《算法笔记》4.4 简单贪心 问题 A 看电视
贪心策略：
    将电视节目按照结束时间进行排序，每次选择结束时间最早的节目，这样保证有尽可能多的时间选择后续节目
"""


def max_programs(_intervals):
    # 贪心策略：将电视节目按照结束时间进行排序，每次选择结束时间最早的节目，这样保证有尽可能多的时间选择后续节目
    sorted_intervals = sorted(_intervals, key=lambda x: x[1])

    ans = 0
    end_time = -float('inf')

    for interval in sorted_intervals:
        if interval[0] >= end_time:
            ans += 1
            end_time = interval[1]

    return ans


# 循环读取输入
while True:
    # 当 n 为 0 时，结束循环
    n = int(input())
    if n == 0:
        break

    # 读取电视节目
    programs = []
    for _ in range(n):
        start, end = map(int, input().split())
        programs.append((start, end))

    # 计算并输出结果
    ans = max_programs(programs)
    print(ans)
