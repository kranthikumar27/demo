def background(color):
    bgcolor=[]
    lines=color.split(";")
    initialtag="background-color:\""
    endtagg=";\""
    answer=[]
    # count=0
    for i in lines:
        if "background-color" in i:
            start = i.index(initialtag)
            i= i[start+len(initialtag):]
            end = i.index(endtagg)
            answer.append(i[end:])
            print(answer)
                
    #     count=count+1
    #     print(answer)
    # print(count)

def image(urls):
    lines = urls.split("<img")
    # print(lines)
    lines = lines[1:]
    startingtag="src=\""
    endtag = "\""
    image=[]
    counter=0
    for i in lines:
        image.append(i)
        # print(image)
        for items in image:
            if startingtag in items:
                start = items.index(startingtag)
                items = items[start+len(startingtag):]
                end = items.index(endtag)
                result = items[:end]
        counter=counter+1
        print(result)
    print(counter)
        
def list1(data):
    pass
def main():
    data = open("webpage5.html", errors="ignore").read()
    # print(data)
    inputdata = input()
    if inputdata == "image":
        image(data)
    elif inputdata == "background":
        background(data)
    elif inputdata == "list"
        list1(data)
    # image(data)
    


if __name__ == '__main__':
    main()