
# Attendance Recovery Computation

print("===== ATTENDANCE RECOVERY SYSTEM =====")

# Get student details
name = input("Enter Student Name: ")
total_classes = int(input("Enter Total Number of Classes: "))
attended_classes = int(input("Enter Attended Classes: "))

# Validate input
if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
    print("Invalid attendance details!")

else:
    # Calculate attendance percentage
    attendance = (attended_classes / total_classes) * 100

    print("\nStudent Name:", name)
    print("Total Classes:", total_classes)
    print("Attended Classes:", attended_classes)
    print("Attendance Percentage:", round(attendance, 2), "%")

    # Check attendance eligibility
    required_percentage = 75

    if attendance >= required_percentage:
        print("Status: Eligible for Examination")
        print("No recovery classes required.")

    else:
        # Calculate minimum classes needed to reach 75%
        recovery_classes = 0

        while ((attended_classes + recovery_classes) /
               (total_classes + recovery_classes)) * 100 < required_percentage:
            recovery_classes += 1

        print("Status: Attendance Shortage")
        print("Required Attendance:", required_percentage, "%")
        print("Recovery Classes Needed:", recovery_classes)

print("======================================")
