words = ["##","###"]
with open("file.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"hy how are")
with open("file.txt","w") as f:
    f.write(content)