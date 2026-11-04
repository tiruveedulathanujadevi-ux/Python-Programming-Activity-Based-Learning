
# String-Based Examination Answer Evaluation

print("===== EXAMINATION ANSWER EVALUATION =====")

# Store questions and correct answers
questions = {
    "1. What is the capital of India?": "Delhi",
    "2. Which language is used for AI?": "Python",
    "3. What is the full form of CPU?": "Central Processing Unit",
    "4. Which symbol is used for comments in Python?": "#",
    "5. What is the extension of Python files?": ".py"
}

score = 0
total = len(questions)

# Evaluate student answers
for question, correct_answer in questions.items():

    print("\n" + question)
    answer = input("Enter your answer: ")

    if answer.strip().lower() == correct_answer.lower():
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print("Correct Answer:", correct_answer)

# Calculate result
percentage = (score / total) * 100

print("\n===== EXAMINATION RESULT =====")
print("Total Questions:", total)
print("Correct Answers:", score)
print("Wrong Answers:", total - score)
print("Total Marks:", score, "/", total)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")

print("==============================")
print("Examination Evaluation Completed!")
