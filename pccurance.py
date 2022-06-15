strr = "Programm"
dic = {}
for ele in strr:
    if ele in dic:
        dic[ele] += 1
    else:
        dic[ele] = 1
print(str(dic))