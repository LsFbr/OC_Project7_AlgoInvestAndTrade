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
                "profit_value": int(row[1]) * int(row[2].split("%")[0]) / 100
                # pré-calcul du profit
            }
        )


def bruteforce():
    max_cost = 500
    best_profit = 0
    best_combination = []

    for r in range(1, len(actions) + 1):
        print(time.time() - start_time)
        for combination in combinations(actions, r):
            total_cost = 0
            total_profit = 0

            for action in combination:
                total_cost += action["cost"]
                if total_cost > max_cost:
                    break
                total_profit += action["profit_value"]

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
    print(f"Profit total: {best_profit:.2f}€")


def main():
    bruteforce()
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")


if __name__ == "__main__":
    main()
