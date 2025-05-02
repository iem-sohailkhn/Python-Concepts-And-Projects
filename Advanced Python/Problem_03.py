n = int(input("Enter a number of table: "))

table = [f"{n} X {i}  = {n*i}" for i in range(1,11)]

for line in table:
    print(line)