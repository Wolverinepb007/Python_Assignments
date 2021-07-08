def ValidNum(number):
            while number<0 or number>255:
                        print("\n")
                        print("Invalid Input!!")
                        number=int(input("Please enter valid number (0 to 255):  "))
            return number
