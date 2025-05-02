import csv
import time

start_time = time.time()

csv_path = "data/dataset_base.csv"

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


combinations = []
combination_times = []  # Pour stocker les temps de chaque combinaison


def bruteforce(index=0, combination=None):
    if combination is None:
        combination = []

    if (
        index == len(actions)
        and sum(action["cost"] for action in combination) <= 500
    ):
        combinations.append(combination.copy())
        return

    bruteforce(index + 1, combination)

    current_cost = sum(action["cost"] for action in combination)
    if current_cost + actions[index]["cost"] <= 500:
        combination.append(actions[index])
        bruteforce(index + 1, combination)
        current_time = time.time() - start_time
        combination_times.append(current_time)

        combination.pop()


def display_results():
    if combinations:
        best_combination = max(
            combinations,
            key=lambda combo: sum(
                action["cost"] * action["profit_rate"] for action in combo
            ),
        )
        total_cost = sum(action["cost"] for action in best_combination)
        total_profit = sum(action["cost"] * action["profit_rate"] for action in best_combination)
        total_profit_rate = total_profit*100/total_cost

        print(f"Meilleure combinaison: {[action['name'] for action in best_combination]}")
        print(f"Coût total: {total_cost}€")
        print(f"Profit total: {total_profit_rate:.2f}% ({total_profit}€)")


def main():
    bruteforce()
    print(f"Nombre de combinaisons avec coût <= 500€: {len(combinations)}")
    display_results()
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")


if __name__ == "__main__":
    main()
