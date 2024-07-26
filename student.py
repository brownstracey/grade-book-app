class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        if len(self.courses_registered) == 0:
            self.GPA = 0.0
        else:
            total_points = sum(course['credits'] * course['grade_point'] for course in self.courses_registered)
            total_credits = sum(course['credits'] for course in self.courses_registered)
            self.GPA = total_points / total_credits

    def register_for_course(self, course):
        self.courses_registered.append(course)
