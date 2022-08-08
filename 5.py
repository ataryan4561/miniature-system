from re import L


def f(str,nu,dict):
    ld=str.split()
    for i in range(len(ld)):
        for key in dict:
            if ld[i]==key:
                ld[i]=dict[key]
    return ld

luv = f("How are you doing?",2,{"are": "am", "you": "I"})
for i in range(len(luv)):
    print(luv[i],end=" ")