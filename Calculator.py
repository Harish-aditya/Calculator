while True:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    z = int(input("Please select the operation: \n 1 - Addition\n 2 - Subtraction\n 3 - Multiplication\n 4- Division\n:"
                  ))


    def calculator(a, b, c):
        while True:
            if type(a) == float and type(b) == float:
                if c == 1:
                    R = a + b
                    print(R)
                elif c == 2:
                    R = a - b
                    print(R)
                    break
                elif c == 3:
                    R = a * b
                    print(R)
                    break
                elif c == 4:
                    R = a / b
                    print(R)
                    break
                else:
                    print("Enter only the above option.")
                    break



            else:
                print("Enter only numerical Values")


    calculator(x, y, z)
    F = int(input("If you want to exit enter 0:"))
    if F == 0:
        break
    else:
        continue
