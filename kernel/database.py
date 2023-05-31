import toml
import psycopg2
import logging.config

from designs.singleton import Singleton


logger = logging.getLogger('database')

class Database(metaclass=Singleton):
    """
    Database class for handling PostgreSQL database operations.
    This class provides methods to connect to a PostgreSQL database, close the connection, and create a table.

    Usage:
    - Create an instance of the Database class to interact with the database.

    Example:
    database = Database()
    database.connect()
    database.create_table()
    database.close_connection()

    """
    def __init__(self):
        self.connection = None

    def connect(self):
        """
        Connect to the PostgreSQL database.
        This method reads the database configuration from a TOML file, establishes a connection to the database,
        and logs a success message if the connection is successful.

        """
        try:
            config = toml.load("database.toml")['database']
            self.connection = psycopg2.connect(
                host=config['host'],
                database=config['database'],
                user=config['user'],
                password=config['password']
            )
            logger.info("Connected to PostgreSQL successfully!")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)

    def close_connection(self):
        """
        Close the database connection.
        This method closes the connection to the PostgreSQL database and logs a message confirming the closure.
        """
        if self.connection is not None:
            self.connection.close()
            logger.info("PostgreSQL connection is closed.")

    def create_table(self):
        """
        Create a table in the PostgreSQL database.
        This method executes a SQL query to create a table named 'students' if it doesn't already exist in the database.
        """
        query = """
            CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            lastname VARCHAR(50) NOT NULL,
            gender VARCHAR(10) NOT NULL,
            birthdate DATE NOT NULL,
            grade VARCHAR(10) NOT NULL,
            registration_date DATE NOT NULL,
            graduation_date DATE NOT NULL,
            address VARCHAR(100) NOT NULL,
            phone_number VARCHAR(20)
        )
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        cursor.close()
        logger.info("Table created successfully!")
