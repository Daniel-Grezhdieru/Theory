import math
import scipy.integrate as I
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib import mlab
import cmath
from mpmath import findroot
Eps = 1
p = 13
q = 3
a10 = 0.5
a20 = 1.2
w = 0.68
k = math.pi/2
a11 = math.cos(k)*Eps
a21 = math.sin(k)*Eps
# delta = 0
# Theta = 2*w + Eps*delta
Lambda1 = (a11*cmath.exp(complex(0,-w*p)) + a21*cmath.exp(complex(0,-w*q)))/(1 - a10*p*cmath.exp(complex(0,-w*p)) - a20*q*cmath.exp(complex(0,-w*q)))
Lambda1_ = complex(Lambda1.real,-Lambda1.imag)
# print(Lambda1)
# d1 = Lambda1
# a = 0.1 # > 0.01
# d2 = (a10*w*a*cmath.exp(complex(0,-w*p)))/2*(1 - a10*p*cmath.exp(complex(0,-w*p)) - a20*q*cmath.exp(complex(0,-w*q)))
# print(d2)
# d2_ =  complex(d2.real,-d2.imag)
mod_L1 = Lambda1.real**2 + Lambda1.imag**2
# mod_d2 = d2.real**2 + d2.imag**2
# print(mod_L1, "<", mod_d2)

def dta(a):
    d2 = (a10*w*a*cmath.exp(complex(0,-w*p)))/2*(1 - a10*p*cmath.exp(complex(0,-w*p)) - a20*q*cmath.exp(complex(0,-w*q)))
    mod_d2 = d2.real**2 + d2.imag**2
    a = w**2
    b = complex(0,1) * w*Lambda1_ - complex(0,1) * w*Lambda1
    # print(b)
    # b = complex(0,w*Lambda1_ - w*Lambda1)
    c = mod_L1 - mod_d2
    discriminant = b**2 - 4*a*c
    if discriminant == 0:
        x = -b / (2 * a)
        # print('x = ' + str(x))
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        # print('x₁ = ' + str(x1))
        # print('x₂ = ' + str(x2))
        # print(x1,x2)
        return x1,x2

delta1 = []
delta2 = []
z = 10
for i in range(1, z):
    r = dta(0.1*i)
    delta1.append(r[0].real)
    delta2.append(r[1].real)

A = [i*0.1 for i in range(1,z)]

plt.xlabel("a")
plt.ylabel("delta")
plt.plot(A,delta1,".")
plt.plot(A,delta2,".")
plt.grid()   
# plt.title(" p = {}, q = {}".format(p,q) + ", уравнение 1")
plt.show()