film=str(input("Выберете фильм:\n"))
date=str(input("Сегодня или завтра?\n"))
time=str(input("Выберете время:\n)"))
num=int(input("Укажите кол-во билетов:\n"))

print ("Выбрали: ", film, "День: ", date, "Время: ", time, "Кол-во билетов: ", num)

def price(num):         
    if film=='Пятница':
        if time=='12':
            return 250*num
        if time=='16':
            return 350*num
        if time=='20':
            return 450*num
    if film=='Чемпионы':
        if time=='10':
            return 250*num
        if time=='13':
            return 350*num
        if time=='16':
            return 350*num
    if film=='Пернатая банда':
        if time=='10':
            return 350*num
        if time=='14':
            return 450*num
        if time=='18':
            return 450*num
    else:
        return "Ошибка"

if price(num)=='Ошибка':
    print (price(num))
else:
    if date=='завтра':
        if num>=20:
            price_disc=int(price(num)*0.8)
            print("Со скидкой: ", price_disc)
        else:
            price_disc=int(price(num)*0.95)
            print("Со скидкой: ", price_disc)
    else:
         if num>=20:
            price_disc=int(price(num)*0.8)
            print("Со скидкой: ", price_disc)
         else:
            print (price(num))

