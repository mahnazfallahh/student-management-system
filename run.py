import os
import json
from kernel.models.student import Student
from core.database.database import Database, Base
from helper.enums import Gender, Grade, ExitCommands
from helper.descriptors import StringValidator
from services.brockerservices.rabbitMQ.consumer import RabbitMqConsumer
from services.brockerservices.rabbitMQ.producer import RabbitMqProducer
from helper.messages import DisplayInputMessage, DisplayInfoMessage, ValidationMessages


database = Database()
Base.metadata.create_all(database.engine)
students = Student()
producer = RabbitMqProducer()
consumer = RabbitMqConsumer()

def callback(ch, method, properties, body):
    data = json.loads(body)
    students.insert_student(**data)

while True:
    validate_exit_commands = [item.value for item in ExitCommands]
    user_input = input(DisplayInputMessage.FIRST_INPUT_MESSAGE)
    if user_input == 'add':
        name = input(DisplayInfoMessage.NAME)
        last_name = input(DisplayInfoMessage.LAST_NAME)
        phone_number =  input(DisplayInfoMessage.PHONE_NUMBER)
        user_input = StringValidator(name, last_name, phone_number)
        valid_gender_choices = [item.value for item in Gender]
        gender = input(DisplayInfoMessage.GENDER)
        if gender in valid_gender_choices:
            birthdate = input(DisplayInfoMessage.BIRTH_DATE)
            valid_grade_choices = [item.value for item in Grade]
            grade = input(DisplayInfoMessage.GRADE)
            if grade in valid_grade_choices:
                registration_date =  input(DisplayInfoMessage.REGISTRATION_DATE)
                graduation_date =  input(DisplayInfoMessage.GRADUATION_DATE)
                address =  input(DisplayInfoMessage.ADDRESS)
                student_data = {
                    'name': name,
                    'lastname': last_name,
                    'phone_number': phone_number,
                    'gender': gender,
                    'birthdate': birthdate,
                    'grade': grade,
                    'registration_date': registration_date,
                    'graduation_date': graduation_date,
                    'address': address
                }
                producer.connect()
                producer.send_message(student_data)
                producer.disconnect()
                students.insert_student(
                    name,
                    last_name,
                    phone_number,
                    gender, 
                    birthdate, 
                    grade, 
                    registration_date, 
                    graduation_date, 
                    address, 
                )
            else:
                print(ValidationMessages.VALIDATION_MESSAGE)
        else:
            print(ValidationMessages.VALIDATION_MESSAGE)
    elif user_input == 'read':
        students.read_students()
    elif user_input == 'update':
        lastname = input(DisplayInfoMessage.LAST_NAME)
        students.update_student(
            lastname
        )
    elif user_input == 'delete':
        last_name = input(DisplayInfoMessage.LAST_NAME)
        students.delete_student(last_name)
    elif user_input in validate_exit_commands:
        break
    else:
        print(ValidationMessages.VALIDATION_MESSAGE)

consumer.connect()
consumer.read_messages(callback)
consumer.disconnect()
database.close_connection()