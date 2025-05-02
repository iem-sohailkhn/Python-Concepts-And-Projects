with open("log.txt","r") as f:
    content = f.read()

if("Python" in content):
    print("Yesss we Find Out The Word Python In Log File Yups")
else:
    print("No  we Can't Find Out The Word Python In Log File Yups")

