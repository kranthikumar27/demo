def background(data):
	bgcolor=[]
	linewithcolor=data.split(";")
	# print(linewithcolor)
	startingtag="background-color"
	endtag=";"
	result=[]
	tag=":"
	count=0
	for items in linewithcolor:
		if "background-color" in items:
			start = items.index(startingtag)
			items = items[start+len(startingtag):]
			end = items.index(tag)
			result = items[end:]
				# count =count+1
				# result=set(result)+
				# 
			print(result)
	# print(count)
	result=set(result)
	# print("............sort.........")
	# print(result)
	count=0
	final=[]
	for i in result:
		print(i)
		if "!" in i:
			i = i[1:].replace(" ","")
			final.append(i)
			count = count+1
	for j in final:
		if "}" in j:
			index=j.index("}")
			j=j[:index]
			final.append(j)
	bgcolor = sorted(final)
	print(bgcolor)
	#     count=count+1
	#     print(result)
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
	elif inputdata == "list":
		list1(data)
	# image(data)
	


if __name__ == '__main__':
	main()