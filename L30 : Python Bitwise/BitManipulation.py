#Swapping two numbers without a temp variable | using bit

def swap_using_bitwise(x, y):
    print("Before swapping: x =", x, "y =", y)

    # Perform swapping using bitwise XOR operation
    x = x ^ y
    y = x ^ y
    x = x ^ y

    print("After swapping: x =", x, "y =", y)

if __name__ == "__main__":
    try:
        input_x = int(input("Enter the value of x: "))
        input_y = int(input("Enter the value of y: "))
        swap_using_bitwise(input_x, input_y)
    except ValueError:
        print("Invalid input. Please enter valid integers.")
