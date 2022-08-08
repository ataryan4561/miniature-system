def mapi(str):
    ls = str.split()
    return ls[1]+"_"+ls[0]

names = ["gupta aryan","falak neha","sharma navi"]
lsa =map(mapi,names)
print(list(lsa))



