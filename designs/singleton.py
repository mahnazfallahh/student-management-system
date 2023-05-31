
class Singleton(type):
    """
    Singleton metaclass.
    This metaclass ensures that only one instance of a class can be created.
    
    Usage:
    - Define a class with this metaclass to make it a singleton.
    - When the class is instantiated, the first instance is created.
    - Subsequent calls to create an instance will return the same instance.

    Example:
    class MyClass(metaclass=Singleton):
        pass
    instance1 = MyClass()  # Creates the first instance
    instance2 = MyClass()  # Returns the same instance as instance1
    """
    _instance = None
    
    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance