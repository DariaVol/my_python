import math
r=int(input("Количество знаков после запятой: "))
num=math.pi
def fun(r):
    number=round(num,r)
    return f'{number}'
print(fun(r))
