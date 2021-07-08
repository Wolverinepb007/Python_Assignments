a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a<b:
    temp=a
    a=b
    b=temp
R=1
while R>0:
    R=a%b
    if R==0:
        break
    else:
        a=b
        b=R
print("HCF: ",b)
