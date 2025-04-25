import csv
import time

start_time = time.time()

csv_path = "Liste+d'actions+-+P7+Python+-+Feuille+1.csv"

actions = []

with open(csv_path, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        actions.append(
            {
                "name": row[0],
                "cost": int(row[1]),
                "profit_rate": int(row[2].split("%")[0]) / 100,
                "profit_value": int(row[1]) * int(row[2].split("%")[0]) / 100
            }
        )


def knapsack(actions, max_cost):
    n = len(actions)
    table = [[0 for _ in range(max_cost + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost_i = actions[i-1]["cost"]
        profit_i = actions[i-1]["profit_value"]
        for w in range(1, max_cost + 1):
            if cost_i <= w:
                table[i][w] = max(
                    table[i-1][w],
                    profit_i + table[i-1][w-cost_i]
                    )
            else:
                table[i][w] = table[i-1][w]

    return table


def traceback(table, actions, max_cost):
    n = len(actions)
    w = max_cost
    best_combination = []
    for i in range(n, 0, -1):
        if table[i][w] != table[i-1][w]:
            best_combination.append(actions[i-1])
            w -= actions[i-1]["cost"]

    return best_combination


def display_results(best_combination):
    total_cost = sum(action["cost"] for action in best_combination)
    total_profit = sum(action["profit_value"] for action in best_combination)
    total_profit_rate = total_profit*100/total_cost

    print(f"Meilleure combinaison: {[action['name'] for action in best_combination]}")
    print(f"Coût total: {total_cost}€")
    print(f"Profit total: {total_profit_rate:.2f}% ({total_profit}€)")
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")


def main():
    max_cost = 500
    table = knapsack(actions, max_cost)
    best_combination = traceback(table, actions, max_cost)
    display_results(best_combination)


if __name__ == "__main__":
    main()
