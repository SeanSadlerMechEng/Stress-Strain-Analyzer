import numpy as np

def r_squared(x_values, y_values) -> float:
    coefficients = np.polyfit(x_values, y_values, 1)
    fitted_curve = np.polyval(coefficients, x_values)

    residual_ss = np.sum((y_values - fitted_curve) ** 2)
    total_ss = np.sum((y_values - np.mean(y_values)) ** 2)

    return 1 - residual_ss / total_ss

def calculate_stress_strain(force, extension, length, area) -> list[float]:
    strain = extension / length
    stress = force / area

    return strain, stress

def calculate_elastic_region(strain, stress):
    end_index = 5
    for i in range(5, len(strain)):
        x_linear = strain[:i]
        y_linear = stress[:i]

        r2 = r_squared(np.array(x_linear), np.array(y_linear))

        if r2 < 0.995:
            end_index = i - 2
            break

    elastic_strain = strain[:end_index]
    elastic_stress = stress[:end_index]

    return elastic_strain, elastic_stress

def calculate_youngs_modulus(elastic_strain, elastic_stress):
    E = (elastic_stress[0] - elastic_stress[-1]) / (elastic_strain[0] - elastic_strain[-1])
    
    return E
