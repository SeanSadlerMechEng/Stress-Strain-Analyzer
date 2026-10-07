import numpy as np

def load_data(filename):
    force = []
    extension = []

    infile = open(filename, "r")

    for line in infile:
        current_line = line.split("\n")
        values = current_line[0].split(",")
        force += [float(values[0])]
        extension += [float(values[1])]

    infile.close()

    return np.array(force), np.array(extension)

def write_data(strain, stress, elastic_strain, elastic_stress, youngs_modulus):

    with open("results.txt", "w") as file:
        file.write("Strain data points:\n")
        file.write(np.array_str(strain) + "\n")
        file.write("--------------------\n")
        file.write("Stress data points:\n")
        file.write(np.array_str(stress) + "\n")
        file.write("--------------------\n")
        file.write("Elastic strain from: " + str(elastic_strain[0]) + " to " + str(elastic_strain[-1]) + "\n")
        file.write("Elastic stress from: " + str(elastic_stress[0]) + " to " + str(elastic_stress[-1]) + "\n")
        file.write("--------------------\n")
        file.write("Young's Modulus: " + str(youngs_modulus))
    return


    