ch=int(input("Введите число:\n"))
def get_parity(x):
    """Определяет целое число на четность"""
    if x%2==0:
        return ("четное")
    else:
        return ("нечетное")

print(get_parity(ch))
