import tools

def GaussLieZhuYuan(x):
    # 对方程组处理
    for i in range(len(x)):
        for j in range(len(x[0])):
            x[i][j] = [tools.DaShu_Int_DaShu(x[i][j]),[1,1]]
    # 创建m下三角矩阵
    m = [[0 for i in range(len(x))] for j in range(len(x))]
    for i in range(len(m)):
        m[i][i] = [[1,1],[1,1]]

    # 高斯消去
    for k in range(len(x) - 1):
        # 列主元素选取
        # 存放当前列绝对值最大值
        max_abs = 0
        for i in range(k, len(x)):
            if max_abs < abs(tools.FenShu_JiSuan(x[i][k])):
                # 替换最大值
                max_abs = abs(tools.FenShu_JiSuan(x[i][k]))
                # 交换行
                temp = x[i]
                x[i] = x[k]
                x[k] = temp
        # print("交换：",x)

        # 高斯消去
        for i in range(k + 1, len(x)):
            m[i][k] = tools.FenShu_ChuFa(x[i][k], x[k][k])
            for j in range(k, len(x) + 1):
                x[i][j] = tools.FenShu_JianFa(x[i][j], tools.FenShu_ChengFa(m[i][k], x[k][j]))
        # print("消去",x)

    # 创建结果集
    res = [0 for i in range(len(x))]
    # 求和
    sum_1 = [[1,0],[1,1]]
    # 回代开始
    for i in range(len(res)):
        for j in range(len(res) - i, len(res)):
            # 循环求和
            sum_1 = tools.FenShu_JiaFa(sum_1, tools.FenShu_ChengFa(x[len(res) - i - 1][j], res[j]))
        # 回代计算
        res[len(res) - i - 1] = tools.FenShu_ChuFa(tools.FenShu_JianFa(x[len(res) - i - 1][len(x[0]) - 1], sum_1),
                                                   x[len(res) - i - 1][len(res) - i - 1])
        # 重置求和
        sum_1 = [[1,0],[1,1]]
    # 将分数形式转为小数形式
    for i in range(len(res)):
        res[i] = tools.FenShu_JiSuan(res[i])

    print("m矩阵：", m)
    print("高斯消去完成后增广矩阵：", x)
    print("结果：", res)