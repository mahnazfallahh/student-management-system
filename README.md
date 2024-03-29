# Student System Management

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
  - [RabbitMQ](#rabbitmq)
  - [Docker](#docker)
  - [Redis](#redis)
  - [Sqlalchemy](#sqlalchemy)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)

## Introduction

Welcome to Student Management System! This project is designed to do CRUD operation on student information. By leveraging technologies such as RabbitMQ, Redis, and PostgreSQL, along with advanced concepts like descriptors and enums i also use Sqlalchemy.

## Technologies Used

### RabbitMQ

the role of RabbitMQ in my project:
Message Queues
Imagine we have a process that needs to insert student records into the database. Instead of performing the database insertion directly, we send a message to a queue in RabbitMQ that signifies the request to insert a new student record. Another part of the system, specifically designed to handle database operations, listens to this queue. When a message arrives, it processes the request and performs the necessary database actions. This architecture not only improves the responsiveness of the application but also enhances its scalability.

### Redis

Detail how Redis is utilized within my project:

Data Caching, there are parts of the system that repeatedly fetch the same data from a database, causing unnecessary delays and potentially straining the database server. To mitigate this, Redis is utilized as a caching mechanism. Whenever data is fetched from the database, a copy is also stored in Redis. Subsequent requests for the same data can then be fulfilled directly from Redis, significantly reducing the load on the database server and improving response times. This caching approach ensures that frequently accessed data is readily available, leading to a smoother user experience.

### Sqlalchemy

Detail how sqlalchemy is utilized within my project:
In student system management, the SQLAlchemy library is leveraged extensively to interact with the PostgreSQL database, manage data models, and perform database operations efficiently. SQLAlchemy provides an Object-Relational Mapping (ORM) approach that allows you to work with database records as Python objects. 

### Docker 

In student system management, Docker is employed to create containerized environments that encapsulate the application, its dependencies, and services in a consistent and isolated manner. Docker simplifies deployment, enhances portability, and streamlines development across different environments. 


### Descriptors

the purpose of descriptors in my project, focusing on how they are used for data validation or customization:
Data Validation
One of the key reasons descriptors are employed is to enforce data validation rules on specific attributes. For instance, the PhoneNumberDescriptor ensures that the assigned value to the phone_number attribute is a valid numeric string. This prevents invalid data from being stored in the attribute and helps maintain data integrity. By using descriptors for validation, we can guarantee that data adheres to specific standards and is suitable for its intended purpose.

Customization of Attribute Behavior
Descriptors allow us to customize the behavior of attributes beyond simple assignment and retrieval. In student system management, the StringDescriptor exemplifies this by enforcing that the assigned value to the attribute must be an alphabetic string. This customization enhances the robustness of the application by ensuring that attribute values meet specific criteria. It also provides an intuitive way to communicate the expected format of attribute values to developers working with the code.

Reusability
Descriptors promote reusability by encapsulating validation logic in a single place. This means that the same descriptor can be applied to multiple attributes across different classes, providing consistent validation rules throughout the application. This reuse of descriptors not only saves development time but also ensures that the same data validation standards are upheld across various parts of the project.

### Enums

the purpose of enums in my project, including how they help define predefined values and improve code readability:

Code Readability and Intent Communication
Enums provide meaningful names to represent specific values, making the code self-explanatory and easy to understand. In student system management, the Gender and Grade enums exemplify this advantage. When you encounter code that references Gender.MALE or Grade.A, the intent behind these values is clear without requiring additional comments or explanations. This improved readability enhances collaboration among developers and simplifies the onboarding process for new team members.

Data Consistency and Valid Options
Enums ensure that attribute values adhere to a predefined set of valid options. In student system management, the Gender enum ensures that the only acceptable values for the gender attribute are MALE or FEMALE. Similarly, the Grade enum enforces that the grade attribute can only be A, B, or C. By restricting attribute values to a well-defined set, enums prevent invalid or unexpected data from entering the system, leading to more reliable and consistent behavior.

### Installation

1. Clone the repository: `git clone https://github.com/mahnazfallahh/student-management-system.git`
2. Navigate to the project directory: `cd crud`
3. Install dependencies: `pip install -r requirements.txt`

### Running the Application
1. run docker-compose file by "sudo docker-compose up -d" command .
2. for running program just run "run.py" module .  
