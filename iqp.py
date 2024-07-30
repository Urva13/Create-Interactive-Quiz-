import random

# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Rome"],
        "correct": 0
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Earth", "Saturn", "Jupiter", "Uranus"],
        "correct": 2
    },
    {
        "question": "What is the smallest country in the world?",
        "answers": ["Vatican City", "Monaco", "Nauru", "Tuvalu"],
        "correct": 0
    },
    # Add more questions here
]

# Function to shuffle the questions
def shuffle_questions(questions):
    random.shuffle(questions)
    return questions

# Function to ask a question
def ask_question(question):
    print(question["question"])
    for i, answer in enumerate(question["answers"]):
        print(f"{i+1}. {answer}")
    response = input("Enter the number of your answer: ")
    try:
        response = int(response) - 1
        if response == question["correct"]:
            return True
        else:
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

# Function to calculate the score
def calculate_score(score, total):
    percentage = (score / total) * 100
    print(f"Your score is {score} out of {total} ({percentage:.2f}%)")

# Main quiz function
def quiz():
    questions = shuffle_questions(questions)
    score = 0
    for question in questions:
        if ask_question(question):
            score += 1
    calculate_score(score, len(questions))

# Run the quiz
quiz()