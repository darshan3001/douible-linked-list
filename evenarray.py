ab = list(map(int,input().split(',')))
for i in range(len(ab)):
    if(i%2==0):
        print(i,'are even numbers')
    else:
        print(i,'are odd numbers')