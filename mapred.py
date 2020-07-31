string1 = str(input("enter a string"))

#print(string1)

#spliting data with imaginary value of 1
string1 = string1.split()

#sorting
string1.sort()

#empty info dictionary
reduceddata = {} 

#reduce
for temp in string1:
	if temp in reduceddata.keys():
		reduceddata[temp]+=1
	else:
		reduceddata.update({temp : 1})

print(reduceddata)
