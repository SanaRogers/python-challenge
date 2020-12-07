# Import two modules necessary for this homework
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'budget_data.csv')

import csv

with open(my_file) as budget:
    reader = csv.reader(budget, delimiter=',')
    
    print(reader)

    budget_header = next(reader) 
    # print(f"Budget Header: {budget_header}")

    for row in reader:
        print(row)






