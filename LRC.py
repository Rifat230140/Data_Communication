def lrc_check(data):

    lrc = ""

    for col in range(len(data[0])):

        ones = 0

        for row in data:
            if row[col] == '1':
                ones += 1

        if ones % 2 == 0:
            lrc += '0'
        else:
            lrc += '1'

    return lrc


# Sender Side
n = int(input("Enter number of rows: "))

data = []

for i in range(n):
    data.append(input("Enter row: "))

lrc = lrc_check(data)

print("\nLRC:", lrc)

codeword = data + [lrc]

print("\nTransmitted Block:")
for row in codeword:
    print(row)


# Receiver Side
received = []

print("\nEnter received block:")

for i in range(n + 1):
    received.append(input())

check = lrc_check(received)

print("Receiver LRC:", check)

if check == '0' * len(received[0]):
    print("No Error Detected")
else:
    print("Error Detected")
