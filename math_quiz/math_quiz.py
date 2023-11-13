import random

def Rand_Int(min, max):
    
    # Returns a random integer.
    
    return random.randint(min, max)


def Rand_Operator():
    # Returns a random operator
    return random.choice(['+', '-', '*'])


def Calculation(number1, number2, operator):
    # Checks the operator and performs the calculations for the given operator
    problem = f"{number1} {operator} {number2}"
    if operator == '+': result= number1 + number2
    elif operator == '-': result = number1 - number2
    else: result = number1 * number2
    return problem, result

def math_quiz():
    score = 0
    total_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = Rand_Int(1, 10);
        number2 = Rand_Int(1, 6);
        operator = Rand_Operator()

        PROBLEM, ANSWER = Calculation(number1, number2, operator) 
        print(f"\nQuestion: {PROBLEM}")

        try:
            # Checks user input and updates the score
            useranswer = int(input("Your answer: "))
            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except ValueError:
            print("please enter an integer")
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
