num=int(input("Enter a number: "))
i=0
n=2
while(n<num):
    if(num%n==0):
        i+=1
        break
    n+=1

if(i==0 and num !=1 and num !=0):
    print(num," is a prime number.")
elif(num ==1 or num ==0):
    print(num," is neither prime nor a composite number.")
else:
     print(num," is not a prime number.")
     
        
