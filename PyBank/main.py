import os
import csv

#from PyBank.Date import Date

# Path to collect data from the Resources folder
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#Read in the CSV file
with open (csvpath,'r') as csvfile: 
  
  #split the date on comas
  csvreader=csv.reader(csvfile,delimiter=",")
  
  #Read the header row first
  csv_header=next(csvreader)

  # Create empty lists 
  total_months = []
  total_profit = []
  monthly_profit_change = []

# Append the total months and total profit 
  for row in csvreader:  
        total_months.append(row[0])
        total_profit.append(int(row[1]))

#Monthly change in profits
  for i in range(len(total_profit)-1): 
       #difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
#Max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

#Max and min months
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

#Print:
print("Financial Analysis")
print("\n")
print("------------------------------------------------------")
print("\n")
print(f"Total Months:{len(total_months)}")
print(f"Total:${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#Output file
output_file = os.path.join('..', 'Analysis', 'Financial_Analysis_Summary.txt')

with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")



