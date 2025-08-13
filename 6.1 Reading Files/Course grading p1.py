

# if False:
student_info = input('Student information: ')
exercise_data = input('Exercises completed: ')
exam_points = input('Exam points: ')
# else:
#     student_info = 'students1.csv'
#     exercise_data = 'exercises1.csv'
#     exam_points = 'exam_points1.csv'

info = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        info[parts[0]] = parts[1] + ' ' + parts[2]

exercise = {}
with open(exercise_data) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        id = parts[0]
        exercise[id] = []
        for exer in parts[1:]:
            exercise[id].append(int(exer))

exams = {}
with open(exam_points) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        id = parts[0]
        exams[id] = []
        for exam in parts[1:]:
            exams[id].append(int(exam))


print(f"{'name':30} {'exec_nbr':10} {'exec_pts.':10} {'exm_pts.':10} {'tot_pts.':10} {'grade':10}")
for id, name in info.items():
    if id in exercise and id in exams:
        exercise_sum = sum(exercise[id])
        exercise_points = int((sum(exercise[id]) / 40) * 10)
        exams_total = sum(exams[id])
        total = exercise_points + exams_total
        if total <= 14:
            grade = 0
        elif total >= 15 and total <= 17:
            grade = 1
        elif total >= 18 and total <= 20:
            grade = 2
        elif total >= 21 and total <= 23:
            grade = 3
        elif total >= 24 and total <= 27:
            grade = 4
        elif total >= 28:
            grade = 5
       # print(f'{name} {grade}')
        print(f"{name:30} {exercise_sum:<10} {exercise_points:<10} {exams_total:<10} {total:<10} {grade:<10}")

