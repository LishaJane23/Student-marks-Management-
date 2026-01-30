name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))
total = 0
for i in range(subjects):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    total += marks
percentage = total / subjects
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"
print("\n--- Student Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
