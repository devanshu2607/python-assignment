##77.	Design a quiz application that evaluates user knowledge using functions and data structures.

# Quiz questions and answers
questions = [
    ("What is the capital of France?", "A"),
    ("Which planet is known as the RedPlanet?", "B"),
    ("Who wrote 'Hamlet'?", "B")
]

options = [
    "A) Paris  B) London  C) Rome  D) Berlin",
    "A) Earth  B) Mars  C) Venus  D) Jupiter",
    "A) Charles Dickens  B) William Shakespeare  C) Mark Twain  D) J.K. Rowling"
]

score = 0

# Ask each question
for i, (question, correct_answer) in enumerate(questions):
    print(f"\nQ{i+1}: {question}")
    print(options[i])
    answer = input("Your answer (A, B, C, or D): ").strip().upper()
    if answer == correct_answer:
        score += 1

# Show final score
print(f"\nYou scored {score}/{len(questions)}!")