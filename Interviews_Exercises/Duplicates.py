# 7. Write a Python program to print set of duplicates in a list
l =[1,2,3,3,4,5,6,6,7]
print(set([x for x in l if l.count(x)>1]))