import csv
import os
os.chdir("/Users/andrewcheng/Documents/GitHub/BCS-data-analytics-materials/3-python-challenge/PyBank")
list_of_yearly_profits = []
with open('budget_data.csv', newline=" ") as budget_data:
    fields =["date", "profit/losses"]
    user_reader = csv.DictReader(budget_data)
    for row in budget_data:
        list_of_yearly_profits.append(row['date'])

print(list_of_yearly_profits)