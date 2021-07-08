name= input("Enter the name of the student: ")
a=int(input("Marks in engish: "))
b=int(input("Marks in maths: "))
c=int(input("Marks in computer: "))
d=int(input("Marks in science: "))
e=int(input("Marks in social: "))
print("Name of the Student: ",name)
avg=(a+b+c+d+e)/5
print ("Average Marks Obtained: ",avg)
if(avg>=70):
      print("Grade Obtained: A")
elif(avg>59 and avg<70):
      print("Grade Obtained: B")
elif(avg>49 and avg<60):
      print("Grade Obtained: C")
elif(avg>42 and avg<50):
      print("Grade Obtained: D")
elif(avg>39 and avg<43):
      print("Grade Obtained: E")
elif(avg>=0 and avg<40):
      print("Grade Obtained: F")
else:
      print("INVALID MARKS!")
