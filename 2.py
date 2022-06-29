a = input(" введите строку : ")
b = input(" введите строку : ")



if(len(a) == len(b)):

    s1 = sorted(a)
    s2 = sorted(b)

    if(s1 == s2):
        print(a + " и " + b + " Являются анаграмой.")


else:
    print(a + " и " + b + " не являются анаграмой")
