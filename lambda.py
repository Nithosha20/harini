double=lambda x: x*2
triple=lambda x: x*3
quadruple=lambda x: x*4
funcs=[double,triple,quadruple]
def apply_all(funcs,value):
    for f in funcs:
        value=f(value)
    return value
n=int(input())
print(apply_all(funcs,n))
