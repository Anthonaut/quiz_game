# --------------------
def new_game():  # Creates a new quiz game
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------------")
        print(key) # print out the question
        for i in options[question_num - 1]: # Access the question choices and print them for each question
            print(i)
        guess = input("Enter (A, B, C, or D): ") # Player types in a guess
        guess = guess.upper() # Still capitalize if the player puts the lowercase of the letters
        guesses.append(guess) # To hold our guesses for display at the end

        correct_guesses += check_answer(questions.get(key), guess) # Check guess with answer key, give 1 point if correct
        question_num += 1
    display_score(correct_guesses, guesses)
# --------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# --------------------
def display_score(correct_guesses, guesses):
    print("---------------------")
    print("RESULTS")
    print("---------------------")

    print("Answers: ", end=" ") # Display all correct answers
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="") # Display guesses made by player
    for i in guesses:
        print(i, end=" ")
    print()

    score = (correct_guesses / len(questions)) * 100 # Score as a percentage
    print("Your score is: " + str(score) + "%")
# --------------------
def play_again(): # If player wants to play again
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == 'YES':
        return True # True, so we stay in the while loop
    else:
        return False # False, so we break out of the while loop
# --------------------

questions = { # A dictionary works to hold a question:answer pair (key:value)
    "Who created Python?": "A",
    "What year was Python created?": "B",
    "Python is attributed to which comedy group": "C",
    "Is the Earth round?": "A"
}

# A 2D list to hold the different answer choices for each question (e.g 1st list for question 1)
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again() == True: # If play_again returns back true, start another quiz game
    new_game()

print("Bye!")