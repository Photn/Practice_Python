import numpy as np
import math

def gen_sn(n):
    path = np.random.standard_normal(n)
    path = (path - np.mean(path)) / np.std(path)
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


parameter_r = {'sigma': 0.2, 'P': 252*2, 'T': 2.0, 'X0': 100.0, 'r': 0.01, 'I': 100}

if __name__ == '__main__':
    path1 = gen_path(parameter_r)
    print(path1)


