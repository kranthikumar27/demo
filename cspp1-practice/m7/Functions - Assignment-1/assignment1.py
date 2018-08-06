# Functions | Assignment-1 - Paying Debt off in a Year

# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the
# credit card company each month.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining
# balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of
# Remaining balance: 813.4141998135

# So your program only prints out one thing: the remaining balance at the end of the year in the format:
# Remaining balance: 4784.0

# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)


def paying_Debt_Off_In_A_Year(balance, annual_Interest_Rate, monthly_Payment_Rate):
        previous_balance = balance
        for _ in range(12):
                Monthly_interest_rate = (Annual_interest_rate) / 12.0
                Minimum_monthly_payment = (Minimum_monthly_payment_rate) * (Previous_balance)
                Monthly_unpaid_balance = (Previous_balance) - (Minimum_monthly_payment)
                Updated_balance_each_month = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
                previous_balance = updated_balance_each_month
        return rounded(updated_balance_each_month,2)
                
def main():
	data = input()
	data = data.split(' ')
	data = list(map(float, data))
	print("Remaining balance:", paying_debt_off_in_a_year (data[0],data[1],data[2]))

if __name__== "__main__":
	main()
