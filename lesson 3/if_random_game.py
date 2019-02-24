import random
x=int(input('Введите число: '))
if x==random.randint(1,4):
    print ('Победа')
elif x>random.randint(1,4):
    print ('введенное число больше,попробуй еще раз')
else:
    print ('введенное число меньше, попробуй еще раз')
