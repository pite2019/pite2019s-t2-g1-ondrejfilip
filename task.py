import json
import copy


def get_student_average(student, classrooms):
    count = 0
    i = 1
    for room in classrooms:
        count += room.get_student_average(student)
        i += 1
    return count/i


class Student:

    def __init__(self, student_id, first_name, last_name):
        self.id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.score = []
        self.attendance = 0

    def filter_score(self):
        return list(filter(lambda x: x >= 50, self.score))

    def __repr__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class ClassRoom:

    def __init__(self, classroom_name):
        self.classroom_name = classroom_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def add_score(self, student_id, score):
        for item in self.students:
            if item.id == student_id:
                item.score.append(score)

    def add_attendance(self, student_id):
        for item in self.students:
            if item.id == student_id:
                item.attendance += 1

    def get_student_average(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return sum(student.score) / len(student.score)
        return 0

    def __repr__(self):
        return '{} {}'.format(self.classroom_name, self.students)


def main():
    classrooms_list = []

    classroom1 = ClassRoom('Python')
    classroom2 = ClassRoom('Math')

    classrooms_list.append(classroom1)
    classrooms_list.append(classroom2)

    student1 = Student('s1', 'John', 'Doe')
    student2 = Student('s2', 'Franta', 'Lala')
    student3 = Student('s3', 'Alan', 'Turing')

    classroom1.add_student(student1)
    classroom1.add_student(student2)
    classroom2.add_student(student3)
    classroom2.add_student(copy.deepcopy(student1))

    classroom1.add_score(student1.id, 40)
    classroom1.add_score(student1.id, 60)
    classroom1.add_score(student1.id, 70)
    classroom2.add_score(student1.id, 40)
    classroom2.add_score(student1.id, 50)

    classroom1.add_attendance(student1.id)
    classroom1.add_attendance(student1.id)
    classroom2.add_attendance(student1.id)

    print('ClassRoom1 Student1 average: {}'.format(classroom1.get_student_average(student1.id)))
    print('Student1 All ClassRooms average: {}'.format(get_student_average(student1.id, classrooms_list)))
    print('Student1 filter score above average: {}'.format(student1.filter_score()))

    data = {}
    data['Students'] = []

    for classroom in classrooms_list:

        for item in classroom.students:
            data['Students'].append({
                'Classroom Name': classroom.classroom_name,
                'First Name': item.first_name,
                'Last Name': item.last_name,
                'Score': item.score,
                'Attendance': item.attendance
            })

    file = open('report.json', 'w', encoding='utf-8')
    json.dump(data, file, indent=2, ensure_ascii=False)
    print('Data save to file.')
    file.close()


if __name__ == '__main__':
    main()
