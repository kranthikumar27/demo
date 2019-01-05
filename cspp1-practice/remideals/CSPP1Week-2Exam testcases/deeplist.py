def listsum1(data):
    total = 0
    for i in data:
        # print(i)
        if isinstance(i,list):
            total = total + listsum1(i)
        else:
            total = total + i 
    return total

def countoflists(data):
    count = 0
    for i in data:
        if isinstance(i, list):
            count = count + countoflists(i)
    return count
    # sum(x.count(1) for x in data)
    # for y in x:
    #     return count
    # return data.count(x) + sum(
    #     countoflists(i,x) for i in data if isinstance(i,list))
    
    
        # a=i
        # print(sum(a))
        
    #     for j in i:
    #         total += sum(i)
    # print(total)

def main():
    
    data = eval(input())
    # print(data)
    # total =sum(data)
    # print(total)
    print(listsum1(data))
    print(countoflists(data))
    # map(str,data)
    # data = map(str,data)
    # total = ''.join(data)
    # print(total)
    # sum(data)
    # for i in data:
    #     print(i)
    #     total=sum(int(i))
    #     # total=data[i]+data[i+1]
    # print(total)
    # list1=data.split()
    # print(list1)
    # total=0
    # for i in data:
    #   total += int(i)
    #   print("Sum = ",total)
    # print(data)
    # for i in data:
    #   data.append(list1)
    # print(list1)
    # mylist = int(input())
    # print(mylist)
    # for number in data: 
    #     total = sum(data)
    # print(total)
    # print ("The sum of the numbers is:", total)
if __name__ == '__main__':
    main()