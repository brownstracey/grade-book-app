from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, student):
        self.student_list.append(student)

    def add_course(self, course):
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name):
        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course({'name': course.name, 'credits': course.credits, 'grade_point': course.grade_point})

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        for rank, student in enumerate(self.student_list, start=1):
            print(f"{rank}. {student.names} - GPA: {student.GPA}")

    def search_by_grade(self, grade_point):
        students_with_grade = [student for student in self.student_list if any(course['grade_point'] == grade_point for course in student.courses_registered)]
        for student in students_with_grade:
            print(f"{student.names} - Email: {student.email}")

    def generate_transcript(self, student_email):
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print(f"Transcript for {student.names}")
            for course in student.courses_registered:
                print(f"{course['name']}: Grade Point {course['grade_point']}")
            print(f"GPA: {student.GPA}")
