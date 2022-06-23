str1 = input(" введите строку : ")
str2 = input(" введите строку : ")


# функция количества строк
if(len(str1) == len(str2)):

    # Сортируем обе строки
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if(sorted_str1 == sorted_str2):
        print(str1 + " и " + str2 + " Являются анаграмой.")


else:
    print(str1 + " и " + str2 + " не являются анаграмой")
