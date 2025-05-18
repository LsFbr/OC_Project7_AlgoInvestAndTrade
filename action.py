class Action:
    def __init__(self, name: str, cost: float, profit_rate: float, optimize=False):
        if optimize:
            self.name = name
            self.cost = int(cost * 100)
            self.profit_rate = profit_rate / 100
            self.profit_value = (self.cost * int(profit_rate * 100)) // 10000
        else:
            self.name = name
            self.cost = int(cost)
            self.profit_rate = profit_rate / 100

    def __repr__(self):
        return f"{self.name} - {self.cost} - {self.profit_rate} - {self.profit_value}"
