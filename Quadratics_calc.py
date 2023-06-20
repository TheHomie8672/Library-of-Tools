import math

def quadratics_calc(itr=1):
    while True:
        if itr > 1:
            exit_choice = input("Would you like to exit the program? (yes/no): ")
            if exit_choice.lower() == "yes":
                return
        
        a = float(input("Enter the value of 'a': "))
        b = float(input("Enter the value of 'b': "))
        c = float(input("Enter the value of 'c': "))

        n = int(input("Enter the total number of squared 'x's: "))
        symbol = input("Enter the positive (+) or negative (-) symbol: ")

        x = symbol + str(n)

        equation = f"{x}^2 + {b} * {x} + {c}"
        print("Quadratic Equation:", equation)

        # Step 1: Calculate the discriminant
        discriminant = b**2 - (4 * a * c)
        print("Step 1: Calculate the discriminant")
        print(f"Discriminant = {b}^2 - 4 * {a} * {c}")
        print("             =", discriminant)

        # Step 2: Check the nature of the roots
        if discriminant < 0:
            print("The quadratic equation has no real solutions.")
        else:
            # Step 3: Calculate the roots
            x1 = (-b + math.sqrt(discriminant)) / (2 * a)
            x2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print("Step 2: Check the nature of the roots")
            print("        The quadratic equation has real solutions.")

            print("Step 3: Calculate the roots")
            print(f"Root 1 = (-{b} + sqrt({discriminant})) / (2 * {a})")
            print("        =", x1)
            print(f"Root 2 = (-{b} - sqrt({discriminant})) / (2 * {a})")
            print("        =", x2)
        
        itr += 1

        how_to_solve = input("Do you want to see the step-by-step solution? (yes/no): ")
        if how_to_solve.lower() == "yes":
            print("Step-by-Step Solution:")
            print("Step 1: Calculate the discriminant")
            print(f"    Discriminant = {b}^2 - 4 * {a} * {c}")
            print("                 =", discriminant)
            print("Step 2: Check the nature of the roots")
            if discriminant < 0:
                print("    The quadratic equation has no real solutions.")
            else:
                print("    The quadratic equation has real solutions.")
                print("Step 3: Calculate the roots")
                print(f"    Root 1 = (-{b} + sqrt({discriminant})) / (2 * {a})")
                print("            =", x1)
                print(f"    Root 2 = (-{b} - sqrt({discriminant})) / (2 * {a})")
                print("            =", x2)
    



