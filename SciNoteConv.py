# Scientific notation to standard form converter

def scientific_to_standard(scientific_notation):
    # Remove whitespace and convert to lowercase
    scientific_notation = scientific_notation.strip().lower()
    
    while scientific_notation:
        if 'e' in scientific_notation:
            # Split the string at the 'e' character
            mantissa, exponent = scientific_notation.split('e', 1)
            mantissa = float(mantissa)
            exponent = int(exponent)
            
            # Calculate the result in standard form
            result = mantissa * (10 ** exponent)
            
            return result
        else:
            print("Invalid scientific notation format.")
            scientific_notation = input("Enter a valid scientific notation (or press 'q' to quit): ")
            
            if scientific_notation.lower() == 'q':
                break
    
    print("Exiting the program.")


