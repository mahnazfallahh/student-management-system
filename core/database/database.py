import toml
# import logging.config
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from designs.singleton import Singleton

Base = declarative_base()
# logger = logging.getLogger('database')

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
        self.engine = self.create_engine()
        self.session = self.get_session()
        
    
    def create_engine(self):
        """
        Connect to the PostgreSQL database.
        This method reads the database configuration from a TOML file, establishes a connection to the database,
        and logs a success message if the connection is successful.

        """
        try:
            config = toml.load("database.toml")['database']
            engine = create_engine(
                f"postgresql://{config['user']}:{config['password']}@{config['host']}/{config['database']}"
            )
            return engine
        except Exception as error:
            print("Error while connecting to PostgreSQL:", error)

    def get_session(self):
        return Session(self.engine)
    
    def close_connection(self):
        """
        Close the database connection.
        This method closes the connection to the PostgreSQL database and logs a message confirming the closure.
        """
        if self.session is not None:
            self.session.close()
            # logger.info("PostgreSQL connection is closed.")
