# a - счетчик
a: int = 0

str1 = input(" введите строку : ")
str2 = input(" введите символ : ")




for i in str1:
    if i == str2:
        a += 1

print(a)
