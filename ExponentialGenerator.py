
import numpy as np

def Exponential(N, lam):
    
    random_numbers = np.zeros(N)
    
    for i in range(N):
        U = np.random.uniform(0, 1)  # Generate a single uniform random number
        X = -np.log(1 - U) / lam  # Inverse transform method for Exponential distribution
        random_numbers[i] = X
    
    return random_numbers



# Example usage:
N = 5  # Number of random numbers
lam = 0.5  # Rate parameter

random_numbers= Exponential(N, lam)

# View the generated random numbers
print(random_numbers)


