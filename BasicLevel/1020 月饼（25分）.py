def max_profit(kind, need, stock, value):
    # 月饼单价
    unit_value = {i: value[i] / stock[i] for i in range(kind)}
    # 月饼顺序
    order = sorted(unit_value, key=lambda i:unit_value[i], reverse=True)

    ans = 0

    # 如果月饼需求量还有, 并且当前价值最大的月饼比所需的量大, 就卖出当前月饼
    for i in order:
        if need - stock[i] >= 0:
            ans += value[i]
            need -= stock[i]
        else:
            ans += need * unit_value[i]
            break
    return ans

# 种类和需求
kind, need = map(int, input().split())
# 月饼存量
stock = list(map(float, input().split()))
# 月饼价值
value = list(map(float, input().split()))

ans = max_profit(kind, need, stock, value)

print("{:.2f}".format(ans))
