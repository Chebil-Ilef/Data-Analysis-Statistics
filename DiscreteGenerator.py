import random

def DiscreteGenerator(N, p):
    if sum(p) != 1 or any(x < 0 or x > 1 for x in p):
        raise ValueError("Invalid probabilities. Probabilities should sum to 1 and be in the range [0, 1].")
    
    n = len(p)
    cumulative_probs = [sum(p[:i+1]) for i in range(n)]
    random_numbers = []
    
    for _ in range(N):
        U = random.uniform(0, 1)  # Generate a single uniform random number
        for j in range(n):
            if U < cumulative_probs[j]:
                random_numbers.append(j + 1)
                break
    
    return random_numbers


# Define the probabilities p
p = [0.2, 0.3, 0.4, 0.1]

# Generate 100 random numbers following the specified distribution
random_numbers = DiscreteGenerator(10, p)

# View the generated random numbers
print(random_numbers)
