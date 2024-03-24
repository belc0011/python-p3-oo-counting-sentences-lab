#!/usr/bin/env python3


class MyString:

    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if (isinstance(value, str)):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        word_length = len(self._value)
        if (self._value[word_length - 1] == '.'):
            return True
        else:
            return False
        
    def is_question(self):
        word_length = len(self._value)
        if (self.value[word_length - 1] == '?'):
            return True
        else:
            return False
    
    def is_exclamation(self):
        word_length = len(self._value)
        if (self.value[word_length - 1] == "!"):
            return True
        else:
            return False
        
    def count_sentences(self):
        count = 0
        repl_quest = self._value.replace('?', '.')
        repl_excl = repl_quest.replace('!', '.')
        repl_dup = repl_excl.replace('...', '.')
        repl_trip = repl_dup.replace('..', '.')
        print(repl_quest, repl_excl, repl_dup, repl_trip)
        for letter in repl_trip:
            if (letter == '.'):
                count += 1
        return count