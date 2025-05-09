import matplotlib.pyplot as plt
from memory_profiler import memory_usage
from utils import parse_csv
from bruteforce import bruteforce
from optimized import knapsack

csv_path = "datasets/dataset_base.csv"


def measure_memory(func, actions, max_cost):
    mem_usage = memory_usage((func, (actions, max_cost)), interval=0.01)
    return max(mem_usage) - min(mem_usage)


def main():
    max_cost = 500
    action_counts = []
    bruteforce_memory = []
    optimized_memory = []

    # Charger les actions depuis le CSV
    actions = parse_csv(csv_path, optimize=True)

    # Tester pour différentes tailles de listes d'actions
    for i in range(1, len(actions)+1):
        subset_actions = actions[:i]
        action_counts.append(i)

        # Mesurer l'utilisation de la mémoire pour bruteforce
        bruteforce_mem = measure_memory(bruteforce, subset_actions, max_cost)
        bruteforce_memory.append(bruteforce_mem)

        # Mesurer l'utilisation de la mémoire pour knapsack
        optimized_mem = measure_memory(knapsack, subset_actions, max_cost)
        optimized_memory.append(optimized_mem)

    # Tracer les résultats
    plt.figure(figsize=(10, 6))
    plt.plot(action_counts, bruteforce_memory, label='Bruteforce', marker='o')
    plt.plot(action_counts, optimized_memory, label='Optimized', marker='x')
    plt.xticks(range(0, len(actions) + 1))
    plt.yticks(range(0, int(max(bruteforce_memory) + 10), 10))
    plt.xlabel('Nombre d\'actions')
    plt.ylabel('Utilisation de la mémoire (MiB)')
    plt.title('Comparaison de la complexité spatiale')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
