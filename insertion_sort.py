myList=[]

for i in range(8):
    inp=int(input("Input A Value: "))
    myList.append(inp)

print(f"Original List: {myList}")
n=len(myList)
for i in range(1,n):
    insert_index=i
    current_value=myList.pop(i)
    for j in range(i-1, -1, -1):
        if myList[j]>current_value:
            insert_index=j
    
    myList.insert(insert_index,current_value)

print(f"Sorted List: {myList}")