# Bill Splitter

This code implements a bill splitting functionality using the `BillSplitter` class. It allows a group of friends to enter their names and calculates the amount each person needs to pay based on the total bill value. It also includes a "Who is lucky?" feature that randomly selects one person who doesn't have to pay their share.

## How it works

1. The user is prompted to enter the number of friends joining the dinner (including themselves).
   - If the number is less than 1, the program displays a message and exits.

2. The user is then asked to enter the name of every friend (including themselves), each on a new line.
   - The names and initial amounts (set to 0) are stored in a dictionary called `names_and_amounts`.

3. An instance of the `BillSplitter` class is created, passing in the `names_and_amounts` dictionary.

4. The user is prompted to enter the total bill value.
   - The total bill amount is set for the `bill_splitter` instance using the `set_total_amount()` method.

5. The user is asked if they want to use the "Who is lucky?" feature.
   - If the user enters "Yes" (case-insensitive):
     - A random person is selected from the list of names using `random.choice()`.
     - The `split_bill_evenly()` method of the `bill_splitter` instance is called with the lucky person's name as an argument.
     - The program displays the name of the lucky person who doesn't have to pay.
   - If the user enters "No" or any other input:
     - The program displays a message indicating that no one will be lucky.
     - The `split_bill_evenly()` method of the `bill_splitter` instance is called without any arguments.

6. Finally, the `bill_splitter` instance is printed, which displays the amount each person needs to pay.

## Usage

1. Run the script and enter the number of friends joining the dinner (including yourself).
2. Enter the name of every friend (including yourself), each on a new line.
3. Enter the total bill value.
4. Decide whether to use the "Who is lucky?" feature by entering "Yes" or "No".
5. The program will display the amount each person needs to pay based on the total bill value and the "Who is lucky?" feature.

## Dependencies

This code depends on the `BillSplitter` class, which should be defined in a separate file named `BillSplitterClass.py`. Make sure to have the `BillSplitterClass.py` file in the same directory as the main script.
