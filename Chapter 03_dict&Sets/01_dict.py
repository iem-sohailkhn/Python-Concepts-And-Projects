marks = {
    "Sui":100,
    "Suffi":80,
    "Umar":70
}
print(marks,type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Sui":99,"Rohan":88})
print(marks)
print(marks.get("Sui"))

print(marks.get("Sui2"))#print None
print(marks["Sui"])
print(marks["Sui2"])#print error


