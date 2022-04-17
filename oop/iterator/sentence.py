"""Module for Iterator and Generator construction theme"""
import re


class TypeError(Exception):
    """Define typerror for exception"""

    def __init__(self, exc):
        self.msg = f"Expected a str, not {type(exc)}."

    def __str__(self):
        return self.msg


class ValueError(Exception):
    """Define valuerror for exception"""

    def __init__(self):
        self.msg = f'Expected end symbol: {Sentence._end_chars}'

    def __str__(self):
        return self.msg


class MultipleSentencesError(Exception):
    """Define for multiply sentences exception"""

    def __init__(self):
        self.msg = 'Object take only 1 sentence'

    def __str__(self):
        return self.msg


class SentenceIterator:
    """Class for iterating and sentence object"""

    def __init__(self, sentence):
        self._words = iter(sentence.split())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self._words)


class Sentence:
    """Class that define sentence object with methods to recognize letters and symbols"""
    _other_chars = '&!?$;№)(*&".,'
    _end_chars = ('.', '...', '!', '?')
    __pattern = r"[\w\s]+?(\!|[\.]{1,3}|\?)$"

    def __init__(self, sentence):
        try:
            if not isinstance(sentence, str):
                raise TypeError(sentence)

            if sentence.endswith(Sentence._end_chars) is False:
                raise ValueError

            if re.match(pattern=Sentence.__pattern, string=sentence) is None:
                raise MultipleSentencesError

            sentence = re.match(pattern=Sentence.__pattern, string=sentence).group()

            self.sentence = ' '.join([sentence]).strip('.?!')

        except TypeError as err:
            print(err)
        except ValueError as err:
            print(err)
        except MultipleSentencesError as err:
            print(err)

    def __repr__(self):
        words, other_chars = len(self.words()), len(self.other_chars())
        return f"<{self.__class__.__name__}(words={words}, other_chars={other_chars}))>"

    def __getitem__(self, item):
        try:
            if isinstance(item, slice):
                return self.sentence[item.start:item.step:item.stop]
            if isinstance(item, int):
                return ''.join(str(item) for item in self.sentence.split()[item])
        except IndexError:
            return 'There is no item to get'
        return self.sentence[item]

    def __iter__(self):
        return SentenceIterator(self.sentence)

    def _words(self):
        """Return a queue of words in sentence"""
        for word in self.sentence.split():
            yield word

    def words(self):
        """Return a list of words in sentence"""
        return self.sentence.split()

    def other_chars(self):
        """Return non letter characters in sentence"""
        print(self.sentence)
        return list(char for char in re.findall(r"[^A-z\s]", self.sentence))


# s = Sentence('Jelly 2390 Fish!')
# print(s.other_chars())
# print(s._words)
# print(s.words())
# print(s[1])
# print(s[:])
