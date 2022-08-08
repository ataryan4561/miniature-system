def linear_search(arr,low,high,x):
    if high<low:
        return -1
    if  arr[high]==x:
        return high
    return linear_search(arr,low,high-1,x)

print(linear_search([1,2,3,4,5,6],0,5,3))