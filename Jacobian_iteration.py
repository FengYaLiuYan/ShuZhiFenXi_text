import tools

def JingDuPanDuan(res_new,res_old,precision):
    res_new_panduan = []
    res_old_panduan = []
    for i in range(len(res_new)):
        res_new_panduan.append(tools.FenShu_JiSuan(res_new[i]))
        res_old_panduan.append(tools.FenShu_JiSuan(res_old[i]))
    sum_new = 0
    sum_old = 0
    for i in range(len(res_new)):
        sum_new += abs(res_new_panduan[i])
        sum_old += abs(res_old_panduan[i])
    print("差为：", abs(sum_old - sum_new))
    if abs(sum_old - sum_new) < precision:
        return True
    else:
        return False

def Jacobian_iteration(x,initial,precision):
    len_0 = len(x)
    res_new = [[[1,0],[1,1]] for i in range(len_0)]
    res_old = [[tools.DaShu_Int_DaShu(i),[1,1]] for i in initial]

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
                sum = tools.FenShu_JiaFa(sum,tools.FenShu_ChengFa(x[i][j],res_old[j]))
            res_new[i] = tools.FenShu_ChuFa(tools.FenShu_JianFa(x[i][len(x[0]) - 1],sum),x[i][i])
        k += 1
        print("第",k,"次迭代结果：",res_new)
        if JingDuPanDuan(res_new,res_old,precision) or res_new == res_old:
            break
        res_old = [i for i in res_new]

    for i in range(len(res_new)):
        res_new[i] = tools.FenShu_JiSuan(res_new[i])
    return res_new