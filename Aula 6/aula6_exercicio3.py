import numpy as np
import matplotlib.pyplot as plt

def vanlaar(x):
    A12 = 1.6798
    A21 = 0.9227
    gamma = np.zeros(2)
    gamma[0] = np.exp(A12*(1+A12*x[0]/(A21*x[1]))**(-2))
    gamma[1] = np.exp(A21*(1+A21*x[1]/(A12*x[0]))**(-2))
    return gamma

xx = np.arange(0.001,1,0.001)
T = 348.15 # K
NC = 2
xexp = [0, 0.0895, 0.1317, 0.142, 0.154, 0.192, 0.2628, 0.3648, 0.4913, 0.5344, 0.6478, 0.7959, 0.8965, 1]
yexp = [0, 0.4564, 0.5083, 0.5194, 0.5268, 0.553, 0.5768, 0.6054, 0.6532, 0.6739, 0.729, 0.8174, 0.8965, 1]
Pexp = [0.3825,	0.62555, 0.67794, 0.68488, 0.69287, 0.71927, 0.7554, 0.7866, 0.82113, 0.83113, 0.85393, 0.86793, 0.87193, 0.87059] # bar

# Coeficientes de Antoine
A = [5.246770, 5.076800]
B = [1598.673, 1659.793]
C = [-46.4240, -45.8540]

# ELV - Diagrama P-xy
Psat = np.zeros(NC)
for i in [0,1]:
    Psat[i] = 10**(A[i] - B[i]/(T+C[i])) # [bar]

Pi = np.zeros(NC)
P  = np.zeros(np.size(xx))
y  = np.zeros((NC,np.size(xx)))
for i in np.arange(0,np.size(xx),1):
    x = [xx[i], 1-xx[i]]
    gamma = vanlaar(x)
    for j in [0,1]:
        Pi[j] = x[j]*gamma[j]*Psat[j]

    P[i] = np.sum(Pi)
    y[:,i] = Pi/P[i]

plt.plot(xx,P,y[0,:],P)
plt.plot(xexp,Pexp,'bo',yexp,Pexp,'ro')
plt.xlabel('Fração molar $x_1$,$y_1$')
plt.ylabel('Pressão [bar]')
plt.legend(['$x_1$','$y_1$','$x_{exp}$','$y_exp$'])
plt.grid()
plt.show()
