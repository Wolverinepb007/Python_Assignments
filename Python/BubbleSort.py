List=[5,1,2,0,8]
sorted = False
while sorted == False:
    num_swaps=0
    for i in range(1,len(List)):
        if List[i-1]>List[i]:
            temp = List[i-1]
            List[i-1]=List[i]
            List[i]= temp
            num_swaps = num_swaps+1
    if num_swaps == 0:
        sorted = True
    else:
        sorted = False
print(List)
      
