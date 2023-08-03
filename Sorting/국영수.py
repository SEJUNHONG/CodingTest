N = int(input())
students = []
for i in range(N):
    student = input().split()
    students.append((student[0], int(student[1]), student[2], student[3]))

students = sorted(students, key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])