contLoop=True
allNum=[]
sumEven=0
sumOdd=0
while contLoop==True:
    N=int(input("Enter the number:"))
    allNum.append(N)
    conti=input("Do you wish to continue??(Y/N)")
    if conti=="N" or conti=="n":
        break
    #print("List of numbers: ",allNum)
    #print("Number of elements: ",len(allNum))
    for i in range(len(allNum)):
        #print("index of list :",i)
        #print("Value of list are:",allNum)
        if(allNum[i]%2==0):
            sumEven=sumEven+allNum[i]
        else:
            sumOdd=sumOdd+allNum[i]
print("Sum of even numbers= ",sumEven)
print("Sum of odd numbers= ",sumOdd)
            
