'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''This is to remove special characters from the given string'''
    remove_spec_char = re.sub('[^A-Za-z0-9]+', '', string)
    return remove_spec_char

def main():
    '''This is the main method'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
