import numpy as np
import time
import random
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_final_corruption(size):
    chars = ['@', '#', '$', '0', '1', 'X', '&', '!']
    for _ in range(25):
        clear_screen()
        print("[ALERTE] INTRUSION TERMINÉE : CONTRÔLE PERDU\n")
        for _ in range(size + 3):
            line = "".join(random.choice(chars) for _ in range(size * 3))
            print(line)
        time.sleep(0.05)


def print_ui(grid, row_hints, col_hints, time_left, total_time, diff_name):
    clear_screen()

    print(f"ZONE : {diff_name}")
    print(f"SÉCURITÉ DU NOYAU : {time_left}s AVANT BRÈCHE\n")

    print("SOMMES COL -> ", end="")
    for c in col_hints:
        print(f"{c} ", end="")
    print("\n" + " " * 14 + "-" * (grid.shape[1] * 3))

    for i in range(grid.shape[0]):
        current_sum = int(np.sum(grid[i]))
        print(f"L{i+1} ({row_hints[i]}) | ", end="")
        for j in range(grid.shape[1]):
            print("■ " if grid[i, j] == 1 else "· ", end="")
        print(f"| [{current_sum}]")