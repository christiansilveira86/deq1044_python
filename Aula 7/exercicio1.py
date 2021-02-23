import numpy as np
from scipy.optimize import newton
def circ(I,V,R):
    f1 = R[0]*I[0] + R[3]*I[0] - R[3]*I[1] - V[0]
    f2 = -R[3]*I[0] + R[1]*I[1] + R[3]*I[1] + R[4]*I[1] - R[4]*I[2]
    f3 = -R[4]*I[1] + R[2]*I[2] + R[4]*I[2] + V[1]
    return [f1, f2, f3]
    
V = [10, 5]
R = [1, 2, 3, 4, 5]
I0 = [1, 1, 1]
I = newton(circ, I0, args=[V,R])
print(I)
