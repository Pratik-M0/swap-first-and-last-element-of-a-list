arr = [10,20,30,2,4,666,1,89]

#finding maximum element

max = arr[0]
n = len(arr)

for i in range(1,n):
    if arr[i] > max:
        max = arr[i]

print("Maximum Element is : ",max)

#finding minimum element

min = arr[0]

for i in range(1,n):
    if arr[i] < min:
        min = arr[i]

print("Minimum Element is : ",min)