# Step 1: Define the questions and answers
questions = {
    "What is the capital of France?": "paris",
    "What is the capital of Germany?": "berlin",
    "What is the capital of Italy?": "rome",
    "What is the capital of Spain?": "madrid",
    "What is the capital of Portugal?": "lisbon",
    "What is the capital of Netherlands?": "amsterdam",
    "What is the capital of Belgium?": "brussels",
    "What is the capital of Sweden?": "stockholm",
    "What is the capital of Norway?": "oslo",
    "What is the capital of Finland?": "helsinki"
}

# Step 2: Create the quiz
for question, correct_answer in questions.items():
    user_answer = input(question + " ").strip()  # Step 3: Handle capitalization
    if user_answer == correct_answer:#using if,else statement
        print("Correct! 🎉")
    else:
        print("Wrong! 😢 please try again")

