import numpy as np
A = np.zeros((4,4))
i = 0
while i < 4:
    j = 0
    while j < 4:
        if i == j:
            A[i,j] = 1
        else:
            A[i,j] = 0
        j += 1
    i += 1

print(A)
