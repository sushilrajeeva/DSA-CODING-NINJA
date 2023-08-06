n = 5
upperHillRows = int(n/2 + 1)
lowerHillRows = int(n/2)

for row in range(upperHillRows):
    for column in range(row, upperHillRows-1):
        print(" ", end="")
    for column in range(row+1):
        print("*", end="")
    for column in range(row):
        print("*", end="")
    print()
    
for row in range(lowerHillRows):
    for column in range(row+1):
        print(" ", end="")
    for column in range(lowerHillRows-row):
        print("*", end="")
    for column in range(lowerHillRows-row-1):
        print("*", end="")
    print()