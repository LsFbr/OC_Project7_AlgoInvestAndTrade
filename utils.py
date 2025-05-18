import csv
from prettytable import PrettyTable


def parse_csv(csv_name, optimized=False):
    """
    Parse the CSV file and return a list of actions.
    args:
        csv_name: str, name of the csv file
        optimized: bool, if True, add the profit_value to the actions and scale the costs by 100
    returns:
        list of actions
    """
    csv_path = f"datasets/{csv_name}"
    actions = []
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        if optimized:
            for row in reader:
                scaled_cost = int(float(row[1]) * 100)
                profit_rate = float(row[2].split("%")[0]) / 100
                action = {
                    "name": row[0],
                    "cost": scaled_cost,
                    "profit_rate": profit_rate,
                    "profit_value": int(scaled_cost * profit_rate)
                }
                actions.append(action)
        else:
            for row in reader:
                cost = float(row[1])
                profit_rate = float(row[2].split("%")[0]) / 100
                action = {
                    "name": row[0],
                    "cost": cost,
                    "profit_rate": profit_rate
                }
                actions.append(action)
    return actions


def display_results(csv_name, best_combination, optimized=False):
    """
    Display the results of the best combination.
    args:
        csv_name: str, name of the csv file
        best_combination: list of actions
        optimized: bool, if True, the actions are optimized
    """
    print(f"--- Résultat pour le dataset {csv_name} ---")

    table = PrettyTable()
    table.field_names = ["Nom", "Coût (€)", "Profit (%)"]
    table.title = "Meilleure combinaison :"

    for action in best_combination:
        if optimized:
            table.add_row([action["name"], f"{action['cost']/100:.2f}", f"{action['profit_rate']*100:.2f}"])
        else:
            table.add_row([action["name"], f"{action['cost']:.2f}", f"{action['profit_rate']*100:.2f}"])

    print(table)

    if optimized:
        total_cost = sum(action["cost"] for action in best_combination)/100
        total_profit = sum(action["cost"]*action["profit_rate"] for action in best_combination)/100
        total_profit_rate = total_profit*100/total_cost
    else:
        total_cost = sum(action["cost"] for action in best_combination)
        total_profit = sum(action["cost"]*action["profit_rate"] for action in best_combination)
        total_profit_rate = total_profit*100/total_cost

    print(f"Coût total: {total_cost}€")
    print(f"Profit total: {total_profit_rate:.2f}% ({total_profit:.2f}€)")


def dataset_exploration_report(csv_name, actions):
    """
    Display a report of the dataset.
    args:
        csv_name: str, name of the csv file
        actions: list of actions
    """
    null_cost_count = 0
    negative_cost_count = 0
    null_profit_rate_count = 0
    negative_profit_rate_count = 0
    unusable_actions_count = 0

    for action in actions:
        if action["cost"] == 0:
            null_cost_count += 1
        if action["cost"] < 0:
            negative_cost_count += 1
        if action["profit_rate"] == 0:
            null_profit_rate_count += 1
        if action["profit_rate"] < 0:
            negative_profit_rate_count += 1

    unusable_actions_count = (
        null_cost_count
        + negative_cost_count
        + null_profit_rate_count
        + negative_profit_rate_count
    )

    print(f"Rapport de l'exploration du dataset {csv_name}:")
    print(f"Actions: {len(actions)}")
    print(f"Actions avec un coût nul: {null_cost_count}")
    print(f"Actions avec un coût négatif: {negative_cost_count}")
    print(f"Actions avec un profit nul: {null_profit_rate_count}")
    print(f"Actions avec un profit négatif: {negative_profit_rate_count}")
    print("--------------------------------")
    print(f"Actions inutilisables: {unusable_actions_count} ({unusable_actions_count*100/len(actions):.2f}%)\n")
