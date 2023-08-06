
#looks like this for n = 4

'''

****
***
**
*

'''



n = int(input("Enter number of rows in the decreasing right triangle : "))

for row in range(n+1):
    for column in range(n-row):
        print("*", end=" ")
    print()