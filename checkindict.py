dict={0:'zero',1:'one',2:'two',3:'three'}
x=int(input('Enter an input: '))
if x in dict.keys():
    print(True)
else:
    print(False)