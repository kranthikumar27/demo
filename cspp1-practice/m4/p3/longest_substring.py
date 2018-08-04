'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and cleared your head.'''

def main():
    s=input("Enter string")
    s=s+" "
    i=0
    len1=-1
    while i<(len(s)-2):
        j=i
        while s[j]<=s[j+1] and (j)<(len(s)-2):
            j=j+1
            len2=j-i
            if len2>len1:
                len1=len2
                k=int(i)
                l=int(j)
            i=j+1
        t1=k
        t2=l
        print(k,l)
        while k<=l:
            print(s[k])
            k=k+1
    if __name__ == "__main__":
        main()
