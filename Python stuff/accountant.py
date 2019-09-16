investment = float(input("enter the investment amount: £"))
interest_rate = float(input("enter the interest rate as a decimal: "))
target = float(input("enter the target amount: £"))
count = 0

while investment <= target:
	increment = investment * interest_rate
	investment += increment
	count += 1
print("it will take", count, "years to accrue £" +str(target))