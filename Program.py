newArray = []
size = int(input("Введите размер массива: "))
for i in range(size):
    s = input("Введите элемент массива: ")
    if len(s) <= 3:
        newArray.append(s)
print(*newArray)
