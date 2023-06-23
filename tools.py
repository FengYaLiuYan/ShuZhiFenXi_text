import numpy as np

from matplotlib import pyplot as plt

#大数运算（整数）
#大数去零化简
def DaShu_HuaJian(res):
    len_res = len(res)
    len_real = 0
    for i in range(1,len_res):
        if res[i] == 0:
            len_real += 1
        else:
            break
    res_new = [ 0 for i in range(len_res - len_real)]
    res_new[0] = res[0]
    for i in range(1,len_res - len_real):
        res_new[i] = res[len_real + i]
    if len(res_new) == 1:
        res_new.append(0)
    return res_new

#大数绝对值比大小
def DaShu_abs_maxsize(a,b):
    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        return True
    elif len_a < len_b:
        return False
    else:
        for i in range(1, len(a)):
            if a[i] > b[i]:
                return True
            elif a[i] < b[i]:
                return False

#大数取绝对值
def DaShu_abs(a):
    if a[0] == -1:
        a[0] = 1
        return a
    else:
        return a

#大数判断绝对值相等
def DaShu_abs_equal(a,b):
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        return False
    for i in range(1,len_a):
        if a[i] != b[i]:
            return False
    return True

#大数结果符号判断
def DaShu_symbol(a,b,sign):
    len_a = len(a)
    len_b = len(b)
    if a[0] * b[0] > 0:
        return a[0]
    elif a[1] == 0:
        if sign == 0:
            return b[0]
        else:
            return a[0]
    elif b[1] == 0:
        if sign == 0:
            return a[0]
        else:
            return b[0]
    else:
        if len_a == len_b and (DaShu_abs_maxsize(a,b) or DaShu_abs_equal(a,b)):
            if a[0] == 1:
                return 1
            else:
                return -1
        else:
            if len_a > len_b:
                if a[0] == 1:
                    return 1
                else:
                    return -1
            else:
                if a[0] == -1:
                    return 1
                else:
                    return -1

#大数互换判断
def DaShu_HuHuanPanDuan(a,b):
    if len(a) < len(b):
        return True
    elif len(a) == len(b):
        for i in range(1,len(a)):
            if a[i] > b[i]:
                return False
            elif a[i] < b[i]:
                return True
    else:
        return False

#大数取负
def DaShu_QuFu(res):
    res[0] = res[0] * -1
    return res

#大数加法
def DaShu_JiaFa(a,b):
    #a[-1,a0,a1,a2,...]
    #b[1,b0,b1,b2,...]
    #判断是否交换，确保大数在前
    if DaShu_HuHuanPanDuan(a,b):
        temp = a
        a = b
        b = temp

    #取负计算再将结果取负不影响结果
    sign = 0
    if a[0] == -1:
        a = DaShu_QuFu(a)
        b = DaShu_QuFu(b)
        sign = 1

    len_a = len(a)
    len_b = len(b)
    #创建运算结果，并先将大数放入
    c = [0 for i in range(len_a + 1)]
    c[0] = DaShu_symbol(a,b,sign)
    for i in range(1,len_a):
        c[i + 1] = a[i]

    #运算主程序
    if a[1] == 0:
        if sign != 0:
            b = DaShu_QuFu(b)
        return b
    elif b[1] == 0:
        if sign != 0:
            a = DaShu_QuFu(a)
        return a
    else:
        for i in range(1,len(b)):
            c[len(c) - i] = c[len(c) - i] + b[0] * b[len_b - i]
        for i in range(1,len_a):
            if c[len(c) - i] >= 10:
                c[len(c) - i - 1] += 1
            elif c[len(c) - i] < 0:
                c[len(c) - i - 1] -= 1
            c[len(c) - i] = c[len(c) - i] % 10
    c = DaShu_HuaJian(c)
    if sign != 0:
        c = DaShu_QuFu(c)
    return c

#大数减法
def DaShu_JianFa(a,b):
    b = DaShu_QuFu(b)
    res = DaShu_JiaFa(a,b)
    return res

#大数乘法
def DaShu_ChengFa(a,b):
    len_a = len(a)
    len_b = len(b)
    c = [0 for i in range(2)]
    c[0] = 1
    d = [0 for i in range(len_a + 1)]
    d[0] = 1
    for i in range(len_b - 1):
        d = [0 for i in range(len_a + 1)]
        d[0] = 1
        for j in range(len_a - 1):
            e = [0 for m in range(3)]
            e [0] = 1
            e[len(e) - 1] =  (e[len(e) - 1] + b[len_b - i - 1] * a[len_a - j - 1]) % 10
            e[len(e) - 2] += int((b[len_b - i - 1] * a[len_a - j - 1]) / 10)
            e = DaShu_HuaJian(e)
            for k in range(j):
                e.append(0)
            d = DaShu_JiaFa(e,d)
        d = DaShu_HuaJian(d)
        for k in range(i):
            d.append(0)
        c = DaShu_JiaFa(c,d)
    c[0] = a[0] * b[0]
    return c

#大数切片判断
def DaShu_Cut(len_a,len_b,i):
    if -(len_a - i - len_b) == 0:
        return None
    else:
        return -(len_a - i - len_b)

#大数除法（有余除法）、
def DaShu_ChuFa(a_old,b_old):
    a = a_old[:]
    b = b_old[:]
    len_a = len(a)
    len_b = len(b)
    symbol = a[0] * b[0]
    a = DaShu_abs(a)
    b = DaShu_abs(b)
    if DaShu_abs_maxsize(b,a):
        return [1,0]
    c = [1]
    #除数位数：len_a - len_b + 1
    for i in range(len_a - len_b + 1):
        # if len(a) != len_a - len_b - i:
        #     c.append(0)
        #     break
        d = [1, 0]
        for j in range(11):
            e = DaShu_ChengFa(b, d)
            if DaShu_abs_maxsize(e, a[:DaShu_Cut(len_a,len_b,i)]):
                d[1] -= 1
                if d[1] == -1:
                    c.append(0)
                    break
                e = DaShu_ChengFa(b, d)
                c.append(d[1])
                if e[1] == 0:
                    break
                else:
                    e = e + [0] * (len_a - len_b - i)
                    a = DaShu_JianFa(a,e)
                break
            d[1] += 1
    c[0] = symbol
    c = DaShu_HuaJian(c)
    return c

#大数除余（有余除法）、
def DaShu_ChuYu(a_old,b_old):
    a = a_old[:]
    b = b_old[:]
    len_a = len(a)
    len_b = len(b)
    symbol = a[0] * b[0]
    a = DaShu_abs(a)
    b = DaShu_abs(b)
    if DaShu_abs_maxsize(b,a):
        return a
    c = [1]
    #除数位数：len_a - len_b + 1
    for i in range(len_a - len_b + 1):
        d = [1, 0]
        for j in range(11):
            e = DaShu_ChengFa(b, d)
            if DaShu_abs_maxsize(e, a[:DaShu_Cut(len_a,len_b,i)]):
                d[1] -= 1
                e = DaShu_ChengFa(b, d)
                c.append(d[1])
                if e[1] == 0:
                    break
                else:
                    e = e + [0] * (len_a - len_b - i)
                    a = DaShu_JianFa(a,e)
                break
            d[1] += 1
    return a

#大数Int转数组类型
def DaShu_Int_DaShu(x):
    res = []
    x_beifen = x
    x = abs(x)
    while True:
        res.append(x % 10)
        x = int(x / 10)
        if x == 0:
            break
    if x_beifen >= 0:
        res.append(1)
    else:
        res.append(-1)
    res.reverse()
    return res

#大数数组转Int类型
def DaShu_DaShu_Int(x):
    res = 0
    for i in range(1,len(x)):
        temp = x[len(x) - i]
        for j in range(i - 1):
            temp = temp * 10
        res += temp
    res = res * x[0]
    return res

#分数运算
#化简
def FenShu_YueFen(res):
    x = res[0]
    y = res[1]
    while True:
        if DaShu_ChuYu(x,y) == [1,0]:
            break
        else:
            c = DaShu_ChuYu(x,y)
            x = y
            y = c
    res[0] = DaShu_ChuFa(res[0],y)
    res[1] = DaShu_ChuFa(res[1],y)
    return res

#加法
def FenShu_JiaFa(a,b):
    if type(a) == type([1,1]) and type(a[0]) == type(0):
        for i in range(len(a)):
            a[i] = DaShu_Int_DaShu(a[i])
    if type(b) == type([1,1]) and type(b[0]) == type(0):
        for i in range(len(b)):
            b[i] = DaShu_Int_DaShu(b[i])
    if type(a) == type(0):
        a = [DaShu_Int_DaShu(a),[1,1]]
    if type(b) == type(0):
        b = [DaShu_Int_DaShu(b),[1,1]]
    res = [DaShu_JiaFa(DaShu_ChengFa(a[0],b[1]),DaShu_ChengFa(a[1],b[0])),DaShu_ChengFa(a[1],b[1])]
    FenShu_YueFen(res)
    return res

#减法
def FenShu_JianFa(a,b):
    if type(a) == type([1,1]) and type(a[0]) == type(0):
        for i in range(len(a)):
            a[i] = DaShu_Int_DaShu(a[i])
    if type(b) == type([1,1]) and type(b[0]) == type(0):
        for i in range(len(b)):
            b[i] = DaShu_Int_DaShu(b[i])
    if type(a) == type(0):
        a = [DaShu_Int_DaShu(a),[1,1]]
    if type(b) == type(0):
        b = [DaShu_Int_DaShu(b),[1,1]]
    res = [DaShu_JianFa(DaShu_ChengFa(a[0],b[1]),DaShu_ChengFa(a[1],b[0])),DaShu_ChengFa(a[1],b[1])]
    FenShu_YueFen(res)
    return res

#乘法
def FenShu_ChengFa(a,b):
    if a == 0 or b == 0:
        return [0,1]
    if type(a) == type([1,1]) and type(a[0]) == type(0):
        for i in range(len(a)):
            a[i] = DaShu_Int_DaShu(a[i])
    if type(b) == type([1,1]) and type(b[0]) == type(0):
        for i in range(len(b)):
            b[i] = DaShu_Int_DaShu(b[i])
    if type(a) == type(0):
        a = [DaShu_Int_DaShu(a),[1,1]]
    if type(b) == type(0):
        b = [DaShu_Int_DaShu(b),[1,1]]
    res = [DaShu_ChengFa(a[0],b[0]),DaShu_ChengFa(a[1],b[1])]
    FenShu_YueFen(res)
    return res

#除法
def FenShu_ChuFa(a,b):
    if a == 0:
        return [0,1]
    elif b == 0:
        raise Exception("分母不可为0")
    if type(a) == type([1,1]) and type(a[0]) == type(0):
        for i in range(len(a)):
            a[i] = DaShu_Int_DaShu(a[i])
    if type(b) == type([1,1]) and type(b[0]) == type(0):
        for i in range(len(b)):
            b[i] = DaShu_Int_DaShu(b[i])
    if type(a) == type(0):
        a = [DaShu_Int_DaShu(a),[1,1]]
    if type(b) == type(0):
        b = [DaShu_Int_DaShu(b),[1,1]]
    res = [DaShu_ChengFa(a[0],b[1]),DaShu_ChengFa(a[1],b[0])]
    FenShu_YueFen(res)
    return res

#计算
def FenShu_JiSuan(res):
    if res == [1,0]:
        return res
    res = DaShu_DaShu_Int(res[0]) / DaShu_DaShu_Int(res[1])
    return res

#取负
def FenShu_QuFu(res):
    if DaShu_abs_maxsize([1,0],DaShu_ChengFa(res[0],res[1])):
        if res[0] < 0:
            res[0] = DaShu_QuFu(res[0])
        else:
            res[1] = DaShu_QuFu(res[1])
    else:
        res[0] = DaShu_QuFu(res[0])
    return res

#多项式
#相乘
def DuoXiangShiChengFa(f1,f2):#两个n，m次多项式
    len1 = 0
    len2 = 0
    for i in range(0,len(f1)):#检测f1有效长度
        if f1[i] != 0:
            len1 += 1
    for i in range(0,len(f2)):#检测f2有效长度
        if f2[i] != 0:
            len2 += 1
    res = [0]*(len(f1) + len(f2) - 1)#创建结果系数矩阵
    for i in range(len(f1)):
         for j in range(len(f2)):
            res[i + j] += f1[i] * f2[j]#f1、f2每两项两两相乘
    return res

#字符串形式输出
def DuoXiangShiShuChu(res):
    len0 = 0
    times = 0
    y = ""#输出结果
    for i in range(0,len(res)):
        if res[i] != 0:
            len0 = i#判断为0项及极小项
            break
        else:
            continue
    len0 = len(res) - len0#刷新有效长度，用于输出
    for i in range(0,len(res)):
        if res[i] == 0 or abs(res[i]) < 10e-10:#判断为0项及极小项，是则跳过输出
            if y != '' and res[i] != 0:
                y += "+"
            continue
        y += str("%.3f"%(res[i]))
        times += 1#用于判断已输出长度，控制结束
        if times == len0:
            break
        else:
            y += "x^" + str(len(res) - i - 1)
            if res[i + 1] < 0:#若后一项系数为负则跳过
                continue
            elif times < len0 and res[i + 1] != 0:#已输出次数小于有效长度且下一项不为0
                y += "+"
    if y == '':
        y = '0.000'
    return y

#求k阶导（仅限多项式）
def DuoXiangShiQiuDao(res,k):
    for i in range(0,len(res)):
        if res[i] != 0:
            len0 = i#判断为0项及极小项
            break
        else:
            continue
    len0 = len(res) - len0#刷新有效长度，用于输出
    for j in range(0,k):
        if j < len0 - 1:
            new = [0] * (len0 - j - 1)
            for i in range(1, len(res)):
                new[(len(res) - i) % len(res) - 1] = i * res[len(res) - i - 1]
            res = new
        else:
            res = [0.0]
    return res

#[a,b]区间上定积分（仅限多项式）
def DuoXiangShiDingJiFen(res,a,b):
    new = [0] * (len(res) + 1)
    for i in range(0,len(res)):
        new[i] = res[i]/(len(res) - i)
    x = [a,b]
    y = [0.0] * len(x)
    for i in range(0,len(x)):
        for j in range(0,len(new)):
            if new[j] == 0:
                continue
            elif j == len(new) - 1:
                y[i] += new[j]
            else:
                y[i] += new[j] * np.power(x[i],len(new) - j - 1)
    c = y[1] - y[0]
    return c

#给定多项式求某一定点值
def DuoXiangShiQiuZhi(res,x):
    y = 0.0
    for j in range(0, len(res)):
        if res[j] == 0:
            continue
        elif j == len(res) - 1:
            y += res[j]
        else:
            y += res[j] * np.power(x, len(res) - j - 1)
    return y

#多项式绘图
def HuiTu(res,b,Num0):#绘图
    #以下语句无法直接使用
    #y = -0.08333333x^3 + 0.75000000x^2 - 1.66666667x^1 + 1.00000000
    #y = -0.08333333 * np.power(3,x) + 0.75000000 * np.power(2,x) - 1.66666667 * np.power(1,x) + 1.00000000
    x = np.arange(-10, 10, 0.01)
    y = [0.0] * len(x)
    for i in range(0,len(x)):
        for j in range(0,len(res)):
            if res[j] == 0:
                continue
            elif j == len(res) - 1:
                y[i] += res[j]
            else:
                y[i] += res[j] * np.power(x[i],len(res) - j - 1)
    plt.figure(num= Num0)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y=' + DuoXiangShiShuChu(res))
    plt.plot(x,y)
    for i in range(0,len(res)):#标点
        plt.scatter(b[0][i],b[1][i])
    plt.show()

#组合
def C(a,b):
    up = 1
    down = 1
    c = b - a
    for i in range(0,b - c):
        up *= b
        b -= 1
        down *= a
        a -= 1
    return int(up/down)

#矩阵运算
#加法
def matrix_JiaFa(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception ("两矩阵行列不等")
    c = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a[0])):
        for j in range(len(a)):
            c[i][j] = FenShu_JiaFa(a[i][j],b[i][j])
    return c

#减法
def matrix_JianFa(a,b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise Exception ("两矩阵行列不等")
    c = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a[0])):
        for j in range(len(a)):
            c[i][j] = FenShu_JianFa(a[i][j],b[i][j])
    return c

#乘法
def matrix_ChengFa(a,b):
    if len(a[0]) != len(b):
        raise Exception ("无法相乘")
    c = [[0 for i in range(len(b[0]))] for j in range(len(a))]
    for k in range(len(a)):
        for m in range(len(b[0])):
            for n in range(len(b)):
                c[k][m] = FenShu_JiaFa(c[k][m],FenShu_ChengFa(a[k][n],b[n][m]))
    return c

#数量乘法
def matrix_num_ChengFa(a,k):
    k = [DaShu_Int_DaShu(k),[1,1]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[j][i] = [DaShu_Int_DaShu(a[j][i]),[1,1]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = FenShu_ChengFa(a[i][j],k)
            FenShu_YueFen(a[i][j])
    return a

#转置
def matrix_ZhuanZhi(a):
    b = [[0 for i in range(len(a))]for j in range(len(a[0]))]
    for i in range(len(a)):
        temp = a[i]
        for j in range(len(a[0])):
            b[j][i] = temp[j]
    return b

#求逆
def matrix_QiuNi_LU(a):
    #判断行列元素个数是否相等
    if len(a) != len(a[0]):
        print("无法求逆，因为该矩阵非方阵")
        return -1

    #判断a矩阵是否可逆
    reversible = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[j][i] == 0:
                reversible += 1
        if reversible == len(a):
            print("矩阵行列式为0，不可逆")
            return -1
        reversible = 0
    del reversible

    #创建L，U矩阵
    L = [[0 for i in range(len(a))] for j in range(len(a))]
    U = [[0 for i in range(len(a))] for j in range(len(a))]
    for i in range(len(L)):
        L[i][i] = [[1,1],[1,1]]
        U[i][i] = [[1,1],[1,1]]

    #创建a逆矩阵
    a_inverse = [[0 for i in range(len(a))] for j in range(len(a))]
    for i in range(len(a_inverse)):
        a_inverse[i][i] = [[1,1],[1,1]]

    #对矩阵处理
    for i in range(len(a)):
        for j in range(len(a[0])):
            if type(a[i][j]) == type(0):
                a[i][j] = [DaShu_Int_DaShu(a[i][j]),[1,1]]

    #行变换列主元素选取，确保对角线元素无零元，可以进行高斯消去
    #记录变换顺序
    for k in range(len(a)):
        # 列主元素选取
        # 存放当前列绝对值最大值
        max_abs = 0
        #记录绝对值最大列元素行
        order = []
        order_inverse = []
        for i in range(len(a)):
            if max_abs < abs(FenShu_JiSuan(a[i][k])):
                # 替换最大值
                max_abs = abs(FenShu_JiSuan(a[i][k]))
                order = a[i]
                order_inverse = a_inverse[i]
        for j in range(len(order)):
            a[k][j] = FenShu_JiaFa(a[k][j], order[j])
            a_inverse[k][j] = FenShu_JiaFa(a_inverse[k][j],order_inverse[j])
    del order,order_inverse

    #LU三角分解
    for r in range(0, len(a)):
        for i in range(r, len(a)):
            sum_lu2 = [[1,0],[1,1]]
            for k in range(r):
                sum_lu2 = FenShu_JiaFa(sum_lu2, FenShu_ChengFa(L[r][k], U[k][i]))
            U[r][i] = FenShu_JianFa(a[r][i], sum_lu2)
            sum_lu3 = [[1,0],[1,1]]
            for k in range(r):
                sum_lu3 = FenShu_JiaFa(sum_lu3, FenShu_ChengFa(L[i][k], U[k][r]))
            L[i][r] = FenShu_ChuFa(FenShu_JianFa(a[i][r], sum_lu3), U[r][r])
    del sum_lu2,sum_lu3

    #求L逆
    #创建L逆矩阵
    L_inverse = [[0 for i in range(len(L))] for j in range(len(L))]
    for i in range(len(L_inverse)):
        L_inverse[i][i] = [[1,1],[1,1]]
    # 创建m下三角矩阵
    m_L = [[L[j][i] for i in range(len(L))] for j in range(len(L))]
    for i in range(len(m_L)):
        m_L[i][i] = [[1,1],[1,1]]

    # 高斯消去
    for k in range(len(L)):
        for i in range(k + 1, len(L)):
            # m_L[i][k] = FenShu_ChuFa(L[i][k], L[k][k])
            for j in range(i,len(L)):
                # L[j][k] = FenShu_JianFa(L[j][k],FenShu_ChengFa(m_L[j][i - 1], L[i - 1][k]))
                L_inverse[j][k] = FenShu_JianFa(L_inverse[j][k],FenShu_ChengFa(m_L[j][i - 1], L_inverse[i - 1][k]))
    del m_L

    #求U逆
    #创建U逆矩阵
    U_inverse = [[0 for i in range(len(U))] for j in range(len(U))]
    for i in range(len(U_inverse)):
        U_inverse[i][i] = [[1,1],[1,1]]
    # 创建m下三角矩阵
    m_U = [[0 for i in range(len(U))] for j in range(len(U))]
    for i in range(len(m_U)):
        m_U[i][i] = [[1,1],[1,1]]

    #处理U与U逆，确保U对角线元素为1
    for i in range(len(U)):
        k = U[i][i]
        if FenShu_JiSuan(k) == 1:
            continue
        for j in range(len(U)):
            U[i][j] = FenShu_ChuFa(U[i][j],k)
            U_inverse[i][j] = FenShu_ChuFa(U_inverse[i][j],k)

    # 高斯消去
    for k in range(len(U)):
        for i in range(k + 1, len(U)):
            m_U[k][i] = FenShu_ChuFa(U[k][i], U[i][i])
            for j in range(i, len(U)):
                U[k][j] = FenShu_JianFa(U[k][j], FenShu_ChengFa(m_U[k][i], U[i][j]))
                U_inverse[k][j] = FenShu_JianFa(U_inverse[k][j], FenShu_ChengFa(m_U[k][i], U_inverse[i][j]))
    del m_U

    #a逆 = U逆 L逆
    a_inverse = matrix_ChengFa(U_inverse,L_inverse)
    print("完成")

    return a_inverse