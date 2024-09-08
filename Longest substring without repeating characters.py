import operator as b
def getans(name):
    res_set=set()
    res=0
    l=0
    for i in range(0,len(name)):
        while b.contains(res_set,name[i]):
            res_set.remove(name[l])
            l+=1
            
        
        res_set.add(name[i])
        
        res=max(res,len(res_set))
    return res
name=input("Enter the String: ")
result=getans(name)
print(f"Your answer is {result}")
