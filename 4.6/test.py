

exam_points = [15,10,11,4]
exercises = [87,55,40,17]

final_exercise_points = []
average_exam_points = round(sum(exam_points) / len(exam_points), 1)
for i in exercises:
    exercise_point = round(i / 10)
    final_exercise_points.append(exercise_point)
print(exam_points)
print(final_exercise_points)
final_grades = []
for i in range(len(exam_points)):
    value = exam_points[i] + final_exercise_points[i]
    final_grades.append(value)

print(final_grades)