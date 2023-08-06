#looks like this for n = 4

'''

   *
  **
 ***
****

'''

n = int(input("Enter number of rows in reverse increasing right triangle : "))

for row in range(n):
    for column in range(row,n-1):
        print(" ", end=" ")
    for column in range(row+1):
        print("*", end=" ")
    print()