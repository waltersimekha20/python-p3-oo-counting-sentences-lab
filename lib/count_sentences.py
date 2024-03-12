# Save this code in a file named 'count_sentences.py'

class MyString:
    def __init__(self, value=None):
        self.value = value

    def is_sentence(self):
        if self.value is None or not isinstance(self.value, str):
            print("The value must be a string.")
            return False
        return self.value.endswith(".")

    def is_question(self):
        if self.value is None or not isinstance(self.value, str):
            print("The value must be a string.")
            return False
        return self.value.endswith("?")

    def is_exclamation(self):
        if self.value is None or not isinstance(self.value, str):
            print("The value must be a string.")
            return False
        return self.value.endswith("!")

    def count_sentences(self):
        if self.value is None or not isinstance(self.value, str):
            print("The value must be a string.")
            return 0
        sentences = filter(None, [s.strip() for s in self.value.split('.') + self.value.split('?') + self.value.split('!')])
        return len(sentences)
