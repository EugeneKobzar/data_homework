numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
with open("numbers.txt", "w") as f:
    for n in numbers:
        f.write(str(n) + "\n")
print("Done!")