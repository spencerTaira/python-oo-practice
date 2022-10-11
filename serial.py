from re import I


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Initialize serial code with start parameter"""
        self.initial_val = start - 1
        self.start_val = start - 1

    def generate(self):
        """Generate a new serial code then increment start value"""
        self.start_val += 1
        return self.start_val

    def reset(self):
        """Resets self.start to intiial start parameter"""
        self.start_val = self.initial_val