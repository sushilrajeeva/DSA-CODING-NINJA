#looks like this for n = 4

'''

   *
  ***
 *****
*******

'''

n = int(input("Enter number of rows in hill triangle : "))

for row in range(n):
    for column in range(row,n-1):
        print(" ", end=" ")
    for column in range(row+1):
        print("*", end=" ")
    for column in range(row):
        print("*", end=" ")
    print()