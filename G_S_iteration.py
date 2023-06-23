import tools


def JingDuPanDuan(res,temp,precision):
    res_new_panduan = []
    res_old_panduan = []
    for i in range(len(res)):
        res_new_panduan.append(tools.FenShu_JiSuan(res[i]))
        res_old_panduan.append(tools.FenShu_JiSuan(temp[i]))
    sum_new = 0
    sum_old = 0
    for i in range(len(res)):
        sum_new += abs(res_new_panduan[i])
        sum_old += abs(res_old_panduan[i])
    print("差为：", abs(sum_old - sum_new))
    if abs(sum_old - sum_new) < precision:
        return True
    else:
        return False

def G_S_iteration(x,initial,precision):
    len_0 = len(x)
    res = [[[1,0],[1,1]] for i in range(len_0)]
    temp = [[[1,0],[1,1]] for i in initial]

    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] = [tools.DaShu_Int_DaShu(x[i][j]),[1,1]]

    k = 0
    while True:
        for i in range(len_0):
            sum = [[1,0],[1,1]]
            for j in range(len_0):
                if i == j:
                    continue
                sum = tools.FenShu_JiaFa(sum,tools.FenShu_ChengFa(x[i][j],res[j]))
            res[i] = tools.FenShu_ChuFa(tools.FenShu_JianFa(x[i][len(x[0]) - 1],sum),x[i][i])
        k += 1
        print("第",k,"次迭代结果：",res)
        if JingDuPanDuan(res,temp,precision) or res == temp:
            break
        temp = [i for i in res]

    for i in range(len(res)):
        res[i] = tools.FenShu_JiSuan(res[i])
    return res