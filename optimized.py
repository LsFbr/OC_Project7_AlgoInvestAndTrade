import csv
import time

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
                # on pré-calcule le profit pour éviter de le recalculer
                # à chaque étape de la recursion
            }
        )

best_combination = []
best_profit = 0
MAX_COST = 500


def bruteforce(
        index=0,
        current_combination=[],
        current_cost=0,
        current_profit=0
        ):
    global best_combination, best_profit

    if current_cost > MAX_COST:
        return

    if current_profit > best_profit:
        best_profit = current_profit
        best_combination = current_combination.copy()
        # on sauvegarde la combinaison trouvée
        # seulement si elle est meilleure que la précédente

    if index == len(actions):
        return

    bruteforce(index + 1, current_combination, current_cost, current_profit)

    if current_cost + actions[index]["cost"] <= MAX_COST:
        current_combination.append(actions[index])
        bruteforce(
            index + 1,
            current_combination,
            current_cost + actions[index]["cost"],
            current_profit + actions[index]["profit_value"]
        )
        current_combination.pop()


def display_best_combination():
    if best_combination:
        total_cost = sum(action["cost"] for action in best_combination)
        total_profit = sum(
            action["cost"] * action["profit_rate"]
            for action in best_combination
            )*100/total_cost if total_cost > 0 else 0

        print(f"Meilleure combinaison: "
              f"{[action['name'] for action in best_combination]}"
              )
        print(f"Coût total: {total_cost}€")
        print(f"Profit total: {total_profit:.2f}%")


def main():
    start_time = time.time()
    bruteforce()
    display_best_combination()
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")


if __name__ == "__main__":
    main()
