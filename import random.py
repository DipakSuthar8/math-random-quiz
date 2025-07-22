import random

def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])
    question = f"What is {num1} {operation} {num2}?"
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer

def run_quiz():
    score = 0
    total_questions = 3
    print("Welcome to the Number Quiz!")
    print(f"You will be asked {total_questions} math questions. Let's start!\n")

    for i in range(total_questions):
        question, correct_answer = generate_question()
        print(f"Question {i + 1}: {question}")
        
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}.")
        except ValueError:
            print(f"Invalid input! The correct answer is {correct_answer}.")
        print()

    print(f"Quiz Over! Your score: {score}/{total_questions}")
    return score

def main():
    while True:
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()