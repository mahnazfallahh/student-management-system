from enum import Enum


class Gender(Enum):
    """
    Enumeration for representing gender.
    This enumeration defines two gender options: MALE and FEMALE.
    """
    MALE = 'male'
    FEMALE = 'female'


class Grade(Enum):
    """
    Enumeration for representing grade.
    This enumeration defines three grade options: A, B, C.
    """
    A = 'a'
    B = 'b'
    C = 'c'

class ExitCommands(Enum):
    """
    Enumeration for representing exit commands.
    This enumeration defines two exit commands. options: E, Q.
    """
    E = 'e'
    Q = 'q'