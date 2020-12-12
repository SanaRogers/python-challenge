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

# ![Vote Counting](Images/Vote_counting.png)

# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

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




# Import two modules necessary for this homework
import os
import csv

# Prompt user for budget information and import csv

budget_file_to_load=os.path.join("Resources","budget_data.csv")
for row in budget_file_to_load:
    print row

# # The total number of months included in the dataset
# total_months = 0
# total_profit = 0
# previousNum = 0
# profit_losses = []
# sum_of_profloss = 0
# net_change = 0
# greatest_increase = 0
# greatest_increase_month = ""
# greatest_decrease = 0
# decrease_month = ""
 
# # Read CSV file and convert to a list of dictionaries
# with open(budget_file_to_load) as budget_file:
#     reader = csv.reader(budget_file)
    
#     # Read the Header Row
#     first_row = next(reader)
    
# # print(first_row)

# # header = next(reader)
# # first_row = next(reader)
# previousNum = int(first_row[1])
# total_profit = int(first_row[1])

# for row in reader:
#     total_months = total_months + 1
#     total_profit = total_profit + int(row[1])

#     #Calculate net changes
#     net_change = previousNum - int(row[1])
#     profit_losses.append(int(row[1])) - previousNum
#     previousNum = int(row[1])
#     if net_change > greatest_increase:
#         greatest_increase = net_change
#         increase_month = row[0]
#     if net_change < greatest_decrease:
#         greatest_decrease = net_change
#         increase_month= row[0]

# for x in profit_losses:
#     sum_of_profloss = sum_of_profloss + x
# print(total_months)
# print(profit_losses)
# print(sum_of_profloss/len(profit_losses))
# print(total_profit)
# print(max(profit_losses))
# print(min(profit_losses))
# print(greatest_increase, increase_month)
# print(greatest_decrease, decrease_month)
# print("------------------------")

    
# # print(budget_file)

# # budget_header = next(reader) 
# # print(f"Budget Header: {budget_header}")

# # #     for row in reader:
# # print(row)






