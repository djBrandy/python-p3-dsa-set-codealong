class MySet:

    pass
class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.add(value)

    def __str__(self):
        set_list = [str(key) for key in self.dictionary.keys()]
        return f'MySet: {{{",".join(set_list)}}}'

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        if self.has(value):
            del self.dictionary[value]
        return self

    def has(self, value):
        return value in self.dictionary

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary = {}
        return self

    def is_empty(self):
        return self.size() == 0

