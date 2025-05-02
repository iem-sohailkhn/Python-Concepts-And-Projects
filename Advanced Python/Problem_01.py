n = int(input("Enter a number..."))

table =[f"{n} X {i} = {n*i}" for i in range(1,11)]
for line in table:
   
  with open("table.txt","a") as f:
   f.write(f"{line}\n")
   