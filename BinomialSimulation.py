import random
import matplotlib.pyplot as plt

def Binomial(N, n, p):
    if n < 0 or p < 0 or p > 1:
        raise ValueError("Invalid parameters. n should be non-negative, and p should be in the range [0, 1].")
    
    binomial_numbers = []
    
    for _ in range(N):
        successes = sum(1 if random.uniform(0, 1) < p else 0 for _ in range(n))
        binomial_numbers.append(successes)
    
    return binomial_numbers

# Example usage:
N = 1000  # Number of Binomial random numbers to generate
n = 10    # Number of trials
p = 0.3   # Probability of success

binomial_results = Binomial(N, n, p)

# Create a histogram to visualize the results
plt.hist(binomial_results, bins=range(n+2), align='left', rwidth=0.8)
plt.xticks(range(n+1))
plt.xlabel('Number of Successes')
plt.ylabel('Frequency')
plt.title(f'Binomial Distribution (n={n}, p={p})')
plt.show()
