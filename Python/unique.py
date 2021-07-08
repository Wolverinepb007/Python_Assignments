uList=[]
newList=[1,1,2,3,3]
for each in newList:
    print(each)
    if each not in uList:
        uList.append(each)
print(uList)
