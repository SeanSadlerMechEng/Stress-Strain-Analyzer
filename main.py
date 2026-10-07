import matplotlib.pyplot as plt 
import numpy as np

from data_analysis import r_squared, calculate_stress_strain, calculate_elastic_region, calculate_youngs_modulus
from plot import plot_graph
from data_read_write import load_data, write_data

def main():
    filename = input("Enter CSV filename including .csv extension: ")
    L_0 = float(input("Enter initial length (mm): "))
    A_cross_section = float(input("Enter initial area (mm^2): "))

    force, extension = load_data(filename)

    strain_x, stress_y = calculate_stress_strain(force, extension, L_0, A_cross_section)

    elastic_strain, elastic_stress = calculate_elastic_region(strain_x, stress_y)

    youngs_modulus = calculate_youngs_modulus(elastic_strain, elastic_stress)

    write_data(strain_x, stress_y, elastic_strain, elastic_stress, youngs_modulus)

    plot_graph(strain_x, stress_y, elastic_strain, elastic_stress)


if __name__ == "__main__":
    main()

