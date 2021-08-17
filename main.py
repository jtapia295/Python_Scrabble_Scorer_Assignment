import string
from Scrabble_Scorer import *

run_program()

OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def transform(old_dictionary):
    new_point_structure =  {}
    for letter in list(string.ascii_uppercase):
        for key in old_dictionary:
            if letter in old_dictionary[key]:
                new_point_structure[letter.lower()] = key
    return new_point_structure

new_point_structure = transform(OLD_POINT_STRUCTURE)

def scrabble_scorer(word):
    word_score = 0
    for char in word:
        word_score = word_score + new_point_structure[char]
    return word_score

# print(new_point_structure)

print('-'*50)
print(scrabble_scorer('python'))

