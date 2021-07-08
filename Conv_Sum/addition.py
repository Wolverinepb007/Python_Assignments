#designing the addition function
import reverse      #importing reverse function
def AndGate(a,b):
            return a&b
def OrGate(a,b):
            return a|b
def XorGate(a,b):
            return a^b

def BinaryAddition(num1,num2): #Adding the binary numbers
            Binary1=[]
            cin=0
            for i in range(len(num1)-1,-1,-1):
                        a=int(num1[i])
                        b=int(num2[i])
                        sum1=XorGate(a,b)
                        finalSum=XorGate(sum1,cin)
                        cOut1=AndGate(cin,sum1)
                        cOut2=AndGate(a,b)
                        finalcOut=OrGate(cOut1,cOut2)
                        cin=finalcOut
                        Binary1.append(finalSum)

            Binary2=reverse.Reverse(Binary1)
            return Binary2
            
            
