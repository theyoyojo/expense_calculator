# Shared expense calculator for a very specific file format
# By Joel Savitz <joelsavitz@gmail.com>
# Created 11 February 2019

import sys
from collections import namedtuple

# A simple compund data type
ExpenseStruct = namedtuple("ExpenseStruct","name per_person_cost who_paid")

# Print a welcome message
def hello_there():
    print("Hello there, user. I am %s." % sys.argv[0])

# Assert that at least one argument is passed to the script
def validate_args():
    if len(sys.argv) < 2:
        print("Name of data file must be supplied as argument. Killing self...")
        exit()

# Input: An open file object of expenses.csv data file
# Output: An array of the lines in the file
def get_lines_from_file(file_object):
    return filter(None,file_object.read().split('\n'))

# Input: An array of strings from row of data file
# Output: The name of the expense
def get_name_from_line_items(line_items):
    return line_items[0]
    
# Input: An array of strings from row of data file
# Output: The total price of the expense
def get_total_price_from_line_items(line_items):
    return float(line_items[1]) * float(line_items[2])

# Input: An array of strings from row of data file
# Output: The amount paid by each person for the expense
def get_per_person_cost_from_line_items(line_items):
    return get_total_price_from_line_items(line_items) /        \
            len(get_who_paid_from_line_items(line_items))

# Input: An array of strings from row of data file
# Output: An array of strings, the names of each person who paid
def get_who_paid_from_line_items(line_items):
    return line_items[3].split('/')

# Input: A string of comma separated values from a row of the data file
# Output: Silent if dispute field is empty, otherwise the dispute is reported
def catch_dispute(line_items):
    if line_items[4] != '':
        print("Item \"" + line_items[0] + "\" disputed: " + line_items[4])

# Input: A string of comma separated values from a row of the data file
# Output: A struct containing data relevant data pertaining to a single expense
def get_expense_struct_from_csv_line(csv_line):
    line_items = csv_line.split(',')
    catch_dispute(line_items)
    return ExpenseStruct(                                       \
            get_name_from_line_items(line_items),               \
            get_per_person_cost_from_line_items(line_items),    \
            get_who_paid_from_line_items(line_items))

# Input: An open file object of expenses.csv data file
# Output: An dictionary associating everyone mentioned in the data file to the
#+the amount of shared expenses paid by that person
def get_who_paid_how_much_from_file(file_object):
    who_paid_how_much = {}
    first_line = True
    for csv_line in get_lines_from_file(file_object):
        if first_line == True:
            first_line = False
            continue
        expense = get_expense_struct_from_csv_line(csv_line)
        for person in expense.who_paid:
            if person not in who_paid_how_much:
               who_paid_how_much[person] = 0
            who_paid_how_much[person] += expense.per_person_cost
    return who_paid_how_much

# Print each key and value in a dictionary
# Input: A dictionary object
# Output: Dictionary contents written to stdout
def show_dictionary(d):
    for item in d:
        print(item + ": " + str(d[item]))

# Input: An open file object of expenses.csv data file
# Output: Total ammount paid by each person mentioned in the file written to
#+stdout
def print_amount_paid_per_person(file_object):
    show_dictionary(get_who_paid_how_much_from_file(file_object))

# Entry point for program when run as a script
def main():
    hello_there()
    validate_args()
    file_object = open(sys.argv[1])
    print_amount_paid_per_person(file_object)
    file_object.close() 

if __name__ == "__main__":
    main()
