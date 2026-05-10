# Sender Side

data = input("Enter binary data: ")

ones = data.count('1')

# Even Parity
if ones % 2 == 0:
    parity = '0'
else:
    parity = '1'

# Codeword
codeword = data + parity

print("\nParity Bit:", parity)
print("Transmitted Codeword:", codeword)


# Receiver Side

received = input("\nEnter received codeword: ")

# Error Checking
if received.count('1') % 2 == 0:
    print("No Error Detected")
else:
    print("Error Detected")
