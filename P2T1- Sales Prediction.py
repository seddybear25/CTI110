# finding the projected total amount of sales.
#09/16/19
#CTI-110 P2T1-Sales Prediction
# SedrickCulbreath


# Get the  projected total sales.
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit as 23 percent of total sale.
profit = total_sales *0.23

#Display the profit.
print('The profit is $' , format(profit, ',.2f'))
