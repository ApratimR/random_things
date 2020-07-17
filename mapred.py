string1 = str(input("enter a string"))

print(string1)

#spliting data
string1 = string1.split()


string1.sort()


reduceddata = {} 

for temp in string1:
	if temp in reduceddata.keys():
		#reduction
		reduceddata[temp]+=1
	else:
		#maps
		reduceddata.update({temp : 1})

print(reduceddata)