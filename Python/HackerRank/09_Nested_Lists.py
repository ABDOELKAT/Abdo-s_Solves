students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set(student[1] for student in students))
second_lowest = scores[1]

for student in sorted(students):
    if student[1] == second_lowest:
        print(student[0])
