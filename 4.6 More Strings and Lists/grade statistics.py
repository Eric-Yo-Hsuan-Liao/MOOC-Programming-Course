
# Asking user for exam points and exercises completed
def course_results():
    points = []
    exercises = []
    result = input('Exam points and exercises completed: ')
    if result:
        exam_points, exercise_points = result.split()
        exam_points = int(exam_points)
        exercise_points = int(exercise_points)
        points.append(exam_points)
        exercises.append(exercise_points)
    while result != '':
        result = input('Exam points and exercises completed: ')
        if result:
            exam_points, exercise_points = result.split()
            exam_points = int(exam_points)
            exercise_points = int(exercise_points)
            points.append(exam_points)
            exercises.append(exercise_points)
    return points, exercises


# Calculating statistics for course grades
def statistics(points: list, exercises: list):
    print('Statistics:')
    final_exercise_points = []
    for i in exercises:
        exercise_point = round(i / 10)
        final_exercise_points.append(exercise_point)
    final_grades = []
    course_pass = 0
    for i in range(len(points)):
        value = points[i] + final_exercise_points[i]
        final_grades.append(value)
        if points[i] >= 10 and value > 14:
            course_pass += 1
    average_exam_points = round(sum(final_grades) / len(final_grades), 1)
    print(f'Points average: {average_exam_points}')
    pass_pct = course_pass / len(final_grades)
    print(f'Pass percentage: {pass_pct}')
    return final_grades, points


# Calculating grades
def grades(final_grades: list, points: list):
    count_5 = 0
    count_4 = 0
    count_3 = 0
    count_2 = 0
    count_1 = 0
    count_0 = 0
    for i in points:
        if i < 10:
            count_0 += 1
    for grade in final_grades:
        if grade <= 14:
            count_0 += 1
        elif (grade >= 15) & (grade <= 17):
            count_1 += 1
        elif (grade >= 18) & (grade <= 20):
            count_2 += 1
        elif (grade >= 21) & (grade <= 23):
            count_3 += 1
        elif (grade >= 24 & grade <= 27):
            count_4 += 1
        elif (grade >= 28 & grade <= 30):
            count_5 += 1 
    print('Grade distribution')
    print('5: ', count_5 * '*')
    print('4: ', count_4 * '*')
    print('3: ', count_3 * '*')
    print('2: ', count_2 * '*')
    print('1: ', count_1 * '*')
    print('0: ', count_0 * '*')

#exam_points = [15,10,11,4]
#exercises = [87,55,40,17]

# Main function to run everything
def main():
    points, exercises = course_results()
    stats, exam_scores = statistics(points, exercises)
    student_grades = grades(stats, exam_scores) 
main()