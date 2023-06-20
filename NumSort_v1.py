# Number Sorting Algorithm using eval()

def sort2():
    numbers = []
    while True:
        value = input("Enter a number (type 'done' to sort the numbers, 'exit' to quit): ")
        if value.lower() == "exit":
            print("Exiting the program...")
            break
        elif value.lower() == "done":
            if numbers:
                numbers_sorted = sorted(numbers, key=lambda x: eval(x), reverse=True)
                print("Sorted numbers:")
                print("\n".join(numbers_sorted))
            else:
                print("No numbers entered.")
            break
        else:
            numbers.append(value)