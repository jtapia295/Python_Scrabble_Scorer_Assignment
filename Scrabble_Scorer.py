import string

OLD_POINT_STRUCTURE = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}



# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.


def initial_prompt():
    print("Let's play some Scrabble!\n")
    print('Please enter your name\n')
    user_name = input('Please enter your name')
    for digit in list(string.digits):
        while digit in list(user_name):
            print('Sorry please only provide letters')
            user_name = input('Please enter your name')
    print('''\n\n''')
    print(f"Welcome {user_name}, please enter a word you'd like to use for scrabble")
    user_word = input('Please enter your word to grade').lower()   

    while len(user_word) > 30:
        print('Sorry that is too long')
        user_word = str(input('Please enter your word to grade')).lower()   
    for index in list(user_word):
        while index in list(str(string.digits)) or index in list(string.punctuation):
            print('Sorry we are only accepting letters')
            user_word = input('Please enter your word to grade').lower()   
    return [user_word,user_name]


def simple_scorer(word):
    word_score = len(word)
    return word_score

def vowel_bonus_scorer(word):
    vowels = ['a','e','i','o','u']
    word_score = len(word)
    for vowel in vowels:
        if vowel in word:
            word_score += 2
    return word_score

def scrabble_scorer(word):
    word_score = 0
    for char in word:
        word_score += new_point_structure[char]
    return word_score

scoring_algorithms = ()

def scorer_prompt(word):
    user_choice = int(input('Please select an algorithm'))
    while user_choice not in [0,1,2]:
        print('Sorry please enter on the digits 0,1 or 2')
        user_choice = int(input('Please select an algorithm'))
    if user_choice == 0:
        word_score = simple_scorer(word)
    elif user_choice == 1:
        word_score = vowel_bonus_scorer(word)
    else:
        word_score = scrabble_scorer(word)
    return word_score

def transform(old_dictionary):
    new_point_structure =  {}
    for letter in list(string.ascii_uppercase):
        for key in old_dictionary:
            if letter in old_dictionary[key]:
                new_point_structure[letter.lower()] = key
    new_point_structure[' '] = 0
    return new_point_structure

new_point_structure = transform(OLD_POINT_STRUCTURE)


def run_program():
    prompt_result = initial_prompt()
    word = prompt_result[0]
    name = prompt_result[1]
    word_score = 0
    print('''\n\n''')
    print(f'{name}, Which sorting algorithm would you like to use?')
    print('''\n\n''')
    print('''0 - Simple: One point per character \n1 - Vowel Bonus: Vowels are worth 3 points \n2 - Scrabble: Uses scrabble point system''')
    word_score = scorer_prompt(word)
    print(f'The score for the word {word} is : {word_score}')







