# Parameter M adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
# sum(i, M_i,j) = 1
# Parameter d damping factor (default value 0.85)
# Parameter eps quadratic error for v (default value 1.0e-8)
# Return v, a vector of ranks such that v_i is the i-th rank from [0, 1]

import numpy as np
import matplotlib.pyplot as plt

x = []
x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []
x4 = []
y4 = []
x5 = []
y5 = []

def pagerank(M, eps=1.0e-8, d=0.85):
    ctr = 1
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    last_v = np.ones((N, 1), dtype=np.float32) * 100
    y1.append(v[0][0])
    y2.append(v[1][0])
    y3.append(v[2][0])
    y4.append(v[3][0])
    y5.append(v[4][0])
    x.append(ctr)
    ctr += 1
    while np.linalg.norm(v - last_v, 2) > eps:
        last_v = v
        v = d * np.matmul(M, v) + (1 - d) / N
        print(v)
        print("========================")
        y1.append(v[0][0])
        y2.append(v[1][0])
        y3.append(v[2][0])
        y4.append(v[3][0])
        y5.append(v[4][0])
        x.append(ctr)
        ctr += 1
    return v

M = np.array([[0, 0, 0, 0, 1],
              [0.5, 0, 0, 0, 0],
              [0.5, 0, 0, 0, 0],
              [0, 1, 0.5, 0, 0],
              [0, 0, 0.5, 1, 0]])
v = pagerank(M, 0.001, 0.85)

plt.plot(x, y1, label = "line 1")
plt.plot(x, y2, label = "line 2")
plt.plot(x, y3, label = "line 3")
plt.plot(x, y4, label = "line 4")
plt.plot(x, y5, label = "line 5")
plt.xlabel('Iteration #')
plt.ylabel('PageRank')
plt.title('PageRank by Iteration')
plt.legend()
plt.show()
