import unittest
from python_project import (
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

    def setUp(self):
        students.clear()

    # ===== Student Class =====

    def test_student_creation(self):
        student = Student(1, "Alice", 20)

        self.assertEqual(student.student_id, 1)
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.grades, [])

    def test_add_valid_grade(self):
        student = Student(1, "Alice", 20)

        result = student.add_grade(8)

        self.assertTrue(result)
        self.assertEqual(student.grades, [8])

    def test_add_invalid_grade(self):
        student = Student(1, "Alice", 20)

        result = student.add_grade(15)

        self.assertFalse(result)
        self.assertEqual(student.grades, [])

    def test_average_grade(self):
        student = Student(1, "Alice", 20)

        student.add_grade(8)
        student.add_grade(10)

        self.assertEqual(student.average_grade(), 9)

    def test_average_grade_empty(self):
        student = Student(1, "Alice", 20)

        self.assertEqual(student.average_grade(), 0)

    def test_is_passing_true(self):
        student = Student(1, "Alice", 20)

        student.add_grade(8)

        self.assertTrue(student.is_passing())

    def test_is_passing_false(self):
        student = Student(1, "Alice", 20)

        student.add_grade(4)

        self.assertFalse(student.is_passing())

    # ===== Functions =====

    def test_add_student(self):
        student = Student(1, "Alice", 20)

        add_student(student)

        self.assertEqual(len(students), 1)

    def test_find_student_exists(self):
        student = Student(1, "Alice", 20)

        add_student(student)

        result = find_student(1)

        self.assertEqual(result, student)

    def test_find_student_not_exists(self):
        result = find_student(999)

        self.assertIsNone(result)

    def test_remove_student_exists(self):
        student = Student(1, "Alice", 20)

        add_student(student)

        result = remove_student(1)

        self.assertTrue(result)
        self.assertEqual(len(students), 0)

    def test_remove_student_not_exists(self):
        result = remove_student(999)

        self.assertFalse(result)

    def test_count_passed_students(self):
        s1 = Student(1, "Alice", 20)
        s2 = Student(2, "Bob", 17)

        s1.add_grade(8)
        s2.add_grade(4)

        add_student(s1)
        add_student(s2)

        self.assertEqual(count_passed_students(), 1)

    def test_get_top_student(self):
        s1 = Student(1, "Alice", 20)
        s2 = Student(2, "Bob", 17)

        s1.add_grade(10)
        s2.add_grade(5)

        add_student(s1)
        add_student(s2)

        top = get_top_student()

        self.assertEqual(top.name, "Alice")

    def test_get_top_student_empty(self):
        top = get_top_student()

        self.assertIsNone(top)

    def test_get_adult_students(self):
        s1 = Student(1, "Alice", 20)
        s2 = Student(2, "Bob", 17)

        add_student(s1)
        add_student(s2)

        adults = get_adult_students()

        self.assertEqual(len(adults), 1)
        self.assertEqual(adults[0].name, "Alice")

    def test_calculate_statistics(self):
        s1 = Student(1, "Alice", 20)
        s2 = Student(2, "Bob", 18)

        add_student(s1)
        add_student(s2)

        stats = calculate_statistics()

        self.assertEqual(stats["total_students"], 2)
        self.assertEqual(stats["average_age"], 19)

    def test_calculate_statistics_empty(self):
        stats = calculate_statistics()

        self.assertEqual(stats["total_students"], 0)
        self.assertEqual(stats["average_age"], 0)

    # ===== Dictionary Tests =====

    def test_course_exists(self):
        self.assertIn("Python", courses)

    def test_course_teacher(self):
        self.assertEqual(courses["Python"], "Adrian")

    # ===== Tuple Tests =====

    def test_valid_courses_length(self):
        self.assertEqual(len(valid_courses), 3)

    def test_course_in_tuple(self):
        self.assertIn("Docker", valid_courses)

    # ===== Class Variable Test =====

    def test_school_name(self):
        self.assertEqual(Student.school_name, "Python Academy")


if __name__ == "__main__":
    unittest.main()
