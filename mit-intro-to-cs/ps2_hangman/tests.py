###############################################################################
#
#   May 2021
#   Problem Set 2
#
#   Testing module for the hangman game
#
###############################################################################

import hangman

# randomly generated list of words from words.txt
word_list = [
    'annoying', 'denizen', 'conducing', 
    'nee', 'fate', 'pipits', 'coachmen', 
    'refraining', 'slurped', 'vases'
]

# helper functions
def get_test_results(passed, failed):
    print('Test results', 
        '\n    Passed:', passed, '/', passed+failed, 
        '\n    Failed:', failed, '/', passed+failed, 
        '\nRun again with detail = True for more info.')

# testing functions
cases_is_word_guessed = [
    ['apple', 'apple', True], 
    ['apple', ['a', 'p', 'p', 'l', 'e'], True], 
    ['apple', 'aple', False], 
    ['apple', ['e', 'i', 'k', 'p', 'r', 's'], False], 
    ['annoying', 'annoying', True],
    ['annoying', 'sdbjsa', False],
    ['nee', 'een', True],
    ['nee', 'i', False],
    ['nee', 'asdfas', False]
]
def test_is_word_guessed(test_cases, detail=False):
    '''
    Input:  test_cases (array):     first item -> secret_word, 
                                    second item -> letters_guessed, 
                                    third item -> expected outcome (bool)
    Output: detail=False:   test results prints number passed vs failed
            detail=True:    details on which tests passed/failed
    '''
    n = 1
    passed, failed = 0, 0
    for i in test_cases:
        secret_word = i[0]
        letters_guessed = i[1]
        expected_outcome = i[2]
        if expected_outcome == is_word_guessed(secret_word, letters_guessed): 
            passed += 1
        else:
            failed += 1
        if detail == True:
            print('Test case', n, 
                  '\n    secret_word:               ', secret_word, 
                  '\n    letters_guessed:           ', letters_guessed, 
                  '\n    is_word_guessed returns    ', is_word_guessed(secret_word, letters_guessed))
        n+=1 
    if detail == False: 
        get_test_results(passed, failed)

cases_get_guessed_word = [
    ['apple', ['z', 'e', 'i', 'p', 'l', 'a'], 'apple'], 
    ['apple', ['z', 'e', 'i', 'p' ], '_pp_e'], 
]
def test_get_guessed_word(test_cases, detail = False):
    n = 1
    passed, failed = 0, 0
    for i in test_cases:
        secret_word = i[0]
        letters_guessed = i[1]
        expected_outcome = i[2]
        if expected_outcome == is_word_guessed(secret_word, letters_guessed): 
            passed += 1
        else:
            failed += 1
        if detail == True:
            print('Test case', n, 
                  '\n    secret_word:               ', secret_word, 
                  '\n    letters_guessed:           ', letters_guessed, 
                  '\n    is_word_guessed returns    ', is_word_guessed(secret_word, letters_guessed))
        n+=1 
    if detail == False: 
        get_test_results(passed, failed)

