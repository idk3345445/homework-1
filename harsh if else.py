
def guess_number_basic(numbers):

     # Let's just pick the first number for simplicity  
    
     hosen_number = numbers[0]
     print("picked henumber", chosen_number, ". Try to guess it!")

while True: 
    try:
        guess = int(input("What's your guess? "))
        if guess == chosen_number:
            print("Yes! You guessed right!")
            break
        elif guess > chosen_number:
            print("Too big!")
        else:
            print("Too small!")
    except ValueError:
        print("Please type in a number.")

# Example list of numbers

my_numbers = [5, 10, 2, 8]

guess_number_basic(my_numbers)