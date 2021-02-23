import numpy as np

def NRTL(x,T,NC,g,alpha,R):
    tau = np.zeros((NC,NC))
    for i in range(NC):
        for j in range(NC):
            tau[i][j] = g[i][j]/(R*T)
            #G[i][j] = np.exp(-alpha[i][j]*tau[i][j])
    G = np.exp(-alpha*tau)
    num1 = np.zeros(NC)
    den1 = np.zeros(NC)
    num2 = np.zeros(NC)
    num1 = np.zeros(NC)
    den2 = np.zeros(NC)
    num3 = np.zeros(NC)
    den3 = np.zeros(NC)
    lngamma = np.zeros(NC)
    for i in range(NC):
        num1[i] = 0
        den1[i] = 0
        num2[i] = 0
        for j in range(NC):
            num1[i] = num1[i] + tau[j][i]*G[j][i]*x[j]
            den1[i] = den1[i] + G[j][i]*x[j]
            den2[j] = 0
            num3[j] = 0
            den3[j] = 0
            for k in range(NC):
                den2[j] = den2[j] + x[k]*G[k][j]
                num3[j] = num3[j] + x[k]*tau[k][j]*G[k][j]
                den3[j] = den3[j] + x[k]*G[k][j]

            num2[i] = num2[i] + x[j]*G[i][j]/den2[j]*(tau[i][j] - num3[j]/den3[j])

        lngamma[i] = num1[i]/den1[i] + num2[i]

    gamma = np.exp(lngamma)
    return gamma

NC = 3              # Number of components
T  = 342.94;        # Temperature [K]
R  = 1.9872;        # Universal gas constant [cal/(mol.K)]
x  = [0.1, 0.1, 0.8]; # Molar fractions
# Binary interaction parameters matrix
g = np.array([[0.0, 1332.55, 189.11],[-519.89, 0.0, -94.23],[1581.27, 348.01, 0.0]],dtype=float)
# Non-randomness parameters matrix
alpha = np.array([[0.0, 0.284, 0.301],[0.284, 0.0, 0.309],[0.301, 0.309, 0.0]],dtype=float)

gamma = NRTL(x, T, NC, g, alpha, R)
print(gamma)
