#Importing the dependencies
import os
import csv

#Setting the file location
bank_csv_path = os.path.join("budget_data.csv")

#creating lists of months
pl_months = [] 

#creating lists of profit/loss of each month
total_profit_loss = []

#creating lists 0f profit/loss change of each month
pl_difference = []

#opening the file
with open(bank_csv_path,"r") as bank_csv_file:
    
    #reading the file
    bank_csv_reader = csv.reader(bank_csv_file, delimiter=',')
    
    #skip the header row 
    bank_csv_header = next(bank_csv_reader)
    
    #loop to read each row in the file
    for row in bank_csv_reader:
        
        #Add the each month value to the month list
        pl_months.append(row[0])

        #Add each month profit/loss to the profit loss list
        total_profit_loss.append(int(row[1]))

#loop to find the monthly profit or loss for each month
for i in range(len(total_profit_loss) - 1):

    #Creat a list of difference of next month to previous month
    pl_difference.append (total_profit_loss[i+1] - total_profit_loss[i])


#Calculate total months
total_months = len(pl_months)

#Calculate total amount
total_amount = sum(total_profit_loss)

#Calculate the average change of total differences  vs total values
average_change = round(sum(pl_difference) / len(pl_difference),2)

#finding greatest profit
greatest_profit = max(pl_difference)

#find the month of greatest profit
#adding 1 to find the month associated in the month list with this profit (next month) 
greatest_increase_month_index = pl_difference.index(greatest_profit) + 1 
greatest_increase_month = pl_months[greatest_increase_month_index]

#finding greatest loss
greatest_loss = min(pl_difference)

#find the month of greatest loss
# adding 1 to find the month associated in the month list with this profit (next month) 
greatest_decrease_month_index = pl_difference.index(greatest_loss) + 1 
greatest_decrease_month = pl_months[greatest_decrease_month_index]

#printing the values to screen
print("Financial Analysis")
print("-----------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total : ${total_amount}")
print(f"Average Change : ${average_change}")
print(f"Greatest Increase in Profits : {greatest_increase_month} (${greatest_profit})")
print(f"Greatest Decrease in Profits : {greatest_decrease_month} (${greatest_loss})")

#Specify the file to write the results
bank_output_path = os.path.join("budget_output.txt")
# Open the file to creat and write  
with open(bank_output_path, 'w+') as Bank_output_csv_file:
    # Initialize csv writer to write the contents
    Bank_output_csv_file.write(
        f'----------------------------------------------------------\n'
        f'Financial Analysis\n'
        f'----------------------------------------------------------\n'
        f'Total Months: {total_months}\n'
        f'Total : ${total_amount}\n'
        f'Average Change : ${average_change}\n'
        f'Greatest Increase in Profits : {greatest_increase_month} (${greatest_profit})\n'
        f'Greatest Decrease in Profits : {greatest_decrease_month} (${greatest_loss})')

#End of code