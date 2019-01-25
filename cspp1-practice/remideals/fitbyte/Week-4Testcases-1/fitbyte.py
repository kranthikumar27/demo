# def dailyActivites(energy):
# 	list_1 = []
# 	list_2 = []
# 	# print(energy)
# 	for i in energy:
# 		print(i)
# 		list_1.append(i[1])
# 	print(list_1)
# 	# for each in list_1:
# 		# print(each)
		

def dailyActivites(energy):
	# print(energy)
	dict_1 = {}
	list_1= []

# 	for i in energy:
# 		list_2.append(i.split(",")[1])
# 	print(list_2)
	for each in energy:
		# print(each)
		
		if len(each)>1:
	# [each.split(",")[0] for each in energy]
	# print(each)
			if each[0] not in dict_1:
				dict_1[each[0]] = each[1]
		else:
			list_1.append(each[0])	
	# print(list(dict_1.values()))
	# print(dict_1)
	list_2 = []
	# (dict_1.values().split(","))
	# print(list_2)
	# for each in dict_1:
	# 	# print(each)
	for i in dict_1.values():
			# print("kranthi")
			# print(i)
		list_2.append(i.split(','))
	# print(list_2)
	# print("kranthiiiiiiiiii")
	# print(list_2[0][1])

	for each in list_2:
		# print(each)
		# if each == dict_1.keys():
		# if each == "Food":
		for i in dict_1:
			# for j in i:
			# 	print(j)
		# print("FFFFFFFFFFFFF")
			# for x in xrange(1,10):
			# 	pass
			# print(dict_1.keys())
			print(i)
			print(str(each[1]) + ":")
			print("-"+ str(each[2]) +":"+str(each[0]))
		break

		# elif each == "Water":
		# 	print("water:")
		# 	# for x in xrange(1,10):
		# 	# 	pass
		# 	print(str(list_2[0][1]) + ":")
		# 	print("-"+ str(list_2[0][2]) +":"+str(list_2[0][0]))
		# break
		# if each == 
		

		# except:
		# 	list_1.append(each)
		# 	print(list_1)
		
	# print(tokens)
def main():
	data = int(input())
	caloriesintake=[]
	for i in range(data):
		# tokens=input().split(",")
		# print(tokens)
		caloriesintake.append(input().split())
	# print(caloriesintake)
	dailyActivites(caloriesintake)

if __name__ == '__main__':
	main()