first, second, third = input('Введите три целых числа '). split()
first = int(first)
second = int(second)
third = int(third)
if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')