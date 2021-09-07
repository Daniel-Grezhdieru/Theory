import math
import scipy.integrate as I
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib import mlab

Eps = 1
p = 10
q = 1
a1 = 1.23
a2 = 1.05
w = 1.54

def a1(w):
    a1 = (-math.sin(p*w) - Eps*w*math.cos(p*w)) / math.sin((p-q)*w)
    return a1
def a2(w):
    a2 = (Eps*w*math.cos(q*w) + math.sin(q*w)) / math.sin((p-q)*w)
    return a2
def func(w):
    a = -a2(w) - 1
    return a


wlist = np.linspace(0, 3.15, 20000)
# for w in wlist:
#     # print(func(w),w)
#     if a1(w) <= 1 and a1(w) >= 0.8:
#         print(a1(w),a2(w),w)


a1_list_1=[a1(w) for w in wlist]
# a1_list_2=[a1_2(w) for w in wlist]
a2_list_2=[a2(w) for w in wlist]
func_list_1=[func(w) for w in wlist]
# func_list_2=[a1_3(w) for w in wlist]
plt.plot(a1_list_1, a2_list_2, 'b,')
# plt.plot(a1_list_1, a2_list_2, 'b,')
plt.plot(func_list_1, a2_list_2, 'b,')
# plt.plot(a1_list_2, a2_list_2, 'g,')
# plt.plot(func_list_2, a2_list_2, 'g,')
plt.xlabel('a1')
plt.ylabel('a2')
plt.xlim([-5,5])
plt.ylim([-5,5])
plt.grid()
plt.show()