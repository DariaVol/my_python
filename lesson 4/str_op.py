s="У лукоморья 123 дуб зеленый 456"
print('Позиция буквы Я в строке ',s.index('я'))
a=s.count("у")
a1=s.count("У")
print('Буква У встречается',a+a1,'раз(а)')
if s.isdigit():
    print (s)
else:
    print (s.upper())

if len(s)>4:
    print (s.lower())
else:
    print (s)
    
print(s.replace("У", "О"))
