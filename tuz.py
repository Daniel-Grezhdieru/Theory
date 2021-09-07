import math
import scipy.integrate as I
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
from matplotlib import mlab
import cmath
from mpmath import findroot, quad,inf,exp,fabs
from sympy import Float

def Q(p,alpha,delta): # функция Q
    return I.quad(lambda t: np.exp(-p*t**(1+delta))/t**alpha,0,np.inf)[0]

def R(t,p,alpha,delta): # функция R
    return 1/Q(p,alpha,delta) *  exp(-p*fabs(t)**(1+delta))/fabs(t)**alpha 

def I_R(p,alpha,delta): # интеграл функциии R
    return I.quad(lambda t: R(t,p,alpha,delta),0,np.inf)[0]

print("Integral(R)[0,inf] =",I_R(1,0.25,0.1)) # интеграл примерно равен 1 с погрешностью 10^-14

# def E_c(x,y,p,alpha,delta):
#     return I.quad(lambda t: R(t,p,alpha,delta)*math.exp(-x*t)*math.cos(y*t),0,np.inf)[0]
# def E_s(x,y,p,alpha,delta):
#     return I.quad(lambda t: R(t,p,alpha,delta)*math.exp(-x*t)*math.sin(y*t),0,np.inf)[0]

# def Complex_I(L,p,alpha,delta):
#     x = L.real
#     y = L.imag
#     i1 = I.quad(lambda t: R(t,p,alpha,delta)*np.exp(-x*t)*np.cos(y*t),0,np.inf)[0]
#     print(i1)
#     i2 = I.quad(lambda t: R(t,p,alpha,delta)*np.exp(-x*t)*np.sin(y*t),0,np.inf)[0]
#     return complex(i1,i2)

def characteristic_polynom(p,alpha,delta,omega,mu,a,n): # n = 200, 2000
    x = np.ndarray(n, dtype=np.complex128)
    roots = []
    r_real = []
    r_imag = []
    for i in range(1,n):
        x[i] = complex(0,i*0.1) #0.01 0.1 начальные точки для алгоритма мюллера

    for i in x:
        try:
            a = findroot(lambda L: L**2+a*L+omega**2 *(1 - mu*quad(lambda t: R(t,p,alpha,delta)*exp(L*t),[-inf,0])), i, solver='muller')
            # print(a)
            roots.append(complex(Float(a.real,5),Float(a.imag,5)))
            r_real.append(Float(a.real,5))
            r_imag.append(Float(a.imag,5))
        except: 
            pass

    roots = set(roots)
    for L in roots:
        print(L)

    plt.xlabel("X")
    plt.ylabel("y")
    plt.plot(r_real,r_imag,".")
    plt.grid()   
    # plt.title(" p = {}, q = {}".format(p,q) + ", уравнение 1")
    plt.show()


characteristic_polynom(1,0.25,0.1,1,0.5,1,20) # p,alpha,delta,omega,mu,a,n    n = 20 шаг 0.1 начальные значения 
