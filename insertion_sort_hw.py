myList=["apple","kiwi","banana","pie","date"]

print(f"Original List: {myList}")

n=len(myList)
for i in range(1,n):
    insert_index=i
    current_val=myList.pop(i)

    for j in range(i-1, -1, -1):
        if len(myList[j])>len(current_val):
            insert_index=j
    
    myList.insert(insert_index,current_val)

print(f"Sorted List: {myList}")