n = int(input("Enter number of rows: "))

data = [input(f"Row {i+1}: ") for i in range(n)]

lrc = ""

for i in range(len(data[0])):
    count = sum(row[i] == '1' for row in data)
    lrc += '0' if count % 2 == 0 else '1'

print("\nLRC:", lrc)

# Receiver Check
data.append(lrc)

error = False

for i in range(len(data[0])):
    count = sum(row[i] == '1' for row in data)

    if count % 2 != 0:
        error = True

print("Error Detected" if error else "No Error")
