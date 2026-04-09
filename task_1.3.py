lines = []
print("Enter text (empty line = save and exit):")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
with open("output.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
print("Saved to output.txt!")