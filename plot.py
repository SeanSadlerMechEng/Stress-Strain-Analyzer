import numpy as np
import matplotlib.pyplot as plt

def plot_graph(strain, stress, elastic_strain, elastic_stress):
    fig = plt.figure()
    plt.title("Stress-Strain Curve")
    plt.plot(strain, stress)
    plt.plot(elastic_strain, elastic_stress, '--', label="Elastic Region")
    plt.xlabel("Strain")
    plt.ylabel("Stress (N/mm^2)")
    plt.legend()
    plt.show()