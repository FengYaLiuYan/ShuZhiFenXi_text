import os
import random

import numpy as np
from matplotlib import pyplot as plt
import time
import tools
from coptpy import *

# x = np.arange(-10,10,0.01)
# b = [[1,-2,3,4],[10,-5,3,-2]]#第一个中括号为x分量，第二个中括号为y分量
# #y = -0.08333333*x*x*x + 0.75000000x^2 - 1.66666667x^1 + 1.00000000
# y = -5.920*np.power(x,3)+11.160*np.power(x,2)+33.920*x-29.160
# for i in range(0, len(b[0])):
#     plt.scatter(b[0][i], b[1][i])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.plot(x, y)
# plt.show()
#
# print(np.power(2,3))


# x = [i for i in range(10)]
# y = [i*2 for i in range(10)]
#
# plt.ion()
# plt.figure()
#
# for i in range(10):
# 	plt.scatter(x[i], y[i])
# 	plt.pause(0.1)
# plt.ioff()
# plt.show()


# bk = [1,2,3]
# #区间
# a = 0
# b = 1
# #k阶导
# k = 3

# print("原函数：" + tools.DuoXiangShiShuChu(bk))
# print("求{:d}阶导后：{:s}".format(k,tools.DuoXiangShiShuChu(tools.DuoXiangShiQiuDao(bk,k))))
# print("在[{:d},{:d}]区间上积分后得：{:.8f}".format(a,b,tools.DuoXiangShiDingJiFen(bk,a,b)))

# Create COPT environment
# env = Envr()
#
# # create model
# model = env.createModel("LP example")
#
# # create variables
# x1 = model.addVar(lb=0, ub=COPT.INFINITY, vtype = COPT.CONTINUOUS, name="x1")
# x2 = model.addVar(lb=0, ub=COPT.INFINITY, vtype = COPT.CONTINUOUS, name="x2")
#
# # create objective
# model.setObjective(8*x1 + 5*x2, sense=COPT.MAXIMIZE)
#
# # create constraints
# model.addConstr(x1 + x2 <= 6)
# model.addConstr(9*x1 + 5*x2 <= 45)
#
# # solve and output the optimal solution
# model.solve()
#
# print("Objective value: {}".format(model.objval))
# print("Variable solution:")
#
# for var in model.getVars():
#     print(" x[{0}]: {1}".format(var.index, var.x))

# print(tools.FenShu_JiaFa([2,6],[1,3]))

# a = [[[1,1],[0,1]],
#      [[0,1],[1,1]]]
# b = [[[7,1],[3,1]],
#      [[9,1],[2,1]]]
# c = [[1,2,3],
#      [4,5,6]]
# d = [[4,2],
#      [3,2]]
# e = [[0,1,1,1],
#      [1,0,1,1],
#      [1,1,0,1],
#      [1,1,1,0]]
# f = [[1,-1,1],
#      [1,1,3],
#      [2,-3,2]]

# print(tools.matrix_JiaFa(a,b))
# print(tools.matrix_JianFa(a,b))
# print(tools.matrix_ChengFa(b,c))

# print(os.getcwd())
# print(os.listdir())
#[[-81,-98,-76,-4,29],[-38,-77,-72,27,44],[-18,57,-2,8,92],[87,27,-32,69,-31],[33,-93,-74,99,67]]
#[[-67,60,-44,-48,43,10],[22,-95,24,77,25,-16],[14,-20,65,9,94,-9],[16,-25,86,31,12,-50],[9,51,20,-50,-2,-22],[99,76,-61,-80,50,45]]
#[[10,-85,29,-9,-8,77,-39,20,88,81],[-28,54,-50,-84,-43,-9,25,-64,-53,-52],[-70,37,91,-12,21,74,33,71,-20,-49],[-3,3,71,65,-59,83,-65,-87,62,52],[32,34,-64,7,5,57,-82,-96,-70,-18],[53,72,36,59,-94,-97,12,-80,55,-52],[24,30,-1,-22,-74,-13,47,-27,-17,26],[-88,-67,57,-58,28,10,-6,-48,24,37],[44,14,-96,82,33,-65,2,28,-55,31],[6,34,-41,-18,-73,-80,40,10,65,-15]]
a = [[10,-85,29,-9,-8,77,-39,20,88,81],[-28,54,-50,-84,-43,-9,25,-64,-53,-52],[-70,37,91,-12,21,74,33,71,-20,-49],[-3,3,71,65,-59,83,-65,-87,62,52],[32,34,-64,7,5,57,-82,-96,-70,-18],[53,72,36,59,-94,-97,12,-80,55,-52],[24,30,-1,-22,-74,-13,47,-27,-17,26],[-88,-67,57,-58,28,10,-6,-48,24,37],[44,14,-96,82,33,-65,2,28,-55,31],[6,34,-41,-18,-73,-80,40,10,65,-15]]

# print(tools.matrix_num_ChengFa(a,3))
# print(tools.matrix_ZhuanZhi(a))

start_time = time.time()
a_inverse = tools.matrix_QiuNi_LU(a)
print("------")
a_cheng1 = tools.matrix_ChengFa(a,a_inverse)
a_cheng2 = tools.matrix_ChengFa(a_inverse,a)
end_time = time.time()
print(a_inverse)
print(a_cheng1)
print(a_cheng2)
elapsed_time = end_time - start_time
print("代码运行时间为：", elapsed_time, "秒")
# print()
# for i in range(len(a_inverse[0])):
#      for j in range(len(a_inverse)):
#           a_inverse[i][j] = tools.FenShu_JiSuan(a_inverse[i][j])
#           a_cheng1[i][j] = tools.FenShu_JiSuan(a_cheng1[i][j])
#           a_cheng2[i][j] = tools.FenShu_JiSuan(a_cheng2[i][j])
# print(a_inverse)
# print(a_cheng1)
# print(a_cheng2)

#[1,5,3,6,7,4,6,7,7]#=53674677
#[-1,7,3,3,9,7,6,5]#=-7339765

def SuiJiShengCheng_DaShu():
    a = []
    b = []
    len_a = random.randint(3, 5)
    len_b = random.randint(1, 3)
    sym = [-1, 1]
    a.append(random.choice(sym))
    a.append(random.randint(1, 9))
    for i in range(len_a):
        a.append(random.randint(0, 9))
    b.append(random.choice(sym))
    b.append(random.randint(1, 9))
    for j in range(len_b):
        b.append(random.randint(0, 9))
    return a,b

# a,b = SuiJiShengCheng_DaShu()

# a = [1, 1, 6, 1, 5, 6, 8]
# b = [-1, 3, 1, 3, 6]
# a =[1,1]
# b =[1,3]

# a1 = [1,1,0,1,2]
# a2 = [1,1,0,1,2]
# a3 = [1,2,2]
#
# print(a[:-3])
# print(a1[:-2])
# print(a2[:-1])
# print(a3[:None])

# print(a)
# print(b)
# a_int = tools.DaShu_DaShu_Int(a)
# b_int = tools.DaShu_DaShu_Int(b)
# print(a_int)
# print(b_int)
# print(a_int//b_int)

# print(tools.DaShu_JiaFa(a,b))
# print(tools.DaShu_JianFa(a,b))
# print(tools.DaShu_ChengFa(a,b))
# print(tools.DaShu_ChuFa(a,b))
# print(tools.DaShu_ChuYu(a,b))

# a = [[1, 1,2,0,1,2],[1,1]]
# b = [[1, 1,1],[1,1]]
# print(tools.FenShu_JiaFa(a,b))
