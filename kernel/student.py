import redis
import logging.config


logging.config.fileConfig(fname='Log/config.toml', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


class Student:
    """
    Student class for interacting with student records in a PostgreSQL database.
    This class provides methods to insert, read, update, and delete student records in the database.
    """
    def __init__(self, connection):
        """
        Initialize the Student instance.

        Args:
        - connection: A psycopg2 connection object representing the connection to the PostgreSQL database.
        """
        self.connection = connection
        self.redis = redis.Redis(host='redis', port=6379, db=0)

    def insert_student(
        self,
        name:str,
        lastname:str,
        phone_number:str,
        gender:str,
        birthdate:str,
        grade:str,
        registration_date:str,
        graduation_date:str,
        address:str
        )->None:
        """
        Insert a new student record into the database.

        Args:
        - name: The first name of the student.
        - lastname: The last name of the student.
        - phone_number: The phone number of the student.
        - gender: The gender of the student.
        - birthdate: The birthdate of the student.
        - grade: The grade of the student.
        - registration_date: The registration date of the student.
        - graduation_date: The graduation date of the student.
        - address: The address of the student.

        """
        query = """
            INSERT INTO students (
                name,
                lastname,
                gender,
                birthdate,
                grade,
                registration_date,
                graduation_date,
                address,
                phone_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
        records = (
            name,
            lastname,
            gender,
            birthdate,
            grade,
            registration_date,
            graduation_date,
            address,
            phone_number
        )
        cursor = self.connection.cursor()
        cursor.execute(query, records)
        self.connection.commit()
        cursor.close()
        print(f"Student <<{lastname}>> inserted successfully!")
        logger.info(f"Student <<{lastname}>> inserted successfully!")

    def read_students(self):
        """
        Read all student records from the database.
        This method retrieves all student records from the 'students' table in the database and prints the details.

        """
        if self.redis.exists("students"):
            records = self.redis.get("students")
            print("retrieving students from cache ... ")
            logger.info("retrieving students from cache ...")
        else:
            query = "SELECT * FROM students"
            cursor = self.connection.cursor()
            cursor.execute(query)
            records = cursor.fetchall()
            for record in records:
                print("Id:", record[0])
                print("Name:", record[1])
                print("LastName:", record[2])
                print("Gender:", record[3])
                print("Birthdate:", record[4])
                print("Grade:", record[5])
                print("GraduationDate:", record[6])
                print("Address:", record[7])
                print("PhoneNumber:", record[8])
            cursor.close()
            self.redis.set("students", records)
            logger.info("user get a list of students.")

    def update_student(
        self,
        name:str,
        lastname:str,
        phone_number:str,
        gender:str,
        birthdate:str,
        grade:str,
        registration_date:str,
        graduation_date:str,
        address:str,
        pk:int)->None:
        """
        Update an existing student record in the database.

        Args:
        - name: The updated first name of the student.
        - lastname: The updated last name of the student.
        - phone_number: The updated phone number of the student.
        - gender: The updated gender of the student .
        """
        query = """
        UPDATE students
        SET name = COALESCE(%s, name),
            lastname = COALESCE(%s, lastname),
            gender = COALESCE(%s, gender),
            birthdate = COALESCE(%s, birthdate),
            grade = COALESCE(%s, grade),
            registration_date = COALESCE(%s, registration_date),
            graduation_date = COALESCE(%s, graduation_date),
            address = COALESCE(%s, address),
            phone_number = COALESCE(%s, phone_number)
        WHERE id = %s
        """
        records= (name, lastname, gender, birthdate, grade, registration_date, graduation_date, address, phone_number, pk)
        cursor = self.connection.cursor()
        cursor.execute(query, records)
        self.connection.commit()
        cursor.close()
        print("Student updated successfully!")
        logger.info(f"Student {lastname} updated successfully!")

    def delete_student(self, lastname:str)->None:
        """
        Delete an existing student record in the database.
        """
        query = "DELETE FROM students WHERE lastname = %s"
        record = (lastname,)
        cursor = self.connection.cursor()
        cursor.execute(query, record)
        self.connection.commit()
        cursor.close()
        print(f"Student <<{lastname}>> deleted successfully!")
        logger.info(f"Student <<{lastname}>> deleted successfully!")
