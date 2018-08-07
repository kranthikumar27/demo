'''
# This function takes in one number and returns one number.
'''

def factorial(NUM_VAL):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if NUM_VAL == 1 or NUM_VAL == 0:
        return 1
        return NUM_VAL * factorial(NUM_VAL - 1)  
def main():
    A = input()
    print(factorial(int(A)))

if __name__ == "__main__":
    main()
