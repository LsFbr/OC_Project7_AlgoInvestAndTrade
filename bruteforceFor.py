import csv
from itertools import combinations
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
            }
        )

# tester toutes les combinaisons d'actions
# chaque action ne peut etre prise qu'une fois
# on ne peut pas dépenser plus de 500€
# on veut maximiser le profit


def bruteforce():
    max_cost = 500
    best_profit = 0
    best_combination = []

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = sum(action["cost"] for action in combination)
            total_profit = sum(
                action["cost"] * action["profit_rate"]
                for action in combination
            )

            if total_cost <= max_cost and total_profit > best_profit:
                best_profit = total_profit
                best_combination = combination

    print(
        f"meilleure combinaison: "
        f"{[action['name']for action in best_combination]}"
        )
    print(
        f"Coût total: "
        f"{sum(action['cost'] for action in best_combination)}€"
        )
    print(f"Profit total: {best_profit}€")


def main():
    bruteforce()
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")


if __name__ == "__main__":
    main()
