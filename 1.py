
def fun(list):
    sume=0
    sumo=0
    for i in range(len(list)):
        if i%2==0:
            sume=sume+list[i]
        else:
            sumo=sumo+list[i]
    print("Sume=",sume)
    print("sumo=",sumo)

fun([1,2,3,4,5,6])



