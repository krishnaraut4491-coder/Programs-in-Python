filename = "output.txt"
with open(filename, "wt") as write2file:
    text = input("Enter text to write to the file: ")
    write2file.write(f"{text}\n")

print(f"Data successfully written to {filename} \n")

with open(filename, "at") as append2file:
    text2append = input("Enter additional text to append: ")
    append2file.write(text2append)

print("Data successfully appended.\n")

with open(filename, "rt") as file2read:
    content = file2read.read()
    print(f"Final content of {filename}:\n{content}")
