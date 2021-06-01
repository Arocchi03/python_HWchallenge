import csv 
import os 

date = 0
profit = 0
profit_losses_list = []
profit_change=[]

#Reading data 
csvpath = os.path.join("PyBank/Resources/budget_data.csv")
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') 
    csv_header = next(csvreader)
# Starting For loop
    for column in csvreader:
#print(row)
#The total number of months included in the dataset

        date = date + 1
        #date += 1
#The net total amount of "Profit/Losses" over the entire period
        profit += int(column[1])
#The average of the changes in "Profit/Losses" over the entire period
        profit_losses_list.append(int(column[1]))

        # for x in range(len(profit_losses_list)):
        #     profit_change.append(profit_losses_list[x-1]-profit_losses_list[x])

print(date)
print(profit)
#     print(profit_losses_list)
#     print(profit_change)



for x in range(len(profit_losses_list)-1):
    profit_change.append(profit_losses_list[x+1]-profit_losses_list[x])
print(profit_losses_list)
print(profit_change)

avg_change= round((sum(profit_change)/len(profit_change)),2)
print(avg_change)

print(min(profit_change))
print(min(profit_change))

max_inc = max(profit_change)
min_dec = min(profit_change)

x = [profit_change.index(max_inc)+1]
y = [profit_change.index(min_dec)+1]

print(max_inc)
print(min_dec)