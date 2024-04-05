# write your code here
from BillSplitterClass import BillSplitter

if __name__ == "__main__":

    n_at_dinner = int(input("Enter the number of friends joining (including you):\n"))

    if n_at_dinner < 1:
        print("\nNo one is joining for the party")
        exit()

    print("\nEnter the name of every friend (including you), each on a new line:")
    names_and_amounts = {}
    for i in range(n_at_dinner):
        name = input()
        names_and_amounts[name] = 0

    bill_splitter = BillSplitter(names_and_amounts)
    print(f"\n{bill_splitter}\n")