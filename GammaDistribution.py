import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

def my_gamma(n,lambd,N):
    
    # Génération d'échantillons à partir de la loi gamma
    gamma_sample = gamma.rvs(a=n, scale=1/lambd, size=N)  # Adjust scale parameter

    # Tracé de l'histogramme
    plt.hist(gamma_sample, bins=30, density=True, alpha=0.7, color='b', label='Gamma Distribution Histogram')

    # Tracé de la densité de probabilité
    x = np.linspace(0, 20, 400)
    pdf = gamma.pdf(x, a=n, scale=1/lambd)  # Adjust scale parameter
    plt.plot(x, pdf, 'r-', label='PDF')

    plt.xlabel('Valeur')
    plt.ylabel('Densité')
    plt.title('Loi Gamma')
    plt.legend()
    plt.show()  # Add this line to display the plot

# Paramètres de la loi gamma
n = 2  # Paramètre de forme
lambd = 0.5  # Paramètre d'échelle
N=1000

my_gamma(n,lambd,N)
