from gradebook import GradeBook
from student import Student
from course import Course

def main():
    gradebook = GradeBook()
    
    while True:
        print("\nGrade Book Application")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            gradebook.add_student(student)
            print("Student added successfully.")
        
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            grade_point = float(input("Enter grade point (e.g., 4.0 for A, 3.0 for B, etc.): "))
            course = Course(name, trimester, credits, grade_point)
            gradebook.add_course(course)
            print("Course added successfully.")
        
        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            gradebook.register_student_for_course(student_email, course_name)
            print("Student registered for course successfully.")
        
        elif choice == '4':
            gradebook.calculate_GPA()
            print("GPA calculated successfully.")
        
        elif choice == '5':
            gradebook.calculate_ranking()
        
        elif choice == '6':
            grade_point = float(input("Enter grade point to search (e.g., 4.0 for A): "))
            gradebook.search_by_grade(grade_point)
        
        elif choice == '7':
            student_email = input("Enter student email: ")
            gradebook.generate_transcript(student_email)
        
        elif choice == '8':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
