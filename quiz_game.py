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
# --------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
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

print("Bye!")