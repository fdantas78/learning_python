gradeDict = {'Kelly':89,'David':65,'Jack':95,'Samantha':78}
print(gradeDict)

print(gradeDict['David'])

gradeDict['David'] = 56
print(gradeDict['David'])

gradeDict['Jessy'] = 92
print(gradeDict)

del gradeDict['David']
print(gradeDict)


gradeDict['Kelly'] = [89,88]
gradeDict['Jack'] = [95,87]
gradeDict['Samantha'] = [78,89]
gradeDict['Jessy'] = [[92,97],99]
print(gradeDict)
print(gradeDict['Jessy'][0][1])


