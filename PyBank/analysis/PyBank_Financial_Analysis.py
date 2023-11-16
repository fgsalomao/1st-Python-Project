# Import OS and csv
import os
import csv
from datetime import datetime

# determine file path
read_file= os.path.join("..","Resources","budget_data.csv")

# Open and read file
with open(read_file) as csvfile:
    budget_file=csv.reader(csvfile, delimiter=",")
    budget_header= next(budget_file)

    # Create variables to store read information
    months=1
    total_amount=0
    delta=0
    first_row= next(budget_file)
    # Start variable if value of first row
    total_amount+=int(first_row[1])
    # Assign value of of first row amount to calculate delta
    # will use curre_amount on each iteration
    # to update previous value
    previous_amount=int(first_row[1])

    # Create lists to add variation and calc avg/max/min
    changes_prof_loss=[] 
    changes_date=[]

    # # Iterate through rows
    for row in budget_file:
        months+=1
        total_amount+=int(row[1])
        current_amount=int(row[1])
        delta=current_amount-previous_amount
        
        # Update previous_amount
        previous_amount=current_amount

        # Add variance to changes_prof_loss list
        # for future calculations (after iteration)
        changes_prof_loss.append(delta)
        
        # Add Month to dates list to allow reference
        # When writtig and printing analysis
        changes_date.append(row[0])

# # Calculations for analysis

grt_incr = max(changes_prof_loss)
grt_incr_dt = changes_date[changes_prof_loss.index(grt_incr)]
grt_decr = min(changes_prof_loss)
grt_decr_dt = changes_date[changes_prof_loss.index(grt_decr)]
month_avr_chg = round(sum(changes_prof_loss)/len(changes_prof_loss),2)

# Print Results

print('Financial Analysis')
print('------------------------------------------------------')
print(f'Total Months: {months}')
print(f'Total:$ {total_amount}')
print(f'Average Change: $ {month_avr_chg}')
print(f'Greatest Increase in Profits: {grt_incr_dt} (${grt_incr})')
print(f'Greatest Decrease in Profits: {grt_decr_dt} (${grt_decr})')


# Create output file in txt
output_file = os.path.join("..","analysis","PyBank_results.txt")

# Write analysis print statements to file by adding ",file=datafile"
#  to same print statements
with open(output_file, "w") as datafile:
    print('Financial Analysis', file=datafile)
    print('------------------------------------------------------',file=datafile)
    print(f'Total Months: {months}',file=datafile)
    print(f'Total:$ {total_amount}',file=datafile)
    print(f'Average Change: $ {month_avr_chg}',file=datafile)
    print(f'Greatest Increase in Profits: {grt_incr_dt} (${grt_incr})',file=datafile)
    print(f'Greatest Decrease in Profits: {grt_decr_dt} (${grt_decr})',file=datafile)