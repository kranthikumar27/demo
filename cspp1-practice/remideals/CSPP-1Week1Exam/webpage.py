def background(color):
    lines=color.split("back")
    startingtag="ground-color:\""
    endtag=";\""
    bgcolor=[]
    count=0
    for i in lines:
        bgcolor.append(i)
        for j in bgcolor:
            if startingtag in j:
                start = j.index(startingtag)
                items = j[start+len(startingtag):]
                end = j.index(endtag)
                results = j[:end]
        count=count+1
        print(results)
    print(count)

# def image(urls):
#     lines = urls.split("<img src")
#     # print(lines)
#     startingtag="=\""
#     endtag = "\""
#     image=[]
#     counter=0
#     for i in lines:
#         image.append(i)
#         # print(image)
#         for items in image:
#             if startingtag in items:
#                 start = items.index(startingtag)
#                 items = items[start+len(startingtag):]
#                 end = items.index(endtag)
#                 result = items[:end]
#         counter=counter+1
#         print(result)
#     print(counter)
        
    
def main():
    data = open("webpage5.html", errors="ignore").read()
    # print(data)
    # image(data)
    background(data)


if __name__ == '__main__':
    main()