import numpy as np
import time

#SYS = Système
def solve_with_numpy_step_by_step(size, row_hints, col_hints):
    print("\033[94m[SYS] Initialisation du solveur matriciel...\033[0m")
    time.sleep(0.5)

    num_equations = 2 * size
    num_variables = size * size

    A = np.zeros((num_equations, num_variables), dtype=int)

    # Contraintes des lignes
    for i in range(size):
        for j in range(size):
            A[i, i * size + j] = 1

    # Contraintes des colonnes
    for j in range(size):
        for i in range(size):
            A[size + j, i * size + j] = 1

    B = np.concatenate((row_hints, col_hints))

    print("\033[93m[SYS] Résolution avec np.linalg.lstsq()...\033[0m")
    time.sleep(0.5)

    x, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)

    result = np.round(np.clip(x.reshape((size, size)), 0, 1)).astype(int)

    print("\033[92m[OK] Solution générée.\033[0m")
    time.sleep(1)

    return result