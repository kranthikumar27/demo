'''
# This function takes in one number and returns one number.
'''

def factorial(num_val):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if num_val in [0, 1]:
        return 1
    return num_val * factorial(num_val - 1)
def main():
    '''
    fact
    '''
    data = input()
    print(factorial(int(data)))

if __name__ == "__main__":
    main()
