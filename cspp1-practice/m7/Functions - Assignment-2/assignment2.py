# Assignment-2 - Paying Debt off in a Year

# Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be
# paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:

"""credit card"""
def paying_debtoffinayear(bal_ance, annual_interestrate):
    """defining paying function"""
    ba_la = bal_ance
    p_a_y = 0
    while True:
        i = 12
        ba_la = bal_ance
        while i != 0:
            upd_bal = ba_la - p_a_y
            ba_la = upd_bal + ((annual_interestrate / 12.0) * upd_bal)
            i -= 1
        if ba_la > 0:
            p_a_y += 10
        else:
            break
    return p_a_y
def main():
    """Defining main"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(paying_debtoffinayear(data[0], data[1])))

main()