
n = int(input("Enter number of students: "))

eligible = []

for i in range(n):
    print("\nEnter Student", i + 1, "Details")

    name = input("Enter name: ")
    aggregate = float(input("Enter aggregate marks: "))

    print("Enter marks in 3 subjects:")
    s1 = float(input("Subject 1: "))
    s2 = float(input("Subject 2: "))
    s3 = float(input("Subject 3: "))

    attendance = float(input("Enter attendance: "))
    income = float(input("Enter annual family income: "))

    if (aggregate >= 75 and s1 >= 50 and
        s2 >= 50 and s3 >= 50 and
        attendance >= 75 and income <= 250000):

        eligible.append((name, aggregate, attendance))
        print("Student is Eligible")

    else:
        print("Student is Not Eligible")

# Ranking students
eligible.sort(key=lambda x: (-x[1], -x[2], x[0]))

print("\n--- SCHOLARSHIP MERIT LIST ---")

if len(eligible) == 0:
    print("No students are eligible.")
else:
    rank = 1

    for student in eligible:
        print("Rank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Attendance:", student[2])
        print("Scholarship: Approved")
        print("----------------------")
        rank += 1


