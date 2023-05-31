from .messages import ValidationMessages


class PhoneNumberDescriptor:
    """
    Descriptor for validating phone numbers.
    This descriptor validates that the assigned value is a numeric string.

    Usage:
    - Assign this descriptor to a class attribute to validate phone numbers.

    Example:
    class MyClass:
        phone_number = PhoneNumberDescriptor()
    my_instance = MyClass()
    my_instance.phone_number = "123456789"  # Valid
    my_instance.phone_number = "abc"  # Raises a ValueError

    """
    def __set_name__(self, owner, title):
        """
        Set the name of the attribute.
        This method is called by the class when the descriptor is assigned to an attribute.

        Args:
        owner: The owner class of the attribute.
        name: The name of the attribute.
        """
        self.title = title

    def __get__(self, instance, owner):
        """
        Get the value of the attribute.
        This method is called when the attribute is accessed.

        Args:
        instance: The instance of the class.
        owner: The owner class of the attribute.

        Returns:
        The value of the attribute.

        """
        return instance.__dict__[self.title]

    def __set__(self, instance, value):
        """
        Set the value of the attribute.
        This method is called when the attribute is assigned a value.

        Args:
        instance: The instance of the class.
        value: The value to be assigned to the attribute.

        Raises:
        ValueError: If the value is not a numeric string.

        """
        if not value.isdigit():
            raise ValueError(ValidationMessages.PHONE_NUMBER_MESSAGE)
        instance.__dict__[self.title] = value


class StringDescriptor:
    """
    Descriptor for validating strings.
    This descriptor validates that the assigned value is an alphabetic string.

    Usage:
    - Assign this descriptor to a class attribute to validate strings.

    Example:
    class MyClass:
        name = StringDescriptor()

    my_instance = MyClass()
    my_instance.name = "Amin"  # Valid
    my_instance.name = "123"  # Raises a ValueError

    """
    def __set_name__(self, owner, title):
        """
        Set the name of the attribute.
        This method is called by the class when the descriptor is assigned to an attribute.

        Args:
        owner: The owner class of the attribute.
        name: The name of the attribute.

        """
        self.title = title

    def __get__(self, instance, owner):
        """
        Get the value of the attribute.
        This method is called when the attribute is accessed.

        Args:
        instance: The instance of the class.
        owner: The owner class of the attribute.

        Returns:
        The value of the attribute.

        """
        return instance.__dict__[self.title]

    def __set__(self, instance, value):
        """
        Set the value of the attribute.
        This method is called when the attribute is assigned a value.

        Args:
        instance: The instance of the class.
        value: The value to be assigned to the attribute.

        Raises:
        ValueError: If the value is not an alphabetic string.

        """
        if not value.isalpha():
            raise ValueError(ValidationMessages.STRING_MESSAGE)
        instance.__dict__[self.title] = value


class StringValidator:
    """
    Class for validating string attributes.
    This class uses the StringDescriptor and PhoneNumberDescriptor to validate the name, last_name, and phone_number
    attributes.
    """
    name = StringDescriptor()
    last_name = StringDescriptor()
    phone_number = PhoneNumberDescriptor()

    def __init__(self, name, last_name, phone_number):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number