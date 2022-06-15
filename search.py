str = 'Darshan is a good boy'.split()
li=[]
search = input('Enter the word to search: ')

if search in str:
    print(search, ' is preasent in the statement')
else:
    print(search, ' is not present in the statement')
