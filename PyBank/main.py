# Python Homework - Py Me Up, Charlie

# Background

# Well... you've made it!

# It's time to put away the Excel sheet and join the big leagues. 
# Welcome to the world of programming with Python. In this homework assignment, 
# you'll be using the concepts you've learned to complete the **two** Python Challenges, PyBank and PyPoll.

# Both of these challenges encompass a real-world situation where your newfound Python scripting skills can come in handy. 
# These challenges are far from easy so expect some hard work ahead!



# PyBank

# ![Revenue](Images/revenue-per-lead.png)

# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:



# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# ## PyPoll



# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Hints and Considerations

# Consider what we've learned so far. To date, we've learned how to import modules like `csv`; 
# to read and write files in various formats; to store contents in variables, lists, and dictionaries; 
# to iterate through basic data structures; and to debug along the way. Using what we've learned, 
# try to break down your tasks into discrete mini-objectives. 
# This will be a _much_ better course of action than spending all your time looking for a solution on Stack Overflow.

# As you will discover, for some of these challenges, the datasets are quite large. 
# This was done purposefully, as it showcases one of the limits of Excel-based analysis. 
# While our first instinct, as data analysts, is often to head straight into Excel, 
# creating scripts in Python can provide us with more robust options for handling "big data".

# Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.

# Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, and the art of programming is extremely unforgiving to moochers. Dig your heels in, burn the night oil, and learn this while you can! These are skills that will pay dividends in your future career.

# Start early, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. Don't resign yourself to simply saying, "I'm totally lost." If you need help, reach out because we're happy to help. But, come prepared and show us what you have done and your thought process.

# Always commit your work and back it up with GitHub/GitLab pushes. You don't want to lose hours of your work because you didn't push it to GitHub/GitLab every half hour or so.

# Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file



# Copyright

# Trilogy Education Services © 2019. All Rights Reserved.

import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    
    
    # Read each row of data after the header
    data = []
    
    for row in csvreader:
        data.append(row)
   
    print("Financial Analysis")
    print("----------------------------")
#   * The total number of months included in the dataset
    print(f'Total Months: {len(data)}')
    
#   * The net total amount of "Profit/Losses" over the entire period
    total_amount = 0
    for i in data: 
        total_amount = total_amount+int(i[1])
    print(f'Total: ${total_amount}')
#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    change_list=[]
    for i in range (0,len(data)-1):
        change=int(data[i+1][1])-int(data[i][1])
        change_list.append(change)
    average=sum(change_list)/len(change_list)
    print(f'Average  Change: ${round(average,2)}')
#   * The greatest increase in profits (date and amount) over the entire period
    
    greatest_increase_month = data[change_list.index(max(change_list))+1][0]
    print(f'Greatest Increase in Profits: {greatest_increase_month} (${max(change_list)})')

#   * The greatest decrease in losses (date and amount) over the entire period
    
    greatest_decrease_month = data[change_list.index(min(change_list))+1][0]
    print(f'Greatest decrease in Profits: {greatest_decrease_month} (${min(change_list)})')

output_path= os.path.join("Analysis","Final_Analysis.txt")
with open(output_path,"w", newline="") as writer:
   
    writer.write("Financial Analysis\n")
    writer.write("----------------------------\n")
    writer.write(f'Total Months: {len(data)}\n')
    writer.write(f'Total: ${total_amount}\n')
    writer.write(f'Average  Change: ${round(average,2)}\n')
    writer.write(f'Greatest Increase in Profits: {greatest_increase_month} (${max(change_list)})\n')
    writer.write(f'Greatest decrease in Profits: {greatest_decrease_month} (${min(change_list)})\n')