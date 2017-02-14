import numpy as np
# model is (A, B, pi) where A = Transition probs, B = Emission Probs, pi = initial distribution

# Algorithm Forward Procedure for computing αi(t)
# 1. Base case: αi(0) = A0 i, i = 1..|S|
# 2. Recursion: αj(t) =  |S| αi(t − 1)AijBj xt , j = 1..|S|, t = 1..T i=1

states = [0,1,2]

A = np.array([
        [0.4, 0.3, 0.3],
        [0.3, 0.2, 0.5],
        [0.3, 0.4, 0.3]
    ])

B = np.array([
        [0.8, 0.2],
        [0.5, 0.5],
        [0.6, 0.4]
    ])

pi = np.array([0.33, 0.33, 0.33])

def forward(obs):
    fwd = [{}]
    # Initialize base cases (t == 0)
    for y in states:
        fwd[0][y] = pi[y] * B[y][obs[0]]

    # Run Forward algorithm for t > 0
    for t in range(1, len(obs)):
        fwd.append({})
        for y in states:
            fwd[t][y] = sum((fwd[t-1][y0] * A[y0][y] * B[y][obs[t]]) for y0 in states)

    prob = sum((fwd[len(obs) - 1][s]) for s in states)
    return prob, fwd[len(obs) - 1]
