st = input(" введите строку : ")

st = st.casefold()

rev_str = reversed(st)

if list(st) == list(rev_str):
   print("Строка является палиндромом")
else:
   print("Строка не является палиндромом")
