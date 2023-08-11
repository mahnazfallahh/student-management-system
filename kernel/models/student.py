import redis
import toml
import json
# import logging.config
from core.database.database import Database, Base
from sqlalchemy.orm import sessionmaker
from services.cachservices.redis import RedisCache
from helper.messages import StudentMessage
from services.brockerservices.rabbitMQ.consumer import RabbitMqConsumer
from services.brockerservices.rabbitMQ.producer import RabbitMqProducer
from sqlalchemy import create_engine, Column, Integer, String, Date
# logging.config.fileConfig('Log/config.toml', disable_existing_loggers=False)
# logger = logging.getLogger(__name__)


class Student(Base):
    """
    Student class for interacting with student records in a PostgreSQL database.
    This class provides methods to insert, read, update, and delete student records in the database.
    """
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    gender = Column(String)
    birthdate = Column(Date)
    grade = Column(String)
    registration_date = Column(Date)
    graduation_date = Column(Date)
    address = Column(String)
    phone_number = Column(String)

    def __init__(self):
        self.db = Database()
        setting = RedisCache()
        redis_setting = setting.get_redis_settings()
        self.redis = redis.Redis(
            host=redis_setting["host"],
            port=redis_setting["port"],
            db=redis_setting["db"]
        ) 
        self.session = self.db.get_session()
        self.sender = RabbitMqProducer()
        self.reciever = RabbitMqConsumer()

    def __repr__(self):
        return f"<Student(name='{self.name}', lastname='{self.lastname}', " \
               f"gender='{self.gender}', birthdate='{self.birthdate}', " \
               f"grade='{self.grade}', registration_date='{self.registration_date}', " \
               f"graduation_date='{self.graduation_date}', address='{self.address}', " \
               f"phone_number='{self.phone_number}')>"

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

        student_data = {
        'name': name,
        'lastname': lastname,
        'phone_number': phone_number,
        'gender': gender,
        'birthdate': birthdate,
        'grade': grade,
        'registration_date': registration_date,
        'graduation_date': graduation_date,
        'address': address
    }
        self.sender.connect()
        self.sender.send_message(student_data)
        self.sender.disconnect()
        student = Student()
        student.name = name
        student.lastname = lastname
        student.gender = gender
        student.birthdate = birthdate
        student.grade = grade
        student.registration_date = registration_date
        student.graduation_date = graduation_date
        student.address = address
        student.phone_number = phone_number
        self.session.add(student)
        self.session.commit()
        print(f"Student <<{lastname}>> inserted successfully!")

    def read_students(self):
        """
        Read all student records from the database.
        This method retrieves all student records from the 'students' table in the database and prints the details.

        """
        if self.redis.exists("student"):
            records = self.redis.get("student")
            students = json.loads(records)
            print(students)
            print(StudentMessage.REDIS_MESSAGE)
        else:
            students = self.session.query(Student).all()
            records = [student.serialize() for student in students]
            self.redis.set("student", json.dumps(records))
        return students
            

    def update_student(
        self,
        lastname:str
        )->None:
        """
        Update an existing student record in the database.

        Args:
        - name: The updated first name of the student.
        - lastname: The updated last name of the student.
        - phone_number: The updated phone number of the student.
        - gender: The updated gender of the student .
        """
        student = self.session.query(Student).filter_by(lastname=lastname).first()
        if student is None:
            print(f"No student with lastname <<{lastname}>> found.")
            return
        student.lastname = lastname

        self.session.commit()
        print(f"Student <<{lastname}>> updated successfully!")

    def delete_student(self, lastname:str)->None:
        """
        Delete an existing student record in the database.
        """
        student = self.session.query(Student).filter_by(lastname=lastname).first()
        if student is None:
            print(f"No student with lastname <<{lastname}>> found.")
            return

        self.session.delete(student)
        self.session.commit()
        print(f"Student <<{lastname}>> deleted successfully!")
