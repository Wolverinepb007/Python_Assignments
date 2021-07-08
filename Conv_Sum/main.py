import greeting             #importing greeting function
import addition             #importing addition function
import reverse              #importing reverse function
import validation           #importing validation function
import conversion           #importing conversion function
import conclusion           #importing conclusion function

greeting.Greeting()    #Execution of the greeting function

continueLoop=True
while continueLoop==True:

            continueFirstNum=False
            while continueFirstNum==False:
                        try:
                                    number1=int(input("Enter the first decimal number: "))  #input for the first decimal
                                    number1=validation.ValidNum(number1)    #Executing the validation function                            
                                    print("\n")
                                    continueFirstNum=True
                        except:
                                    print("\n")
                                    print("Invalid Input!!")
            continueSecondNum=False
            while continueSecondNum==False:
                        try:            
                                    number2=int(input("Enter the second decimal number: ")) #input for the second decimal
                                    number2=validation.ValidNum(number2)    #Executing the validation function
                                    print("\n")
                                    continueSecondNum=True
                        except:     
                                    print("\n")
                                    print("Invalid Input!!")
            
            num1=conversion.DecimalToBinary(number1)                        #Executing the conversion function
            num2=conversion.DecimalToBinary(number2)

            binaryNum1=reverse.Reverse(num1)                                #Executing the reverse function
            binaryNum2=reverse.Reverse(num2)
            
            lastSum=addition.BinaryAddition(binaryNum1,binaryNum2)         #Executing the addition function

            print("Binary equivalent of first decimal number (",number1,") is: ",binaryNum1)    #printing the binary equivalent of first decimal
            print("\n")
            print("Binary equivalent of second decimal number (",number2,") is: ",binaryNum2)   #printing the binary equivalent of second decimal
            print("\n")
            print("sum of binary number is: ",lastSum) #printing the binary equivalent of the sum of first and second decimal
            print("\n")

            toContinue=input("Do you wish to continue the program(Yes/No)??? ").lower()
            if toContinue=="no":
                        break
conclusion.Conclusion() #Executing the Conclusion function

