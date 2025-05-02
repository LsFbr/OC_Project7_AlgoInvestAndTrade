import time

from utils import parse_csv, display_results

csv_path = "datasets/dataset_base.csv"


def knapsack(actions, max_cost):
    """
    Find the best combination of actions using dynamic programming.
    args:
        actions: list of actions
        max_cost: float, maximum cost
    returns:
        list of actions
    """
    for action in actions:
        if action["cost"] <= 0 or action["cost"] > max_cost:
            actions.remove(action)

    actions.sort(key=lambda action: action["profit_value"]/action["cost"], reverse=True)

    # Convert max_cost to an integer by scaling
    scale_factor = 100
    max_cost_int = int(max_cost * scale_factor)

    n = len(actions)
    table = [[0 for _ in range(max_cost_int + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost_i = int(actions[i-1]["cost"] * scale_factor)  # Convert to int
        profit_i = actions[i-1]["profit_value"]
        for w in range(1, max_cost_int + 1):
            if cost_i <= w:
                table[i][w] = max(
                    table[i-1][w],
                    profit_i + table[i-1][w-cost_i]
                )
            else:
                table[i][w] = table[i-1][w]

    # traceback
    best_combination = []
    w = max_cost_int
    for i in range(n, 0, -1):
        if table[i][w] != table[i-1][w]:
            best_combination.append(actions[i-1])
            w -= int(actions[i-1]["cost"] * scale_factor)

    return best_combination


def main():
    start_time = time.time()
    actions = parse_csv(csv_path, optimize=True)
    best_combination = knapsack(actions, 500)
    display_results(best_combination)
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")


if __name__ == "__main__":
    main()
