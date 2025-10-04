a = int(input())
b = int(input())
c = int(input())

# поиск максимума
if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
else:
    print(c)

# встроенные функции для поиска максимума, минимума, модуля числа
mx = max(a, b, c)
mn = min(a, b, c)
m = abs(a)
