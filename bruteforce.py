from itertools import combinations
import time
import sys

from utils import parse_csv, display_results


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
    if len(sys.argv) != 3:
        print("The programm needs a csv name and a max cost as only arguments")
        print("Usage: python bruteforce.py <csv_name> <max_cost>")
        sys.exit(1)

    csv_name = sys.argv[1]
    max_cost = float(sys.argv[2])

    start_time = time.time()
    actions = parse_csv(csv_name, optimize=False)
    best_combination = bruteforce(actions, max_cost)
    display_results(best_combination)
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")


if __name__ == "__main__":
    main()
