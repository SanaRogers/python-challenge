# TEST TEST

# Importing the necessary modules
import os
import csv

# Prompt user for voter lookup
voter = input("Which voter do you want to see?")

# Set path for CSV file
csvpath = os.path.join("Resources","election_data.csv")
found = False

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Look through looking for the voter
    for row in csvreader:
        if row[0]== voter:
            print(row[0] + "voted for" + row[1])
            found = True

# if the voter doesn't show up, alert the user
    if found is False:
        print("can't find voter")

