num = int(input('Enter the number of elements:'))
arr = []
print('Enter ',num,' elements: ')
for i in range(num):
    element = input()
    arr.append(element)
print('the number is : ')
for i in range(num):
    print(arr[i],end='')
    
