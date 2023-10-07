import random
import matplotlib.pyplot as plt

def Bernoulli(n, p):
    results = [1 if random.uniform(0, 1) < p else 0 for _ in range(n)]
    return results

# Example usage:
p = 0.3  # Probability of success
n = 1000  # Number of trials

results = Bernoulli(n, p)

# Create a histogram to visualize the results
plt.hist(results, bins=[0,1,2], align='left', rwidth=0.5)
plt.xticks([0, 1])
plt.xlabel('Outcome')
plt.ylabel('Frequency')
plt.title('Bernoulli Trials Histogram')
plt.show()
