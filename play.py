import time
import numpy as np

from ui import print_ui, show_final_corruption
from solver import solve_with_numpy_step_by_step


def get_difficulty():
    levels = {
        "1": (5, 0.35, 90, "Périmètre Réseau"),
        "2": (6, 0.40, 75, "Proxy Défensif"),
        "3": (7, 0.45, 60, "Noeud Central"),
        "4": (8, 0.50, 50, "Noyau Chiffré"),
        "5": (9, 0.55, 40, "Zone Critique")
    }

    while True:
        print("-------------------------------------------------------")
        print("ID   | ZONE CRITIQUE             | TAILLE   | DÉLAI")
        print("-------------------------------------------------------")
        print("[1]  | Périmètre Réseau          | 5x5      | 90s")
        print("[2]  | Proxy Défensif            | 6x6      | 75s")
        print("[3]  | Noeud Central             | 7x7      | 60s")
        print("[4]  | Noyau Chiffré             | 8x8      | 50s")
        print("[5]  | Zone Critique             | 9x9      | 40s")
        print("-------------------------------------------------------")

        choice = input("Choisissez un niveau (1-5) : ").strip()
        if choice in levels:
            break
        print("Choix invalide.\n")

    while True:
        mode = input("Mode de jeu [1] Manuel [2] IA : ").strip()
        if mode in ("1", "2"):
            break
        print("Choix invalide.\n")

    size, density, total_time, zone_name = levels[choice]
    is_bot_mode = (mode == "2")

    return size, density, total_time, zone_name, is_bot_mode


def play():
    size, density, total_time, diff_name, is_bot_mode = get_difficulty()

    solution = (np.random.rand(size, size) < density).astype(int)
    row_hints = solution.sum(axis=1)
    col_hints = solution.sum(axis=0)

    player_grid = np.zeros((size, size), dtype=int)
    start_time = time.time()

    if is_bot_mode:
        bot_grid = solve_with_numpy_step_by_step(size, row_hints, col_hints)
        print_ui(bot_grid, row_hints, col_hints, total_time, total_time, diff_name)
        print("\nSolution IA affichée.")
        return

    while True:
        elapsed = int(time.time() - start_time)
        time_left = total_time - elapsed

        if time_left <= 0:
            show_final_corruption(size)
            print("\nÉchec : le système a été corrompu.")
            break

        print_ui(player_grid, row_hints, col_hints, time_left, total_time, diff_name)

        if np.array_equal(player_grid, solution):
            print("\nSuccès : menace neutralisée.")
            break

        user_input = input("\nEntrer ligne,colonne (ex: 2,3) ou q pour quitter : ").strip()

        if user_input.lower() == "q":
            print("Session terminée.")
            break

        try:
            row, col = map(int, user_input.split(","))
            row -= 1
            col -= 1

            if 0 <= row < size and 0 <= col < size:
                player_grid[row, col] = 1 - player_grid[row, col]
            else:
                input("Coordonnées hors grille. Entrée pour continuer...")
        except:
            input("Entrée invalide. Entrée pour continuer...")