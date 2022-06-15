list1=input('Enter a string: ')
list2=[]
for i in range(len(list1)):
    if list1[i] not in list2:
        list2.append(list1[i])
    else:
        pass
for i in range(len(list2)):
    print(list2[i])