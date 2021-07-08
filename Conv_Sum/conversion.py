#designing the conversion function
def DecimalToBinary(decimalNum):     #Converting decimal numbery to binary
            bit=[]
            count=0
            while count!=8:
                        R=decimalNum%2
                        bit.append(R)
                        decimalNum=decimalNum//2
                        count+=1
            return bit
