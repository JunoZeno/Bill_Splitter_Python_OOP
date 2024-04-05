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

    # Create an instance of the BillSplitter class passing in the names_and_amounts dictionary
    bill_splitter = BillSplitter(names_and_amounts)

    total_bill_amount = float(input("\nEnter the total bill value:\n"))

    # Set the total bill amount for the bill_splitter instance
    bill_splitter.set_total_amount(total_bill_amount)

    # Split the bill evenly among all the friends in the names_and_amounts dictionary
    bill_splitter.split_bill_evenly()

    print(f"\n{bill_splitter}\n")
