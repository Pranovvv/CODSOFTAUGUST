print("")
print("     ***WELCOME TO THE QUIZ GAME***\n")
print("You will be asked a series of multiple-choice questions.")
print("For each question, enter the letter corresponding to your answer (A, B, C, or D).\n")

play_again = "yes"

while play_again.lower() == "yes":
    questions = ("Where did the G20 Summit 2023 organized?",
                 "Where is the Statue Of Liberty located?",
                 "Which country won the FIFA World Cup 2022?",
                 "Which is the largest populated country?",
                 "Which country is the largest?")

    options = (("A. India", "B. China", "C. USA", "D. Russia"),
               ("A. New York", "B. Mumbai", "C. Berlin", "D. Tokyo"),
               ("A. Croatia", "B. Argentina", "C. Brazil", "D. France"),
               ("A. Russia", "B. India", "C. China", "D. Italy"),
               ("A. Germany","B. USA","C. China","D. Russia"))

    answers = ("A","A","B","C","D")
    guesses = []
    score = 0 
    question_num = 0

    for question in questions:
        print("-------------------------------------")
        print(question)
        for option in options[question_num]:
            print(option)
        guess = input("Enter (A,B,C,D):").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"The correct answer is {answers[question_num]}")
        question_num += 1

    print("--------------------------------")
    print("            RESULTS             ")
    print("--------------------------------")

    print("Answers:", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("Guesses:", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score/len(questions)*100)
    print(f"Your score is: {score}%")

    play_again = input("Do you want to play again? (yes/no): ")

print("♥ Thank you for playing ♥")