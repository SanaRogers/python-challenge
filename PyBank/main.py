print ("homework")
import os
import csv
csvbudget = os.path.join('..','Resources','budget_data.csv')

with open(csvbudget) as csvfile:
    csvreader = csv.reader(csvbudget, delimiter=',')
    print(csvreader)



