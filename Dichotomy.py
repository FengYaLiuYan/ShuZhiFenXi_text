from tools import DuoXiangShiQiuZhi as QZ

def Dichotomy(x,precision,a,b):
    res_JingDu = QZ(x,(a + b)/2)
    if QZ(x, a) * QZ(x, b) > 0:
        print("该多项式在实数域区间[", a, ",", b, "]上无解")
        return 0
    while True:
        if QZ(x, a) * QZ(x,(a + b)/2) < 0:
            b = (b + a)/2
            res = QZ(x,(a + b)/2)
        elif QZ(x, b) * QZ(x,(a + b)/2) < 0:
            a = (b + a)/2
            res = QZ(x,(a + b)/2)
        else:
            res = QZ(x,(a + b)/2)
        if abs(res - res_JingDu) < precision:
            break
        res_JingDu = res
    return (a + b)/2