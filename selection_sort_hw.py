list1=[]
for i in range(4):
    input1=float(input(f"Input A Number: "))
    list1.append(input1)
    
for i in range(len(list1)-1):
    lowIndex=i
    
    for j in range(i+1,len(list1)):
        if list1[j]<list1[lowIndex]:
            lowIndex=j
            
    low_value=list1.pop(lowIndex)

    list1.insert(i,low_value)

print(list1)