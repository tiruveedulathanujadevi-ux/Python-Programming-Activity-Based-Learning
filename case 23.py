
# Student Timetable Conflict Detection

print("===== STUDENT TIMETABLE SYSTEM =====")

# Store timetable details
timetable = []

n = int(input("Enter number of classes: "))

for i in range(n):
    print("\nEnter details for Class", i + 1)

    subject = input("Enter Subject Name: ")
    start = int(input("Enter Start Time (24-hour format): "))
    end = int(input("Enter End Time (24-hour format): "))

    if start < 0 or end > 24 or start >= end:
        print("Invalid time! Please enter valid timings.")
        continue

    timetable.append([subject, start, end])

# Check timetable conflicts
print("\n===== TIMETABLE CONFLICT REPORT =====")

conflict_found = False

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):

        subject1, start1, end1 = timetable[i]
        subject2, start2, end2 = timetable[j]

        if start1 < end2 and start2 < end1:
            print("Conflict Detected!")
            print(subject1, "and", subject2, "have overlapping timings.")
            conflict_found = True

if not conflict_found:
    print("No timetable conflicts found.")

# Display timetable
print("\n===== STUDENT TIMETABLE =====")

for subject, start, end in timetable:
    print(subject, ":", start, "to", end)

print("\n===== ANALYSIS COMPLETED =====")
