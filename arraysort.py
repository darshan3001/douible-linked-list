arr1 = list(map(int,input().split(',')))
arr2 = []
temp = 0
print('elements before sorting: ')
for i in range(0,len(arr1)):
    print(arr1[i],end=' ')
for i in range(0,len(arr1)):
    for j in range(i+1,len(arr1)):
        if(arr1[i] > arr1[j]):
            temp = arr1[i]
            arr1[i] = arr1[j]
            arr1[j] = temp
print('\nelements after sorting: ')
for i in range(0,len(arr1)):
    print(arr1[i],end=' ')


