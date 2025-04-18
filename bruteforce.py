import csv
import time

start_time = time.time()

csv_path = "Liste+d'actions+-+P7+Python+-+Feuille+1.csv"
timing_csv_path = "bruteforce_combination_times.csv"

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
        # Enregistrer le temps écoulé depuis le début
        # current_time = time.time() - start_time
        # combination_times.append(current_time)
        return

    bruteforce(index + 1, combination)
    print(index)

    current_cost = sum(action["cost"] for action in combination)
    if current_cost + actions[index]["cost"] <= 500:
        combination.append(actions[index])
        bruteforce(index + 1, combination)
        current_time = time.time() - start_time
        combination_times.append(current_time)

        combination.pop()


def save_combination_times():
    with open(timing_csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['time_elapsed'])

        for i, time_elapsed in enumerate(combination_times):
            writer.writerow([time_elapsed])


def display_best_combination():
    if combinations:
        best_combination = max(
            combinations,
            key=lambda combo: sum(
                action["cost"] * action["profit_rate"] for action in combo
            ),
        )
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
    bruteforce()
    print(f"Nombre de combinaisons avec coût <= 500€: {len(combinations)}")
    display_best_combination()
    end_time = time.time()
    print(f"Temps d'exécution: {end_time - start_time:.2f} secondes")
    save_combination_times()


if __name__ == "__main__":
    main()
