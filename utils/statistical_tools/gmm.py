import numpy as np
from sklearn.mixture import GaussianMixture

def get_neighborhood(kdtree, point_idx, radius):
    indices = kdtree.query_radius([kdtree.data[point_idx]], r=radius)
    return indices[0]

def automatic_gmm_components(data, max_components=2, criterion='aic', T=0.3, **kwargs):
    n_components_range = range(1, max_components + 1)
    criterions, means = [], []
    if criterion not in ['aic', 'bic']:
        raise ValueError("Criterio no válido. Usa 'bic' o 'aic'.")
    
    for n in n_components_range:
        try:
            gmm = GaussianMixture(n_components=n, **kwargs)
            gmm.fit(data)
            criterions.append(gmm.bic(data)) if criterion == 'bic' else criterions.append(gmm.aic(data))
            means.append(gmm.means_)
            
        except ValueError as e:
            print(f"Error fitting GMM with {n} components: {e}")
            break

    optimal_idx = np.argmin(criterions)
    optimal_means = means[optimal_idx]
    optimal_components = n_components_range[optimal_idx]
    
    if optimal_components == 2 and abs(optimal_means[0] - optimal_means[1]) <= T:
       return 1, [np.mean(optimal_means, dtype=np.float32)]
    
    if not criterions:
        return 1, [np.mean(data, dtype=np.float32)]  # Si no se pudo ajustar ningún modelo, devolver 1 componente
    
    return optimal_components, means[optimal_idx]