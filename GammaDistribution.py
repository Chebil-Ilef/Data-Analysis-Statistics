import numpy as np

def Gamma(N, n, lam):
    if n <= 0 or lam <= 0:
        raise ValueError("Invalid parameters. n and lambda should be greater than 0.")
    
    random_numbers = np.random.gamma(shape=n, scale=1/lam, size=N)
    
    return random_numbers

test = Gamma(5, 3, 0.5)
print(test)

