## AND operator!

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def is_power_of_two(n):
    return bool(n) and (n & (n - 1)) == 0

#Flipping bits 
# XORing a number with a mask can be used to flip specific bits in the number.
def flip_bits(n, k):
    return n ^ ((1 << k) - 1)

#Clear lower bits
# The function clear_lowest_set_bit is designed to clear the lowest (rightmost) set bit in a given integer n. 
# In other words, it changes the rightmost 1 to 0 while leaving all other bits unchanged.

def clear_lowest_set_bit(n):
    return n & (n - 1)

#Getting the lowest set bit:
#lowest_set_bit is designed to find the position of the lowest (rightmost) set bit in a given integer n,
# and return it as a new integer that has only that bit set.
def lowest_set_bit(n):
    return n & (-n)



print("Bitwise AND Operation Result: ", a & b)
print("Bitwise OR Operation Result: ", a|b )
print("Bitwise XOR Operation Result: ", a^b )
print("Bitwise NOR Operation Result: ", ~(a^b) )
print("Bitwise NOT Operation ON A Result: ", ~a )
print("Bitwise RSHIFT A BY 1 Operation Result: ", a>>1 )
print("Bitwise LSHIFT A BY 1 Operation Result: ", a<<1 )

##CHECKING IF THE NUMBER IS DIVISIBLE BY 2
print("Using Bitwise to check remainder of ", a ,"is odd or even : ", (a&1 == 0))

# Multiplying by 2 using left shift
print("Multiplication of", a, "by 2:", a << 1)

# Dividing by 2 using right shift
print("Division of", a, "by 2:", a >> 1)

# Multiplying by 4 using left shift
print("Multiplication of", a, "by 4:", a << 2)

# Dividing by 4 using right shift
print("Division of", a, "by 4:", a >> 2)

# Bitwise to check number of set bits
print("Number of set bits in ", a, " :", count_set_bits(a))

print("Number of set bits in ", b, " :", count_set_bits(b))

#Checking if a given number is power of 2

print("is 1 a power of 2 - ", is_power_of_two(1))   # Output: True (2^0 = 1)
print("is 2 a power of 2 - ",is_power_of_two(2))   # Output: True (2^1 = 2)
print("is 16 a power of 2 - ", is_power_of_two(16))  # Output: True (2^4 = 16)
print("is 7 a power of 2 - ", is_power_of_two(7))   # Output: False (Not a power of two)
print("is 0 a power of 2 - ", is_power_of_two(0))   # Output: False (Not a power of two)

#Fliping bits of a number with k
print("flipping number 55 with k = 3 gives : ", flip_bits(55, 3))

#clear_lowest_set_bit(27) 
# n = 27, which in binary is 11011.
# (n - 1) is 26, which in binary is 11010.
# 27 & 26 performs the bitwise AND operation between 11011 (27 in binary) and 11010 (26 in binary). The result is 11010, which is 26 in decimal.
# The function returns 26.
# So, the result of clear_lowest_set_bit(27) is 26, which is 11010 in binary. The rightmost 1 in 27 has been cleared to 0.

print("Clearning lowest set bit of 27 we get : " , clear_lowest_set_bit(27))

#Getting Lowest set bit
# n = 26, which in binary is 11010.
# -n is -26, which in two's complement binary representation is 00110 (Note: Two's complement negation of n is equivalent to finding the two's complement representation of -n).
# 26 & -26 performs the bitwise AND operation between 11010 (26 in binary) and 00110 (-26 in binary). The result is 00010, which is 2 in decimal.
# The function returns 2.
# So, the result of lowest_set_bit(26) is 2, which represents the position of the lowest set bit in the binary representation of 26. In this example, the lowest set bit is at position 2 (from the right).

print("Getting lowest set bit of 26 : ", lowest_set_bit(26))