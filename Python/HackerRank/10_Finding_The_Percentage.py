n = int(input())
students = {}

for _ in range(n):
    data = input().split()
    students[data[0]] = list(map(float, data[1:]))

name = input()
average = sum(students[name]) / len(students[name])

print(f"{average:.2f}")
