
# Student Performance Trend Analysis

print("===== STUDENT PERFORMANCE ANALYSIS =====")

# Get student details
name = input("Enter Student Name: ")

# Get marks for three exams
exam1 = float(input("Enter Exam 1 Marks: "))
exam2 = float(input("Enter Exam 2 Marks: "))
exam3 = float(input("Enter Exam 3 Marks: "))

# Calculate average
average = (exam1 + exam2 + exam3) / 3

# Analyze performance trend
print("\n===== PERFORMANCE REPORT =====")
print("Student Name:", name)
print("Exam 1 Marks:", exam1)
print("Exam 2 Marks:", exam2)
print("Exam 3 Marks:", exam3)
print("Average Marks:", round(average, 2))

if exam1 < exam2 < exam3:
    print("Performance Trend: Improving")

elif exam1 > exam2 > exam3:
    print("Performance Trend: Declining")

else:
    print("Performance Trend: Fluctuating")

# Calculate grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

print("Final Grade:", grade)

print("===============================")
