'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
N = int(input())
I = 1
while I < abs(N):
    J = N % 10
    I = J * I
    N = N // 10    
print(I)
    
