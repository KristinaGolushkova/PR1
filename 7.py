#счетчик
c = 0
#последнее вхождение
ind = -1

a = input(" введите строку : ")
b = input(" введите символ : ")



for i in a:
    if i == b:
        ind = c
print(ind)
