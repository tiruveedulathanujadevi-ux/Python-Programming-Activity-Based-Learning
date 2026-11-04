
# Student Marks Matrix Analysis

print("===== STUDENT MARKS MATRIX ANALYSIS =====")

# Store student marks in a matrix
students = [
    [85, 90, 78],
    [75, 80, 88],
    [92, 95, 89],
    [60, 70, 65],
    [80, 85, 90]
]

subjects = ["Python", "Java", "DBMS"]

total_students = len(students)
total_subjects = len(subjects)

# Display marks matrix
print("\nStudent Marks Matrix:")

for i in range(total_students):
    print("Student", i + 1, ":", students[i])

# Calculate student totals and averages
print("\n===== STUDENT PERFORMANCE =====")

for i in range(total_students):
    total = sum(students[i])
    average = total / total_subjects

    print("\nStudent", i + 1)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))

    if average >= 90:
        print("Grade: A+")
    elif average >= 80:
        print("Grade: A")
    elif average >= 70:
        print("Grade: B")
    elif average >= 60:
        print("Grade: C")
    else:
        print("Grade: Fail")

# Calculate subject-wise averages
print("\n===== SUBJECT-WISE ANALYSIS =====")

for j in range(total_subjects):
    subject_total = 0

    for i in range(total_students):
        subject_total += students[i][j]

    subject_average = subject_total / total_students

    print(subjects[j], "Average:",
          round(subject_average, 2))

print("\n===== ANALYSIS COMPLETED =====")
