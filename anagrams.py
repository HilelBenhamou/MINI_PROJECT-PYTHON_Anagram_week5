
from anagram_checker import AnagramChecker

if __name__ == "__main__":
    menu=input('''Welcome to the Anagram Word Game
    If you want to play, press 1
    If you want to exit, press 2\n\n''')
    if menu=='1':
        ask= input('Put a word !\n')
        wordasked=AnagramChecker(ask)
        print(wordasked.is_valid_word())
        wordasked.get_anagrams()

    elif menu=='2':
        print('Goodbye My friend !')

