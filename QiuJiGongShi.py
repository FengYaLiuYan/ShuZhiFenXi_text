#区间
a = 0
b = 1
#等分份数
n = 8

def FuHuaTiXing():
    x = [0] * (n + 1)
    res = 0
    temp = a
    # 复化梯形公式
    for i in range(1, n):
        temp += (b - a) / n
        x[i] = temp
        res += 2 * x[i] / (4 + x[i] ** 2)
    for i in a, b:
        res += i / (4 + i ** 2)
    res = res * (b - a) / (2 * n)
    # 函数
    # y = x / (4 + x ** 2)
    print(res)

#变步长复化梯形公式
def BianBuChang():
    Tn = 0
    n = 2
    res = (a / (4 + a ** 2) + b / (4 + b ** 2))/2
    while(True):
        temp = 0
        for i in range(1,n):
            temp += (a + i * (b - a)/n) / (4 + (a + i * (b - a)/n) ** 2)
        res = res / 2 + (b - a) * temp/(n * 2)
        if res - Tn < (5 * 10e-8):
            break
        Tn = res
        n += 2
    print("{:.9f}".format(res))

FuHuaTiXing()
BianBuChang()