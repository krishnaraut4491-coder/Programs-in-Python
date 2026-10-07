try:
    with open("sample.txt", "rt") as samplefile:
        print("Reading file content")

        line1 = samplefile.readline()
        print(f"Line 1: {line1.strip()}")

        line2 = samplefile.readline()
        print(f"Line 2: {line2.strip()}")
        
except FileNotFoundError:
    print(f"Error: the file 'sample.txt' was not found.")