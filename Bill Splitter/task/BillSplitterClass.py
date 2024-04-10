# create a class named BillSplitter which has a constructor that takes in a dictionary with names as keys and amounts as values.

class BillSplitter:
    def __init__(self, names_and_amounts):
        self.names_and_amounts: dict = names_and_amounts
        self.total_amount: float = None

    def show(self):
        for name, amount in self.names_and_amounts.items():
            print(f"{name} - {amount}")

    def set_total_amount(self, total_amount):
        self.total_amount = total_amount

    def split_bill_evenly(self, lucky_name=None):
        if self.total_amount is None:
            raise ValueError("Total amount has not been set")
        if lucky_name:
            n = len(self.names_and_amounts) - 1
            for name in self.names_and_amounts:
                if name == lucky_name:
                    continue
                self.names_and_amounts[name] = round(self.total_amount / n, 2)

        else:
            n = len(self.names_and_amounts)
            for name in self.names_and_amounts:
                self.names_and_amounts[name] = round(self.total_amount / n, 2)

    def __repr__(self):
        return f"{self.names_and_amounts}"

    def __str__(self):
        return f"{self.names_and_amounts}"

