first=float(input("Введите первое число:\n"))
second=float(input("Введите второе число:\n"))
def my_max(x,y):
    """Вычисление большего числа из двух"""   
    if x>y:
        return x
    else:
        return y

print(my_max(first,second))
                 
           
