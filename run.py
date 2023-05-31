import os
from kernel.student import Student
from kernel.database import Database
from helper.enums import Gender, Grade, ExitCommands
from helper.descriptors import StringValidator
from helper.messages import DisplayInputMessage, DisplayInfoMessage, ValidationMessages


database = Database()
database.connect()
database.create_table()
students = Student(database.connection)

with open('doc\introduction.txt', 'r') as file:
    content = file.read()
    print(content)

os.system('pause')
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
        name = input(DisplayInfoMessage.NAME)
        lastname = input(DisplayInfoMessage.LAST_NAME)
        phone_number = input(DisplayInfoMessage.PHONE_NUMBER)
        user_input = StringValidator(name, lastname, phone_number)
        valid_gender_choices = [item.value for item in Gender]
        gender = input(DisplayInfoMessage.GENDER)
        if gender in valid_gender_choices:
            birthdate = input(DisplayInfoMessage.BIRTH_DATE)
            valid_grade_choices = [item.value for item in Grade]
            grade =  input(DisplayInfoMessage.GRADE)
            if grade in valid_grade_choices:
                registration_date =  input(DisplayInfoMessage.REGISTRATION_DATE)
                graduation_date =  input(DisplayInfoMessage.GRADUATION_DATE)
                address =  input(DisplayInfoMessage.ADDRESS)
                students.update_student(
                    name,
                    lastname,
                    phone_number,
                    gender,
                    birthdate,
                    grade,
                    registration_date,
                    graduation_date,
                    address,
                    2
                )
    elif user_input == 'delete':
        last_name = input(DisplayInfoMessage.LAST_NAME)
        students.delete_student(last_name)
    elif user_input in validate_exit_commands:
        break
    else:
        print(ValidationMessages.VALIDATION_MESSAGE)
database.close_connection()