import tools

def LnxFenMu(b):#用于计算基函数分母
    len0 = len(b[0])
    c = [1.0] * len0
    for i in range(0,len0):
        for j in range(0,len0):
            if i == j or (b[0][i] - b[0][j] == 0):
                continue
            else:
                c[i] /= b[0][i] - b[0][j]
    return c

def LagrangeChaZhi(b,x):
    c = LnxFenMu(b)#计算基函数分母
    len0 = len(b[0])
    Lx = [0 for i in range(len0)]
    for i in range(0,len0):
        if len0 == 2:
            temp1 = [1, -b[0][len0 - 1 - i]]
            Lx[i] = temp1
        else:
            temp1 = [1]
            for j in range(0,len0):
                if i == j:
                    continue
                temp1 = tools.DuoXiangShiChengFa([1, -b[0][j]],temp1)
            Lx[i] = temp1
    for i in range(0,len0):#分母
        for j in range(0,len0):#分子
            Lx[i][j] = Lx[i][j]*c[i]*b[1][i]
    res = [0]*len(Lx[0])
    for i in range(0,len0):#分母
        for j in range(0,len0):#分子
            res[i] += Lx[j][i]
    print("Lagrange插值函数：",end="")
    print(tools.DuoXiangShiShuChu(res))
    print("Lagrange插值结果：",end="")
    print(tools.DuoXiangShiQiuZhi(res,x))
    tools.HuiTu(res,b,"LagrangeChaZhi")
    # return res