if __name__ == "__main__":

    print("\n" + "=" * 50)
    print("        PROJECT ACADEMY DEMO")
    print("=" * 50 + "\n")

    class Student:
        school_name = "Python Academy"

        def __init__(self, student_id, name, age):
            self.student_id = student_id
            self.name = name
            self.age = age
            self.grades = []

        def add_grade(self, grade):
            if 0 <= grade <= 10:
                self.grades.append(grade)
                return True
            return False

        def average_grade(self):
            if not self.grades:
                return 0
            return sum(self.grades) / len(self.grades)

        def is_passing(self):
            return self.average_grade() >= 5


    # listă goala de studenți
    students = []

    # dicționar cu cursuri și instructori
    courses = {
        "Python": "Adrian",
        "Github": "Alin",
        "Docker": "Radu"
    }

    # tuple cu cursuri valide
    valid_courses = ("Python", "Github", "Docker")

    # funcții pentru gestionarea studenților
    def add_student(student):
        students.append(student)


    def find_student(student_id):
        for student in students:
            if student.student_id == student_id:
                return student
        return None


    def remove_student(student_id):
        student = find_student(student_id)

        if student:
            students.remove(student)
            return True

        return False


    def count_passed_students():
        count = 0

        for student in students:
            if student.is_passing():
                count += 1

        return count


    def get_top_student():
        if not students:
            return None

        top_student = students[0]

        for student in students:
            if student.average_grade() > top_student.average_grade():
                top_student = student

        return top_student


    def get_adult_students():
        return [student for student in students if student.age >= 18]


    def calculate_statistics():
        if not students:
            return {
                "total_students": 0,
                "average_age": 0
            }

        total_age = sum(student.age for student in students)

        return {
            "total_students": len(students),
            "average_age": total_age / len(students)
        }


    # Exemplu utilizare

    # Cream doi studenti
    print("\n\n ==== PROJECT ACADEMY ====\n\n")

    s1 = Student(1, "Alice", 20)
    s2 = Student(2, "Bob", 17)

    print("Au fost creati 2 studenti.")
    print(f"Student 1: {s1.name}, Age: {s1.age}")
    print(f"Student 2: {s2.name}, Age: {s2.age}")


    print("\nAdaugam note pentru Alice")
    s1.add_grade(8)
    s1.add_grade(10)
    print(f"Grades Alice: {s1.grades}")


    print("\nAdaugam note pentru Bob")
    s2.add_grade(4)
    s2.add_grade(5)
    print(f"Grades Bob: {s2.grades}")


    print("\nAdaugam studentii in lista principala")
    add_student(s1)
    add_student(s2)
    print(f"Total students: {len(students)}")


    print("\nCalculam mediile")
    print(f"Alice average: {s1.average_grade()}")
    print(f"Bob average: {s2.average_grade()}")


    print("\nVerificam daca studentii au promovat")
    print(f"Alice passed: {s1.is_passing()}")
    print(f"Bob passed: {s2.is_passing()}")


    print("\nCautam studentul cu ID 1")
    student = find_student(1)
    if student:
        print(f"Student found: {student.name}")


    print("\nCautam studentul cu ID 999")
    student = find_student(999)
    if student:
        print(f"Student found: {student.name}")
    else:
        print("Student not found")


    print("\nAfisam cursurile")
    for course, teacher in courses.items():
        print(f"{course} -> {teacher}")


    print("\nAfisam tuple-ul de cursuri valide")
    for course in valid_courses:
        print(course)


    print("\nCalculam statistici")
    stats = calculate_statistics()
    print(f"Total students: {stats['total_students']}")
    print(f"Average age: {stats['average_age']}")


    print("\nDeterminam cel mai bun student")
    top = get_top_student()
    print(f"Top student: {top.name}")


    print("\nStergem studentul Bob")
    remove_student(2)
    print(f"Students left: {len(students)}")
