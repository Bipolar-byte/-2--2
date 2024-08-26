First = int(input("Число1: "))
Second = int(input("Число2: "))
Third = int(input("Число3: "))
if First == Second == Third:
    print("Количество совпадений: 3")
elif First == Second or Second == Third or First == Third:
    print("Количество совпадений: 2")
else:
    print("Совпадений не найдено")


