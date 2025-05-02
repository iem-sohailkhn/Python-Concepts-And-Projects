f = open("file.txt")
content = f.read()
if "Twinkle" in content:
    print("The Word Twinkle Is Present In The File")
else:
        print("The Word Twinkle Is Not Present In The File")

f.close()