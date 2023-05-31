import unittest
from unittest import TestCase
from unittest.mock import MagicMock
from kernel.student import Student


class StudentTestCase(TestCase):
    def setUp(self):
        self.connection = MagicMock()
        self.student = Student(self.connection)

    def test_insert_student(self):
        self.connection.cursor = MagicMock(return_value=self.connection)
        self.student.insert_student(
            name="mahnaz",
            lastname="fallah",
            phone_number="123456789",
            gender="Male",
            birthdate="2000-14-2",
            grade="C",
            registration_date="1999-2-3",
            graduation_date="2025-01-01",
            address="Tehran"
        )
        self.connection.cursor.assert_called_once()
        self.connection.commit.assert_called_once()
        self.connection.close.assert_called_once()

    def test_read_students(self):
        self.student.read_students()
        self.connection.cursor.assert_called_once()

    def test_update_student(self):
        self.connection.cursor = MagicMock(return_value=self.connection)
        self.student.update_student(
            name="jack",
            lastname="han",
            phone_number="123456789",
            gender="female",
            birthdate="2000-01-01",
            grade="A",
            registration_date="2023-01-01",
            graduation_date="2025-01-01",
            address="Us",
            pk=1
        )
        self.connection.cursor.assert_called_once()
        self.connection.commit.assert_called_once()
        self.connection.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()