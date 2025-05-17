from itertools import combinations
import time

from utils import parse_csv, display_results


csv_path = "datasets/dataset_base.csv"

# tester toutes les combinaisons d 'actions
# chaque action ne peut etre prise qu'une fois
# on ne peut pas dépenser plus de 500€
# on veut maximiser le profit


def bruteforce(actions, max_cost):
    """
    Find the best combination of actions using brute force.
    args:
        actions: list of actions
        max_cost: int, maximum cost
    returns:
        list of actions
    """
    total_combinations = []

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_combinations.append(combination)

    best_combination = max(
            [combo for combo in total_combinations if sum(action["cost"] for action in combo) <= max_cost],
            key=lambda combo: sum(
                action["cost"] * action["profit_rate"] for action in combo
            ),
        )
    return best_combination


def main():
    start_time = time.time()
    actions = parse_csv(csv_path, optimize=False)
    best_combination = bruteforce(actions, 500)
    display_results(best_combination)
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")


if __name__ == "__main__":
    main()
