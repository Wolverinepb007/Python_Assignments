#designing the reverse function
def Reverse(numList):
            trueBinary=[]
            trueBinaryNum=""
            for i in range(len(numList)-1,-1,-1):
                        trueBinary.append(numList[i])
                        trueBinaryNum=trueBinaryNum+str(numList[i])
            return trueBinaryNum
