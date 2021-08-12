# 3. Write a sorting function without using the list.sort function

datalist = [100,5,7,325,800,5,3,56,6]
newlist = []
while datalist:
    newlist.append(max(datalist))
    datalist.remove(max(datalist))
print(newlist)