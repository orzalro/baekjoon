import sys
input = sys.stdin.readline

grade_dict = {'A+':'4.5', 'A0':'4.0', 'B+':'3.5', 'B0':'3.0', 'C+':'2.5', 'C0':'2.0', 'D+':'1.5', 'D0':'1.0', 'F':'0.0'}

grades = []
total_credit = 0

for _ in range(20):
    credit, grade = input().split()[1:]
    if grade != 'P':
        credit = float(credit)
        grades.append(credit * float(grade_dict[grade]))
        total_credit += credit

print(sum(grades) / total_credit)