def interval_greedy(_intervals):
    # 1. 按照结束时间对区间进行排序
    sorted_intervals = sorted(_intervals, key=lambda x: x[1])

    # 2. 选择第一个区间
    selected_intervals = []
    end_time = -float('inf')  # 上一个选择的区间的结束时间

    for interval in sorted_intervals:
        # 如果当前区间的开始时间大于等于上一个选择区间的结束时间，则选择该区间
        if interval[0] >= end_time:
            selected_intervals.append(interval)
            end_time = interval[1]  # 更新结束时间

    return selected_intervals


# 示例输入
intervals = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 8)]
result = interval_greedy(intervals)
print("选择的区间:", result)
