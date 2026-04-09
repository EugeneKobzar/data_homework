with open("text.txt", "r") as f:
    text = f.read()
count = text.upper().count("A")
print("Letter A appears:", count, "times")