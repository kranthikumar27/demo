'''
# This function takes in one number and returns one number.
'''

def factorial(Num_val):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if Num_val == 1 or Num_val == 0:
        return 1
    else:
        return Num_val * factorial(Num_val - 1)
    
def main():
    A = input()
    print(factorial(int(A)))

if __name__ == "__main__":
    main()
