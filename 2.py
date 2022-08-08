def pascal(n):
    if n==0:
        return [1]
    if n==1:
        return [1,1]
    list = [1,1]
    temp = [1,1]
    for i in range(2,n+1):
        list = temp
        temp = [1]
        for i in range(len(list)-1):
            temp.append(list[i]+list[i+1])
        temp.append(1)
    return temp

n = 10
for i in range(n):
    print(pascal(i))

