num = int(input('Enter the number of elements should be present in the array: '))
arr=[]
print(f'Enter {num} elements: ')
for i in range(num):
    arr.append(int(input()))
print('the array is: ',arr)
print('Enter the value to delete: ')
val = int(input())
if val in arr:
    arr.remove(val)
    print(f'The array after {val} is removed is: ')
    for i in range(num-1):
        print(arr[i],end=' ')
else:
    print(f'{val} is not present in the arraY')
    