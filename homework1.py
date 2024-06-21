example = '123456789'
e = len(str(example)) / 2
print(example[0])
print(example[-1])
print(example[int(e):])#Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
print(example[::-1])
print(example[1::2])