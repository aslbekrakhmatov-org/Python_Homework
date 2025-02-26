import csv
content = []
with open("grades.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        content.append(row)

subject_grades = {}
student_nums = {}
for item in content:
    subject = item["Subject"]
    grade = int(item["Grade"])
    if subject not in subject_grades:
        subject_grades[subject] = 0
        student_nums[subject] = 0
    subject_grades[subject]+=grade
    student_nums[subject]+=1

content_avg = []
for subject, total_grade in subject_grades.items():
    avg_grade = total_grade/student_nums[subject]
    content_avg.append({"Subject":subject, "Average Grade":round(avg_grade,2)})

with open("average_grades.csv", 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Subject", "Average Grade"])
    writer.writeheader()
    writer.writerows(content_avg)
