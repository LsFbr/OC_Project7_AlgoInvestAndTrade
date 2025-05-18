import csv
from prettytable import PrettyTable


def parse_csv(csv_path, optimize=False):
    """
    Parse the CSV file and return a list of actions.
    args:
        csv_path: str, path to the CSV file
        optimize: bool, if True, add the profit_value to the actions and scale the costs by 100
    returns:
        list of actions
    """

    actions = []
    with open(csv_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        if optimize:
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


def display_results(best_combination, optimize=False):
    """
    Display the results of the best combination.
    args:
        best_combination: list of actions
    """
    table = PrettyTable()
    table.field_names = ["Nom", "Coût (€)", "Profit (%)"]

    for action in best_combination:
        if optimize:
            table.add_row([action["name"], f"{action['cost']/100:.2f}", f"{action['profit_rate']*100:.2f}"])
        else:
            table.add_row([action["name"], f"{action['cost']:.2f}", f"{action['profit_rate']*100:.2f}"])

    print("Meilleure combinaison :")
    print(table)

    if optimize:
        total_cost = sum(action["cost"] for action in best_combination)/100
        total_profit = sum(action["cost"]*action["profit_rate"] for action in best_combination)/100
        total_profit_rate = total_profit*100/total_cost
    else:
        total_cost = sum(action["cost"] for action in best_combination)
        total_profit = sum(action["cost"]*action["profit_rate"] for action in best_combination)
        total_profit_rate = total_profit*100/total_cost

    print(f"Coût total: {total_cost}€")
    print(f"Profit total: {total_profit_rate:.2f}% ({total_profit:.2f}€)")
