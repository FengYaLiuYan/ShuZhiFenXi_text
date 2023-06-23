import tools

def GaussSanJiaoFenJie(x):
      u = [[0 for i in range(len(x))] for j in range(len(x))]
      l = [[0 for i in range(len(x))] for j in range(len(x))]
      for r in range(0, len(x)):
            for i in range(r, len(x)):
                  sum_lu2 = [[1,0],[1,1]]
                  for k in range(r):
                        sum_lu2 = tools.FenShu_JiaFa(sum_lu2, tools.FenShu_ChengFa(l[r][k], u[k][i]))
                  u[r][i] = tools.FenShu_JianFa([tools.DaShu_Int_DaShu(x[r][i]),[1,1]], sum_lu2)
                  sum_lu3 = [[1,0],[1,1]]
                  for k in range(r):
                        sum_lu3 = tools.FenShu_JiaFa(sum_lu3, tools.FenShu_ChengFa(l[i][k], u[k][r]))
                  l[i][r] = tools.FenShu_ChuFa(tools.FenShu_JianFa([tools.DaShu_Int_DaShu(x[i][r]),[1,1]], sum_lu3), u[r][r])
      # print("U:",u)
      # print("L:",l)

      y = [0 for i in range(len(x))]
      for i in range(0, len(y)):
            sum_lu4 = [[1,0],[1,1]]
            for k in range(i):
                  sum_lu4 = tools.FenShu_JiaFa(sum_lu4, tools.FenShu_ChengFa(l[i][k], y[k]))
            y[i] = tools.FenShu_JianFa([tools.DaShu_Int_DaShu(x[i][len(x[0]) - 1]),[1,1]], sum_lu4)
      # print(y)

      res = [[0, 1] for i in range(len(x))]
      for i in range(0, len(x[0]) - 1):
            sum_lu5 = [[1,0],[1,1]]
            for k in range(len(x) - i, len(x[0]) - 1):
                  sum_lu5 = tools.FenShu_JiaFa(sum_lu5, tools.FenShu_ChengFa(u[len(x[0]) - i - 2][k], res[k]))
            res[len(x[0]) - i - 2] = tools.FenShu_ChuFa(tools.FenShu_JianFa(y[len(x[0]) - i - 2], sum_lu5),
                                                        u[len(x[0]) - i - 2][len(x[0]) - i - 2])
      for i in range(len(res)):
            res[i] = tools.FenShu_JiSuan(res[i])
      print("LU分解方程组结果：", res)
      # for i in range(len(x1)):
      #       for j in range(len(x1[0])):

