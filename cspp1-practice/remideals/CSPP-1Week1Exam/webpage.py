# def getBackground(color):
    # lines=color.split("back")
    # # print(lines)
    # startingtag="ground-color:\""
    # endtag=";\""
    # bgcolor=[]
    # for i in lines:
    #     bgcolor.append(i)
    #     # print(bgcolor)
    #     for j in bgcolor:
    #         if startingtag in j:
    #             start = j.index(startingtag)
    #             items = j[start+len(startingtag):]
    #             end = j.index(endtag)
    #             results = j[:end]
    #             print(results)
        # print(bgcolor)
    # pass

def getImageUrl(urls):
    lines = urls.split("<img src")
    # print(lines)
    startingtag="=\""
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
                print(result)
                counter=counter+1
    print(counter)
    
def main():
    data = open("webpage5.html", errors="ignore").read()
    # print(data)
    getImageUrl(data)
    # getBackground(data)


if __name__ == '__main__':
    main()