import numpy as np
import matplotlib.pyplot as plt
import math

def gen_sn(n):
    path = np.random.standard_normal(n)
    return path

def gen_path(parameter):
    P = parameter['P']
    sigma = parameter['sigma']
    I = parameter['I']
    r = parameter['r']
    T = parameter['T']
    X0 = parameter['X0']
    dt = T / P
    path = np.zeros((P + 1, I))
    path[0] = X0
    for i in range(1, P + 1):
        path[i] = path[i - 1] * np.exp(
            (r - 0.5 * sigma ** 2) * dt + sigma * math.sqrt(dt) * gen_sn(I))
    return path


parameter_r = {'sigma': 0.2, 'P': 100, 'T': 1.0, 'X0': 1.0, 'r': 0.01, 'I': 5}

if __name__ == '__main__':
    path1 = gen_path(parameter_r)
    fig, ax = plt.subplots()
    ax.plot(np.linspace(0, 1., parameter_r['P']+1), path1)
    pass
plt.show()
    


