str='ProGraMMinG'
x=[]
for i in range(len(str)):
    if(str[i].isupper()):
        x.append(str[i].lower())
    elif(str[i].islower()):
        x.append(str[i].upper())
for i in range(len(x)):
    print(x[i],end='')
