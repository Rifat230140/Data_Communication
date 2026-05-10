# Take binary data from user
data = input("Enter binary data: ")

# Count number of 1's
ones = data.count('1')

# Generate Even Parity Bit
parity = '0' if ones % 2 == 0 else '1'

# Create codeword
codeword = data + parity

# Display results
print("\nData:", data)
print("Parity Bit:", parity)
print("Transmitted Codeword:", codeword)

# Receiver Side Checking
if codeword.count('1') % 2 == 0:
    print("No Error Detected")
else:
    print("Error Detected")
