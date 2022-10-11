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
        self.initial_val = start
        self.curr_val = start

    def __repr__(self):
        return f"Start = {self.initial_val} and Next Serial Code is {self.curr_val}"

    def generate(self):
        """Returning curr_val"""
        self.curr_val += 1
        return self.curr_val - 1

    def reset(self):
        """Resets self.start to intiial start parameter"""
        self.curr_val = self.initial_val