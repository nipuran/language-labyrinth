import time

expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(f'I spent {expense[1] - expense[0]} dollars extra compare to January')

time.sleep(2)
# 2. Find out your total expense in first quarter (first threee months) of the year.
first_quarter = 0
for i in range(3):
    first_quarter += expense[i]
print(f'my total expense in first quarter (first three months) of the year is {first_quarter}')

time.sleep(2)
# 3. Find out if you spent exactly 2000 dollars in any month.
for i in expense:
    if i == 2000:
        print('yes, I spent exactly 2000 dollars')
        break
else:
    print('no, I did not spend exactly 2000 dollars in any months')

time.sleep(2)
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
june_expense = 1980
expense.append(june_expense)
print('June month expense has been added')
print(expense)

time.sleep(2)
'''
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your montly expense list.
based on this.
'''
item_refund_price = 200 
april_index = 3
expense[april_index] -= item_refund_price
print(f'new expense list: {expense}')
