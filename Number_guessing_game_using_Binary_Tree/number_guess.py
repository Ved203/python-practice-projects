def guessNumber(start_number, last_number):
    if start_number > last_number:
        print("Number could not be guessed.")
        return
    
    mid = (start_number + last_number) // 2
    
    print(f"Is the number {mid}? (Y/N): ", end="")
    user = input().strip()
    
    if user in ("Y", "y"):
        print(" Congratulations! You successfully guessed the number.")
        return
        
    elif user in ("N", "n"):
        print(f"Is the actual number greater than {mid}? (Y/N): ", end="")
        user = input().strip()

        if user in ("Y", "y"):
            guessNumber(mid + 1, last_number)
        elif user in ("N", "n"):
            guessNumber(start_number, mid - 1)
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            guessNumber(start_number, last_number)
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        guessNumber(start_number, last_number)


if __name__ == "__main__":
    print("... Number Guessing Game in PYTHON ...\n")
    
    start_number = int(input("> Enter the Starting Number of Range: "))
    last_number = int(input("> Enter the Last Number of Range: "))
    
    if start_number > last_number:
        print("Please enter a correct range.")
    else:
        print(f"\nThink about any number between {start_number} and {last_number}.\n")
        guessNumber(start_number, last_number)
