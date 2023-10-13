import numpy as np
import matplotlib.pyplot as plt

def Exponential(N, lam):
    random_numbers = np.zeros(N)
    
    for i in range(N):
        U = np.random.uniform(0, 1)  # Generate a single uniform random number
        X = -np.log(1 - U) / lam  # Inverse transform method for Exponential distribution
        random_numbers[i] = X
    
    return random_numbers

# Example usage:
N = 1000  # Number of random numbers
lam = 0.5 # Rate parameter

random_numbers = Exponential(N, lam)

# Plot the histogram
plt.hist(random_numbers, bins=30, density=True, rwidth=0.8, label="Histogram")

# Plot the probability density function (PDF) as a red line
x = np.linspace(0, max(random_numbers), 100)
pdf = lam * np.exp(-lam * x)
plt.plot(x, pdf, 'r', lw=2, label="PDF")

plt.title('Exponential Distribution')
plt.xlabel('X')
plt.ylabel('Probability')
plt.legend()
plt.show()
