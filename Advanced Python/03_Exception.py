
try:
  a = int(input("Enter a number:  "))
  print(a)

except Exception as e:
  print(e)
  #If Try is Successful than else will run
else:
  print("Thank U...")