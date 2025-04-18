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
            }
        )


best_combination = []


def bruteforce(index=0, current_combination=None):
    global best_combination
    if current_combination is None:
        current_combination = []

    if sum(action["cost"] for action in current_combination) > 500:
        return

    if (
        sum(action["cost"] * action["profit_rate"]
            for action in current_combination)
        >
        sum(action["cost"] * action["profit_rate"]
            for action in best_combination)
    ):
        best_combination = current_combination.copy()

    if index == len(actions):
        return

    bruteforce(index + 1, current_combination)

    current_cost = sum(action["cost"] for action in current_combination)
    if current_cost + actions[index]["cost"] <= 500:
        current_combination.append(actions[index])
        bruteforce(index + 1, current_combination)

        current_combination.pop()


def display_best_combination():
    if best_combination:
        total_cost = sum(action["cost"] for action in best_combination)
        total_profit = sum(
            action["cost"] * action["profit_rate"]
            for action in best_combination
            )*100/total_cost

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
