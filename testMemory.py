from memory_profiler import profile
from optimized import knapsack
from bruteforce import bruteforce
from utils import parse_csv

csv_path = "datasets/dataset_test.csv"


@profile
def main():
    actions = parse_csv(csv_path, True)
    max_cost = 500
    knapsack(actions, max_cost)
    bruteforce(actions, max_cost)


if __name__ == "__main__":
    main()
