from enum import StrEnum


class DisplayInputMessage(StrEnum):
    """
    Enumeration for displaying input messages.
    This enumeration defines input messages to be displayed for user input.

    Usage:
    - Use the DisplayInputMessage enum to display input messages .

    Example:
    input_message = DisplayInputMessage.FIRST_INPUT_MESSAGE

    """
    FIRST_INPUT_MESSAGE = "please choose one option :"

class DisplayInfoMessage(StrEnum):
    """
    Enumeration for displaying info messages.
    This enumeration defines info messages to be displayed for user input.

    Usage:
    - Use the DisplayInfoMessage enum to display info messages.

    Example:
    info_message = DisplayInfoMessage.NAME
    """

    NAME = "please enter first name :"
    LAST_NAME = "please enter last name:"
    PHONE_NUMBER = "please enter phone number:"
    GENDER = "please enter gender (Male/Female):"
    BIRTH_DATE = "please input birthdate:"
    GRADE = "please enter grade (A/B/C):"
    REGISTRATION_DATE = "please enter registration_date:"
    GRADUATION_DATE = "please enter graduation_date:"
    ADDRESS = "please enter address:"


class ValidationMessages(StrEnum):
    """
    Enumeration for validation messages.
    This enumeration defines messages for input validation errors.

    Usage:
    - Use the ValidationMessages enum to retrieve validation error messages.

    Example:
    validation_message = ValidationMessages.VALIDATION_MESSAGE

    """
    VALIDATION_MESSAGE = "invalid choice !!"
    PHONE_NUMBER_MESSAGE = "input must be your phone number."
    STRING_MESSAGE = "input must be alphabet."