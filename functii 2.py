from re import I


print('N mai mare ca M')

n=int(input('introdu n='))
m=int(input('introdu m='))

def factorial(nr):
    p=1
    s=0
    for i in range(1,nr+1):
        p*=i
    return p