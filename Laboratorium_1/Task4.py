def collatz_sequence(start_number):
    """Generate the Collatz sequence starting from start_number."""
    sequence = [start_number]
    while start_number > 1:
        if start_number % 2 == 0: 
            start_number //= 2
        else:  
            start_number = 3 * start_number + 1
        sequence.append(start_number)
    return sequence

if __name__ == "__main__":
    start = int(input("Enter a starting number for the Collatz sequence: "))
    sequence = collatz_sequence(start)
    print("The Collatz sequence starting from {} is:".format(start))
    print(sequence)
