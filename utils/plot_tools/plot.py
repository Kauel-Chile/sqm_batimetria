import numpy as np
import matplotlib.pyplot as plt

def plot_gmm(z, gmm):
    
    # Generar los valores de la curva ajustada
    x = np.linspace(z.min(), z.max(), 1000).reshape(-1, 1)
    logprob = gmm.score_samples(x)
    pdf = np.exp(logprob)

    # Graficar el histograma y la curva ajustada
    plt.hist(z, bins=50, color='red', alpha=0.7, density=True, label='Histogram')

    # Graficar la curva total de la GMM
    plt.plot(x, pdf, color='blue', lw=2, label='GMM')

    plt.xlabel('z')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

