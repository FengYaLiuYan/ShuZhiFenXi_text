import numpy
import time
import tools
import random

from ShuZhiFenXi import LagrangeChaZhi,NewtonChaZhi,GaussXiaoQu,GaussLieZhuYuan,GaussSanJiaoFenJie,Jacobian_iteration,G_S_iteration,Dichotomy

# bianjie.fenkuai()

#第一个中括号为x分量，第二个中括号为y分量
# b0 = [[5],[3]]
# b1 = [[1,0],[0,1]]
# b2 = [[1,2,4],[3,2,1]]
# b3 = [[1,-2,3,4],[10,-5,3,-2]]
# b4 = [[-2,-1,1,2,5],[-4,3,1,-3,6]]
# b22 = [[1,2,3],[2,4,6]]
# b=[[0,2,3,5],[1,-3,-4,2]]
# x = 0.54

# LagrangeChaZhi.LagrangeChaZhi(b,x)
# print()
# print(numpy.polyfit(b[0],b[1],2,full = False))

# NewtonChaZhi.NewtonChaZhi(b,x)

# x1 = [[ 5,-4, 1, 2],
#       [-4, 6,-4,-1],
#       [ 1,-4, 6,-1]]
# x2 = [[ 1, 1, 1, 6],
#       [ 1, 3,-2, 1],
#       [ 2,-2, 1, 1]]
# x3 = [[0.01,1,1],
#       [1,2,1]]
# x4 = [[ 0.001,2.000,3.000,1.000],
#       [-1.000,3.712,4.623,2.000],
#       [-2.000,1.072,5.643,3.000]]
# x5 = [[3,1,1,345,8,679,35,756,7897,25,867,978,576],
#       [1,37,91,20,53,16,93,72,30,60,93,53,87],
#       [52,19,42,6,98,58,87,17,40,30,22,92,47],
#       [62,20,85,85,51,5,51,89,52,32,22,38,18],
#       [24,58,23,42,53,34,2,92,26,6,80,53,33],
#       [37,9,21,28,74,80,53,12,52,93,75,89,72],
#       [32,75,65,38,81,64,82,88,1,23,5,23,30],
#       [23,56,41,61,88,93,41,96,83,80,98,8,2],
#       [51,69,49,10,69,28,54,47,39,35,21,20,53],
#       [38,28,79,20,16,18,77,33,89,67,61,80,99],
#       [51,5,30,58,71,72,33,93,36,79,2,29,47],
#       [60,39,60,40,20,19,62,42,53,70,25,90,72]]
# x6 = [[1,2,3,14],
#       [2,5,2,18],
#       [3,1,5,20]]

# GaussXiaoQu.GaussXiaoQu(x6)
# GaussLieZhuYuan.GaussLieZhuYuan(x6)
# GaussSanJiaoFenJie.GaussSanJiaoFenJie(x6)
# x_0 = numpy.array(x5)
# x = [[0 for j in range(len(x5[0]))] for i in range(len(x5))]
# for i in range(len(x_0)):
#       for j in range(len(x_0[0])):
#             x[i][j] = x_0[i,j]
#
# run_time = 0
# times = 0
# for i in range(10):
#       times += 1
#       for i in range(len(x_0)):
#             for j in range(len(x_0[0])):
#                   x[i][j] = x_0[i, j]
#       start_time = time.time()  # 程序开始时间
#
#       GaussXiaoQu.GaussXiaoQu(x)
#       # GaussLieZhuYuan.GaussLieZhuYuan(x)
#       # GaussSanJiaoFenJie.GaussSanJiaoFenJie(x)
#
#       end_time = time.time()  # 程序结束时间
#       run_time += (end_time - start_time)  # 程序的运行时间，单位为秒
# print("time cost:", float(run_time/times) * 1000.0, "ms")

# x7 = [[8,-1, 1, 8],
#       [2,10,-1,11],
#       [1, 1,-5,-3]]
# initial = [0,0,0]
# precision = 10e-3

#
# x_0 = numpy.array(x7)
# x = [[0 for j in range(len(x7[0]))] for i in range(len(x7))]
# for i in range(len(x_0)):
#       for j in range(len(x_0[0])):
#             x[i][j] = x_0[i,j]
#
# print(Jacobian_iteration.Jacobian_iteration(x7,initial,precision))
# print("——————————————")
# print(G_S_iteration.G_S_iteration(x7,initial,precision))

x = [1,1,-3,-3]
precision = 1e-6
a = 1
b = 2

# precision = 1e-6
# x = [1,1,-3,-3]
# a = 1.0
# b = 2.0
#
print("该区间上根迭代结果:",Dichotomy.Dichotomy(x,precision,a,b))
