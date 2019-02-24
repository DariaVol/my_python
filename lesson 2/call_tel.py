c=int(input("Введите код города:\n"))
def call_tel(x):
    if x==343:
        return 15
    elif x==381:
        return 18
    elif x==473:
        return 13
    elif x==485:
        return 11
    else:
        print ("я не знаю тариф этого города")

print(call_tel(c))    
