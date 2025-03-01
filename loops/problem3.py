# todo MULTIPLICATION TABLE PRINTER

num=int(input("Enter number"))
for i in range(1,11):
    if i == 5:
        continue
    print(f"{num} x {i} = {num*i}")