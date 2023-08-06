#looks like this for n = 4

'''

*
**
***
****

'''

n = int(input("Enter the number of rows in increasing right triangle : "))

for row in range(n):
    for column in range(row+1):
        print("*", end=" ")
    print()
