import unittest

from academy_project import (
    Student,
    students,
    courses,
    valid_courses,
    add_student,
    find_student,
    remove_student,
    count_passed_students,
    get_top_student,
    get_adult_students,
    calculate_statistics
)


class TestStudentProject(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\n" + "=" * 50)
        print("         UNIT TEST EXECUTION")
        print("=" * 50 + "\n")

    def setUp(self):
        print("\n========== NEW TEST ==========")
        students.clear()

    # ===== Student Class =====

    def test_student_creation(self):
        print("Testing student creation...")

        student = Student(1, "Alice", 20)

        print(f"Created: {student.name}")

        self.assertEqual(student.student_id, 1)
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.age, 30)  # This will fail, as the age is set to 20
        self.assertEqual(student.grades, [])

    def test_add_valid_grade(self):
        print("Testing valid grade...")

        student = Student(1, "Alice", 20)

        result = student.add_grade(8)

        print(f"Grade added: {result}")
        print(f"Grades: {student.grades}")

        self.assertTrue(result)
        self.assertEqual(student.grades, [8])

    def test_add_invalid_grade(self):
        print("Testing invalid grade...")

        student = Student(1, "Alice", 20)

        result = student.add_grade(15)

        print(f"Grade added: {result}")

        self.assertFalse(result)
        self.assertEqual(student.grades, [])

    def test_average_grade(self):
        print("Testing average grade...")

        student = Student(1, "Alice", 20)

        student.add_grade(8)
        student.add_grade(10)

        average = student.average_grade()

        print(f"Average: {average}")

        self.assertEqual(average, 9)

    def test_average_grade_empty(self):
        print("Testing average with no grades...")

        student = Student(1, "Alice", 20)

        result = student.average_grade()

        print(f"Average: {result}")

        self.assertEqual(result, 0)

    def test_is_passing_true(self):
        print("Testing passing student...")

        student = Student(1, "Alice", 20)

        student.add_grade(8)

        result = student.is_passing()

        print(f"Passing: {result}")

        self.assertTrue(result)

    def test_is_passing_false(self):
        print("Testing failing student...")

        student = Student(1, "Alice", 20)

        student.add_grade(4)

        result = student.is_passing()

        print(f"Passing: {result}")

        self.assertFalse(result)

    # ===== Functions =====

    def test_add_student(self):
        print("Testing add student...")

        student = Student(1, "Alice", 20)

        add_student(student)

        print(f"Students count: {len(students)}")

        self.assertEqual(len(students), 1)

    def test_find_student_exists(self):
        print("Testing find existing student...")

        student = Student(1, "Alice", 20)

        add_student(student)

        result = find_student(1)

        print(f"Found: {result.name}")

        self.assertEqual(result, student)

    def test_find_student_not_exists(self):
        print("Testing find non-existing student...")

        result = find_student(999)

        print(f"Result: {result}")

        self.assertIsNone(result)

    def test_remove_student_exists(self):
        print("Testing remove existing student...")

        student = Student(1, "Alice", 20)

        add_student(student)

        result = remove_student(1)

        print(f"Removed: {result}")

        self.assertTrue(result)
        self.assertEqual(len(students), 0)

    def test_remove_student_not_exists(self):
        print("Testing remove non-existing student...")

        result = remove_student(999)

        print(f"Removed: {result}")

        self.assertFalse(result)

    def test_count_passed_students(self):
        print("Testing count passed students...")

        s1 = Student(1, "Alice", 20)
        s2 = Student(2, "Bob", 17)

        s1.add_grade(8)
        s2.add_grade(4)

        add_student(s1)
        add_student(s2)

        result = count_passed_students()

        print(f"Passed students: {result}")

        self.assertEqual(result, 1)

    def test_get_top_student(self):
        print("Testing top student...")

        s1 = Student(1, "Alice", 20)
        s2 = Student(2, "Bob", 17)

        s1.add_grade(10)
        s2.add_grade(5)

        add_student(s1)
        add_student(s2)

        top = get_top_student()

        print(f"Top student: {top.name}")

        self.assertEqual(top.name, "Alice")

    def test_get_top_student_empty(self):
        print("Testing top student on empty list...")

        top = get_top_student()

        print(f"Result: {top}")

        self.assertIsNone(top)

    def test_get_adult_students(self):
        print("Testing adult students...")

        s1 = Student(1, "Alice", 20)
        s2 = Student(2, "Bob", 17)

        add_student(s1)
        add_student(s2)

        adults = get_adult_students()

        print(f"Adults count: {len(adults)}")

        self.assertEqual(len(adults), 1)
        self.assertEqual(adults[0].name, "Alice")

    def test_calculate_statistics(self):
        print("Testing statistics...")

        s1 = Student(1, "Alice", 20)
        s2 = Student(2, "Bob", 18)

        add_student(s1)
        add_student(s2)

        stats = calculate_statistics()

        print(f"Statistics: {stats}")

        self.assertEqual(stats["total_students"], 2)
        self.assertEqual(stats["average_age"], 19)

    def test_calculate_statistics_empty(self):
        print("Testing statistics on empty list...")

        stats = calculate_statistics()

        print(f"Statistics: {stats}")

        self.assertEqual(stats["total_students"], 0)
        self.assertEqual(stats["average_age"], 0)

    # ===== Dictionary Tests =====

    def test_course_exists(self):
        print("Testing dictionary key...")

        self.assertIn("Python", courses)

    def test_course_teacher(self):
        print("Testing dictionary value...")

        self.assertEqual(courses["Python"], "Adrian")

    # ===== Tuple Tests =====

    def test_valid_courses_length(self):
        print("Testing tuple length...")

        self.assertEqual(len(valid_courses), 3)

    def test_course_in_tuple(self):
        print("Testing tuple contains Docker...")

        self.assertIn("Docker", valid_courses)

    # ===== Class Variable =====

    def test_school_name(self):
        print("Testing class variable school_name...")

        self.assertEqual(Student.school_name, "Python Academy")


if __name__ == "__main__":
    unittest.main(verbosity=2)