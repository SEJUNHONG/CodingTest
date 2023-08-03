N = int(input())

students = []
for i in range(N):
    student = input().split()
    students.append((student[0], int(student[1])))

students = sorted(students, key = lambda x:x[1])

for student in students:
    print(student[0], end=' ')