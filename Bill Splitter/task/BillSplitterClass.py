# create a class named BillSplitter which has a constructor that takes in a dictionary with names as keys and amounts as values.

class BillSplitter:
    def __init__(self, names_and_amounts):
        self.names_and_amounts = names_and_amounts

    def show(self):
        for name, amount in self.names_and_amounts.items():
            print(f"{name} - {amount}")

    def __repr__(self):
        return f"{self.names_and_amounts}"

    def __str__(self):
        return f"{self.names_and_amounts}"

