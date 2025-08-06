

def add_student(students: dict, person: str):
    if person not in students:
        students[person] = []


def add_course(students: dict, person: str, course: tuple):
    name, grade = course
    if grade != 0 and name not in [c[0] for c in students[person]]:
        students[person].append(course)

def print_student(students: dict, person: str):
    if person not in students:
        print(f"{person}: No such person in the database")
    elif person in students and students[person] == []: # and no course
        print(f'{person}: \n No completed courses')
    else:
        completed_courses = len(students[person])
        sum = 0
        print(f'{person}: \n {completed_courses} completed courses: ')
        for key, value in students[person]:
            print(f'  {key} {value}')
            sum += value
        average = sum / completed_courses
        print(f'average grade {average}')

def summary(students: dict):
    count = len(students)
    print(f'students {count}')
    most_courses = 0
    for name, info in students.items():
        courses = len(info)
        if courses > most_courses:
            most_courses = courses
            most_courses_student = name
    print(f'most courses completed {most_courses} {most_courses_student}')
    best_grades = 0
    total_grade = 0
    names = []
    for name, info in students.items():
        for key, value in info:
            if name not in names:
                names.append(name)
                total_grade = 0
            total_grade += value
        avg_best = total_grade / len(info)
        if avg_best > best_grades:
            best_grades = avg_best
            best_grades_student = name
    print(f'best average grade {avg_best} {best_grades_student}')
        

students = {}
add_student(students, 'Peter')
add_student(students, 'Eliza')
add_course(students, 'Peter', ('Data Structures and Algorithms', 1))
add_course(students, 'Peter', ('Introduction to Programming', 1))
add_course(students, 'Peter', ('Advanced Course in Programming', 1))
add_course(students, 'Eliza', ('Introduction to Programming', 5))
add_course(students, 'Eliza', ('Introduction to Computer Science', 4))
summary(students)

