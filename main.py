# 给定数列，求数列的MAE
import numpy
from numpy import *


def MAE(list):
    sum = 0
    avarge = mean(list)
    for a in list:
        sum += abs(a - avarge)
    return sum / len(list)


def find_answer(list):
    cut = [0,0,0]
    C = MAE(list) * len(list)
    for i in range(1, len(list)):
        listI=list[0:i]
        for j in range(i+1,len(list)):
            listIJ=list[i:j]
            for k in range(j+1,len(list)):
                listJK=list[j:k]
                listK=list[k:len(list)]
                I = MAE(listI) * len(listI)
                IJ = MAE(listIJ) * len(listIJ)
                JK = MAE(listJK) * len(listJK)
                K = MAE(listK) * len(listK)
                All=I+IJ+JK+K
                if (All < C):
                    C = All
                    cut = [i,j,k]
    return cut


a = [-28,1, 12, 11, 4, -3, 4, 7,36]

print(find_answer(a))
print(a[0:find_answer(a)[0]],a[find_answer(a)[0]:find_answer(a)[1]],a[find_answer(a)[1]:find_answer(a)[2]],a[find_answer(a)[2]:len(a)])
#print(b[0:find_answer(b)], " | ", b[find_answer(b):len(b)])
