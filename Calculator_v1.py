from statistics import mean, median, mode, stdev
import math
import sympy as sp
from sympy import Symbol, solve, Eq, sqrt, symbols
from sympy.parsing.sympy_parser import parse_expr

def solve_equation():
    equation = input("Enter an equation: ").replace(" ", "")  # Remove whitespace from the equation
    equation = equation.replace("SR", "math.sqrt")  # Replace "SR" with "math.sqrt" for square root symbol
    try:
        result = eval(equation)
        print("Solution:", result)
    except Exception as e:
        print("Error:", str(e))


def calculate_range(data):
    return max(data) - min(data)

def calculate_data_range():
    data = []

    # Collect data samples
    while True:
        value = input("Enter a data value (or 'done' to finish): ")
        if value.lower() == "done":
            break
        try:
            data.append(float(value))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if len(data) < 2:
        print("Insufficient data to calculate the range.")
        return

    # Calculate range
    data_range = calculate_range(data)

    print("Range:", data_range)


def calculate_standard_deviation(data, reference_number=None):
    if reference_number is not None:
        deviation_from_reference = [(x - reference_number) ** 2 for x in data]
        return (sum(deviation_from_reference) / len(data)) ** 0.5
    else:
        return stdev(data)

def solve_MMM():
    data = []

    while True:
        value = input("Enter a value (or 'done' to finish): ")
        if value.lower() == "done":
            break
        try:
            data.append(float(value))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if data:
        data_mean = mean(data)
        data_median = median(data)
        data_mode = mode(data)
        
        print("Mean:", data_mean)
        print("Median:", data_median)
        print("Mode:", data_mode)
        
        reference_choice = input("Do you want to enter a reference value for standard deviation? (yes/no): ")
        if reference_choice.lower() == "yes":
            reference_number = float(input("Enter the reference number: "))
            data_stddev = calculate_standard_deviation(data, reference_number)
            print("Standard Deviation (Relative to", reference_number, "):", data_stddev)
        else:
            data_stddev = calculate_standard_deviation(data)
            print("Standard Deviation:", data_stddev)

def solve_trigonometric_equation():
    equation = input("Enter a trigonometric equation (e.g., sin(x) + cos(x) = 1): ")

    try:
        result = eval(equation, {"__builtins__": None}, math.__dict__)
        print("Solution:", result)
    except (SyntaxError, NameError, TypeError):
        print("Invalid equation.")

def convert_units():
    print("Unit Conversion Calculator")
    print("Available conversion options:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Pounds to Kilograms")
    print("4. Kilograms to Pounds")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")

    option = input("Enter the conversion option (1-6): ")

    if option == "1":
        kilometers = float(input("Enter the distance in kilometers: "))
        miles = kilometers * 0.621371
        print("Miles:", miles)
    elif option == "2":
        miles = float(input("Enter the distance in miles: "))
        kilometers = miles * 1.60934
        print("Kilometers:", kilometers)
    elif option == "3":
        pounds = float(input("Enter the weight in pounds: "))
        kilograms = pounds * 0.453592
        print("Kilograms:", kilograms)
    elif option == "4":
        kilograms = float(input("Enter the weight in kilograms: "))
        pounds = kilograms * 2.20462
        print("Pounds:", pounds)
    elif option == "5":
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Fahrenheit:", fahrenheit)
    elif option == "6":
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print("Celsius:", celsius)
    else:
        print("Invalid option. Please select a number from 1 to 6.")



def calculator():
    while True:
        command = input("Which calculator do you need? Trig (trig), Mean Median Mode (mmm),  unit converter(converter), standard deviation(stand dev),  calculate range(range), equation solver(equation),  (Enter 'exit' to quit): ")
        if command.lower() == "trig":
            solve_trigonometric_equation()
        if command.lower() == "converter":
            convert_units()
        if command.lower() == "mmm":
            solve_MMM()
        if command == "stand dev":
            calculate_standard_deviation()
        if command == "range":
            calculate_data_range()
        if command == "equation":
            solve_equation()
            
            
            
        elif command.lower() == "exit":
            break
        else:
            print("Invalid command. Please enter 'Trig', 'MMM', or 'exit'.")


