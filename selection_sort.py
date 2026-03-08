myList=[]
for i in range(10):
    inp=int(input(f"Input A Number: "))
    myList.append(inp)

print(f"Original List {myList}")
n=len(myList)
for i in range(n-1):
    minIndex=i
    for j in range(i+1,n):
        if myList[j]<myList[minIndex]:
            minIndex=j
    min_value=myList.pop(minIndex)

    myList.insert(i,min_value)

print(f"The sorted list is {myList}")