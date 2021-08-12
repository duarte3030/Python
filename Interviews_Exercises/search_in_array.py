# 9. Given an array arr[] of n elements, write a Python function to search a given element x in arr[].
def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            print(i)
            print(arr[i])
            return i

    print("not present")
l = [1,2,3,4,4,56,7]
search(l,56)
