import time
import matplotlib.pyplot as plt
from utils import parse_csv
from bruteforce import bruteforce
from optimized import knapsack

csv_name = "dataset_base.csv"


def measure_time(func, actions, max_cost):
    start_time = time.time()
    func(actions, max_cost)
    end_time = time.time()
    return end_time - start_time


def main():
    max_cost = 500
    action_not_optimized_counts = []
    action_optimized_counts = []
    bruteforce_times = []
    optimized_times = []

    # Charger les actions depuis le CSV
    actions_optimized = parse_csv(csv_name, optimized=True)
    actions_not_optimized = parse_csv(csv_name, optimized=False)

    # Tester pour différentes tailles de listes d'actions
    for i in range(1, len(actions_not_optimized) + 1):
        subset_actions = actions_not_optimized[:i]
        action_not_optimized_counts.append(i)

        # Mesurer le temps pour bruteforce
        bruteforce_time = measure_time(bruteforce, subset_actions, max_cost)
        bruteforce_times.append(bruteforce_time)

    for i in range(1, len(actions_optimized) + 1):
        subset_actions = actions_optimized[:i]
        action_optimized_counts.append(i)
        # Mesurer le temps pour knapsack
        optimized_time = measure_time(knapsack, subset_actions, max_cost)
        optimized_times.append(optimized_time)

    # Tracer les résultats
    plt.figure(figsize=(7, 7))
    plt.plot(action_not_optimized_counts, bruteforce_times, label='Bruteforce', marker='o')
    plt.plot(action_optimized_counts, optimized_times, label='Optimized', marker='x')
    plt.xticks(range(0, len(actions_not_optimized) + 1))
    plt.xlabel('Nombre d\'actions')
    plt.ylabel('Temps d\'exécution (secondes)')
    plt.title('Comparaison de la complexité temporelle')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
