# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    c = min(a,b)
    while c > 0:
        if(a%c) == 0 and (b%c) == 0:
            return c
        else:
            c -= 1
    



def main():
    data = input()
    data = data.split(" ")
    print(gcdIter(int(data[0]),int(data[1]))) 

if __name__== "__main__":
    main()