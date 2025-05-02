from itertools import combinations
import time

from utils import parse_csv

csv_path = "data/dataset_base.csv"


def bruteforce(actions, max_cost):
    # pré-calcul du profit (gain de temps : 0.2s)
    for action in actions:
        action["profit_value"] = action["cost"] * action["profit_rate"]

    # trie les actions par ratio profit/coût décroissant (gain de temps : 0.02s)
    actions.sort(key=lambda action: action["profit_value"]/action["cost"], reverse=True)

    best_profit = 0
    best_combination = []

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = 0
            total_profit = 0

            # Elimine les combinaisons qui dépassent le coût maximum (gain de temps : 0.68s)
            for action in combination:
                total_cost += action["cost"]
                if total_cost > max_cost:
                    break
                total_profit += action["profit_value"]

            if total_cost <= max_cost and total_profit > best_profit:
                best_profit = total_profit
                best_combination = combination

    total_profit_rate = best_profit*100/total_cost

    print(f"meilleure combinaison: {[action['name']for action in best_combination]}")
    print(f"Coût total: {sum(action['cost'] for action in best_combination)}€")
    print(f"Profit total: {total_profit_rate:.2f}% ({best_profit:.2f}€)")


def main():
    start_time = time.time()
    actions = parse_csv(csv_path, optimize=True)
    bruteforce(actions, 500)
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")


if __name__ == "__main__":
    main()
