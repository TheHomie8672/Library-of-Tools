def Num_Extrapolator_Algorith():
    sequence = []
    
    while True:
        num_input = input("Enter a number in the sequence (or 'done' to exit): ")
        
        if num_input.lower() == "done":
            break
        
        try:
            number = float(num_input)
            sequence.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to exit.")
    
    if len(sequence) >= 2:
        patterns = [
            lambda seq: all(seq[i] == seq[i-1] + seq[i-2] for i in range(2, len(seq))),  # Fibonacci-like pattern
            lambda seq: all(seq[i] == seq[0] + (i * (seq[1] - seq[0])) for i in range(1, len(seq))),  # Arithmetic progression
            lambda seq: all(seq[i] % seq[1] == 0 for i in range(1, len(seq))),  # Multiple of the second element
            # Add more pattern identification methods as needed
        ]
        
        pattern_found = False
        next_number = None
        
        for pattern in patterns:
            if pattern(sequence):
                pattern_found = True
                
                # Apply pattern-specific extrapolation logic
                if pattern.__code__.co_argcount == 1:  # Check the number of arguments the pattern function takes
                    next_number = pattern_extrapolate(pattern, sequence)
                else:
                    next_number = pattern_extrapolate(pattern, sequence, sequence[-1])
                
                break
        
        if pattern_found:
            print("The next number in the sequence is:", next_number)
        else:
            print("Pattern not found in the sequence.")
    else:
        print("Please enter more numbers to identify a pattern.")

    print("Exiting the program.")

def pattern_extrapolate(pattern, sequence, *args):
    if pattern.__code__.co_argcount == 1:  # Fibonacci-like pattern
        return sequence[-1] + sequence[-2]
    elif pattern.__code__.co_argcount == 2:  # Arithmetic progression or Multiple of the second element
        return sequence[-1] + (sequence[1] - sequence[0])
    # Add more pattern-specific extrapolation logic as needed

# Example usage






