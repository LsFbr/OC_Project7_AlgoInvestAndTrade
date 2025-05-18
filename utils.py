import csv
from prettytable import PrettyTable
from action import Action


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
        for row in reader:
            cost = float(row[1])
            profit_rate = float(row[2].split("%")[0])
            if optimize:
                action = Action(row[0], cost, profit_rate, True)
            else:
                action = Action(row[0], cost, profit_rate, False)
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

    if optimize:
        for action in best_combination:
            table.add_row([action.name, f"{action.cost/100:.2f}", f"{action.profit_rate*100:.2f}"])

        print("Meilleure combinaison :")
        print(table)

        total_cost = sum(action.cost for action in best_combination)/100
        total_profit = sum(action.profit_value for action in best_combination)/100
        total_profit_rate = total_profit*100/total_cost

        print(f"Coût total: {total_cost}€")
        print(f"Profit total: {total_profit_rate:.2f}% ({total_profit:.2f}€)")

    else:
        for action in best_combination:
            table.add_row([action.name, f"{action.cost:.2f}", f"{action.profit_rate*100:.2f}"])

        print("Meilleure combinaison :")
        print(table)

        total_cost = sum(action.cost for action in best_combination)
        total_profit = sum(action.cost*action.profit_rate for action in best_combination)
        total_profit_rate = total_profit*100/total_cost

        print(f"Coût total: {total_cost}€")
        print(f"Profit total: {total_profit_rate:.2f}% ({total_profit:.2f}€)")
