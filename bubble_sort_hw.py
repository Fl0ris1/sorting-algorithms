arr1=[64,34,25,12,22,11,90]

def bubbleSort(arr):
    n=len(arr)
    for i in range(0,n):
        swapped=False
        for j in range(n-i-1):
            if arr[j]<arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                swapped=True
                
        if swapped==False:
            break
        
        

print(f"Original: {arr1}")
bubbleSort(arr1)
print(f"Sorted From Highest To Lowest: {arr1}")