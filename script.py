import sys
from collections import namedtuple

# Consider eliminating first two fields (redundant)
ExpenseStruct = namedtuple("Struct","name unit_price quanitity total_price who_paid")

def test():
    return

test = ExpenseStruct("things",4,1,4,"Joel/Erastus")

if len(sys.argv) < 2:
    print("Input filename must be provided.")

test = open(sys.argv[1])

print(test)

data_string = test.read()

data_lines = []

data_lines = data_string.split('\n') 
data_organized = []

i = 0
for line in data_lines:
    if i == 0:
        i+=1
        continue # skip first line
    #sys.stdout.write(str(i) + ": " + line + '\n')
    #i+=1
    
    line_data = line.split(',')

    data_organized.append(ExpenseStruct( \
            line_data[0], \
            line_data[1], \
            line_data[2], \
            float(line_data[1]) * float(line_data[2]), \
            line_data[3].split('/')))
    
#print(len(data_organized) + " len of orgdata")
who_paid_how_much = {}
for item in data_organized:
    split_n_ways = len(item.who_paid)
    per_person_cost = item.total_price/split_n_ways
    for who in item.who_paid:
        if who not in who_paid_how_much:
            who_paid_how_much[who] = 0
        who_paid_how_much[who] += per_person_cost 


for person in who_paid_how_much:
    print(person + " has paid " + str(who_paid_how_much[person]))


