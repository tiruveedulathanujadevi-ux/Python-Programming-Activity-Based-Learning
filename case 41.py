
# Nested List Classroom Occupancy Analysis

print("===== CLASSROOM OCCUPANCY ANALYSIS =====")

# Store classroom details using nested lists
classrooms = [
    ["Classroom A", 40, 35],
    ["Classroom B", 50, 45],
    ["Classroom C", 30, 25],
    ["Classroom D", 60, 55]
]

total_capacity = 0
total_students = 0

# Display classroom details
print("\nClassroom Occupancy Details")

for room in classrooms:
    name = room[0]
    capacity = room[1]
    occupied = room[2]

    vacant = capacity - occupied
    percentage = (occupied / capacity) * 100

    total_capacity += capacity
    total_students += occupied

    print("\nClassroom:", name)
    print("Total Capacity:", capacity)
    print("Occupied Seats:", occupied)
    print("Vacant Seats:", vacant)
    print("Occupancy Percentage:", round(percentage, 2), "%")

# Calculate overall occupancy
overall_percentage = (total_students / total_capacity) * 100

print("\n===== OVERALL ANALYSIS =====")
print("Total Classrooms:", len(classrooms))
print("Total Capacity:", total_capacity)
print("Total Students:", total_students)
print("Total Vacant Seats:", total_capacity - total_students)
print("Overall Occupancy:", round(overall_percentage, 2), "%")

print("\n===== ANALYSIS COMPLETED =====")
