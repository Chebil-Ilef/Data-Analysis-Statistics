import numpy as np
import matplotlib.pyplot as plt


def NormalDist(n,U1,U2):
   # Apply the Box-Muller transformation
   Z1 = np.sqrt(-2 * np.log(U1)) * np.cos(2 * np.pi * U2)
   Z2 = np.sqrt(-2 * np.log(U1)) * np.sin(2 * np.pi * U2)
   return Z1,Z2


# TESTING
# Number of samples
n = 1000
# Generate n pairs of independent Uniform(0, 1) random variables
U1 = np.random.rand(n)
U2 = np.random.rand(n)

# Apply the Box-Muller transformation
Z1, Z2= NormalDist(n,U1,U2)



# Plot the histograms of Z1 and Z2
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(Z1, bins=30, density=True, alpha=0.7, color='b')
plt.title('Z1 ~ N(0, 1)')
plt.subplot(1, 2, 2)
plt.hist(Z2, bins=30, density=True, alpha=0.7, color='r')
plt.title('Z2 ~ N(0, 1)')
plt.show()

