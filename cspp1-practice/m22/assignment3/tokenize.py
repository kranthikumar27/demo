'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
#from collections import Counter
#def tokenize(string):
	#dict_1 = {}
	#counter = Counter()
	#for i in string:
		#counter[1] += 1
	#return dict_1
    
            
def main():
    num_1 = input(int())
    str_1 = input()
    dict_1 = {}
    for _ in str_1:
    	if str_1 not in dict_1:
    		dict_1.append(str_1)
    		if str_1 in dict_1:
    			count+=1
    print(dict_1)


        
        
    #print(tokenize())

if __name__ == '__main__':
    main()
