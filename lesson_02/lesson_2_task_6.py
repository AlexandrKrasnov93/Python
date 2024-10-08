ist = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
new_list = []
for i in ist:
    if i < 30 and i % 3 == 0:
        new_list.append(i)


print(new_list)
