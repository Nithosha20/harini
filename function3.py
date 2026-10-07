def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
d={1:add,2:sub,3:mul}
for key,value in  d.items():
    print(key,":",value)
op=int(input("enter choice:"))
result=d[op](10,5)
print("result:",result)
