import tools


def NewtonChaZhi(b,x):
    len0 = len(b[0])
    temp = [[[0] for i in range(len0 + 1)] for j in range(len0)]
    for i in range(len0):
        temp[i][0] = [tools.DaShu_Int_DaShu(b[0][i]),[1,1]]
        temp[i][1] = [tools.DaShu_Int_DaShu(b[1][i]),[1,1]]
    for i in range(2,len0 + 1):
        for j in range(i - 1,len0):
            temp[j][i] = tools.FenShu_ChuFa(tools.FenShu_JianFa(temp[j][i - 1],temp[j -1][i - 1]),(tools.FenShu_JianFa(temp[j][0],temp[j + 1 - i][0])))
    Nx = [[1,1] for i in range(len0)]
    for i in range(0,len0 - 1):
        temp1 = [1]
        for j in range(0,i + 1):
            temp1 = tools.DuoXiangShiChengFa([1, -b[0][j]],temp1)
        Nx[i + 1] = temp1
    res = [0 for i in range(len0)]
    for i in range(0,len0):
        for j in range(0,i + 1):
            # print(Nx[i][j])
            # print(tools.DaShu_Int_DaShu(Nx[i][j]))
            Nx[i][j] = tools.FenShu_ChengFa([tools.DaShu_Int_DaShu(Nx[i][j]),[1,1]],temp[i][i + 1])
            # print(Nx[i][j])
    for i in range(0,len0):
        for j in range(i,len0):
            res[len0 - j + i - 1] += tools.FenShu_JiSuan(Nx[j][i])
    print("Newton插值函数：  ",end="")
    print(tools.DuoXiangShiShuChu(res))
    tools.HuiTu(res,b,"NewtonChaZhi")
    print("Newton插值结果：  ",end="")
    print(tools.DuoXiangShiQiuZhi(res,x))
    # return res