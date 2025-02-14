import pyvista as pv

def plot_pv(arrays, colors, point_size=5):
    """
    Función para plotear múltiples arreglos de puntos en PyVista.

    Parámetros:
    - arrays: Lista de arreglos de puntos.
    - colors: Lista de colores correspondientes a cada arreglo.
    - point_size: Tamaño de los puntos (por defecto es 5).
    """
    plotter = pv.Plotter()

    for array, color in zip(arrays, colors):
        polydata = pv.PolyData(array)
        plotter.add_points(polydata, color=color, point_size=point_size)

    plotter.show()