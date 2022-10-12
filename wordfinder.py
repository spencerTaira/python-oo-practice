from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, filepath):
        """Initialize class properties."""
        self.filepath = filepath
        self.word_list = self.get_words()

    def __repr__(self):
        """Displays filepath of chosen file."""
        return f"Filepath: {self.filepath}"

    def get_words(self):
        """get_words: creates list from words in file and removes new line character."""
        file = open(f"{self.filepath}")
        dictionary = [line.replace("\n", "") for line in file]
        file.close()
        return dictionary

    def random(self):
        """random: returns a random word from list of words."""
        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: ignores blank lines or lines containing comments."""

    def get_words(self):
        """Eliminates empty lines and comments from word list"""
        return [word for word in super().get_words()
                if word != "" and not word.startswith("#")]
