import csv

def process_grades(input_file, output_file):
    students = []
    subjects = ['Math', 'Science', 'English']

    with open(input_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row['Name']
            grades = {subject: float(row[subject]) for subject in subjects}
            avg = sum(grades.values()) / len(subjects)
            students.append({'Name': name, **grades, 'Average': avg})


    class_averages = {}
    for subject in subjects:
        class_averages[subject] = sum(s[subject] for s in students) / len(students)

    top_student = max(students, key=lambda s: s['Average'])

    fieldnames = ['Name', 'Math', 'Science', 'English', 'Average']
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

    print("Student Report Generated")
    print("------------------------")
    for s in students:
        print(f"{s['Name']} - Average: {s['Average']:.2f}")

    print("\nClass Averages:")
    for subject, avg in class_averages.items():
        print(f"{subject}: {avg:.2f}")

    print(f"Top Performer: {top_student['Name']} ({top_student['Average']:.2f})")
    print(f"Report saved to '{output_file}'")


if __name__ == "__main__":
    process_grades('students.csv', 'student_report.csv')
