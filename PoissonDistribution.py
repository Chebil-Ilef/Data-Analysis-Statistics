import numpy as np

def generate_poisson_process(n, lamda):
    events = []
    time = 0
    while len(events) < n:
        time += (-1/lamda) * np.log(1 - np.random.uniform(0, 1))
        events.append(time)
    return events

# Example usage:
n = 5  # Desired number of events
lamda = 2.0  # Rate parameter
result = generate_poisson_process(n, lamda)
print("Generated Poisson process events:", result)
