from Example import Example
from Analyzer import Analyzer

e = Example(8, 6)
print(e.add())

s = 'This is a test of the class.'

analyzer = Analyzer(s)

print(analyzer.words)
print('Number of word: ', analyzer.number_of_words())
print('Number of words starting with "t": ', analyzer.starts_with('t'))
print('Number of 2-letter words: ', analyzer.number_with_length(2))