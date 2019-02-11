import sys
from collections import namedtuple

# Consider eliminating first two fields (redundant)
ExpenseStruct = namedtuple("Struct","name per_person_cost who_paid")

def hello_there():
    print("Hello there, user. I am %s." % sys.argv[0])

def validate_args():
    if len(sys.argv) < 2:
        print("Name of data file must be supplied as argument. Killing self...")
        exit()

# Input: Open file object of expenses.csv file
# Output: An array of the lines in the file
def get_lines_from_file(file_object):
    return file_object.read().split('\n')

def get_name_from_line_items(line_items):
    return line_items[0]
    
def get_total_price_from_line_items(line_items):
    return float(line_items[1]) * float(line_items[2])

def get_per_person_cost_from_line_items(line_items):
    return get_total_price_from_line_items(line_items) /        \
            len(get_who_paid_from_line_items(line_items))

def get_who_paid_from_line_items(line_items):
    return line_items[3].split('/')

def get_expense_struct_from_csv_line(csv_line):
    line_items = csv_line.split(',')
    return ExpenseStruct(                                       \
            get_name_from_line_items(line_items),               \
            get_per_person_cost_from_line_items(line_items),    \
            get_who_paid_from_line_items(line_items)            \
            )

def get_who_paid_how_much_from_file(file_object):
    who_paid_how_much = {}
    first_line = 1
    for csv_line in get_lines_from_file(file_object):
        if first_line == 1:
            first_line = 0
            continue
        expense = get_expense_struct_from_csv_line(csv_line)
        for person in expense.who_paid:
            if person not in who_paid_how_much:
               who_paid_how_much[person] = 0
            who_paid_how_much[person] += expense.per_person_cost
    return who_paid_how_much


def show_dictionary(d):
    for item in d:
        print(item + ": " + str(d[item]))

def print_amount_paid_per_person(file_object):
    show_dictionary(get_who_paid_how_much_from_file(file_object))

def main():
    hello_there()
    validate_args()
    file_object = open(sys.argv[1])
    print_amount_paid_per_person(file_object)
    file_object.close() 


if __name__ == "__main__":
    main()
