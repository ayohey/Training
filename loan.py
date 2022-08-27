# get the loan details
money_owed = float(input('How much money do you owe in dollars?\n'))
apr = float(input('What is the APR?\n'))
payment = float(input('What is your Monthly Payment?\n'))
months = int(input('How many months do you want to see results for?\n'))
# divide APR by 100 to get % then divide by 12
monthly_rate = apr/100/12
# since the monthly rate remains tha same and payments vary month to month adding a for loop to show each months results
for i in range(months):
    # add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    # If money paid goes negative print the amount of the last payment
    if (money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the load in', i+1, 'months')
        break
    #make payment
    money_owed = money_owed - payment
    # Print the results after this month
    print('Paid', payment, 'of which', interest_paid, 'was interest.', end=' ')
    print('Now I owe', money_owed)