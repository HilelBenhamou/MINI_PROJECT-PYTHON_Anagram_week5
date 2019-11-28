import os

class AnagramChecker:
    def __init__(self,word):
        self.word = word
        # myfile = open("new.txt")

    def is_valid_word(self):
        numberlist=['0','1','2','3','4','5','6','7','8','9','.',',',';',':','!','/','?','*','+','-','&','#','(','[','-','|','_','@',')',']','=','}']
        for i in self.word:
            if i == ' ':
                return 'Only one word should be input'
            elif i in numberlist :
                    return 'No numbers or special Characters allowed in it'

        with open("sowpods.txt") as f:
            info = f.readlines()
        for line in info:
            if self.word.upper() in line:
                return 'Yes'
        else:
            return 'No'

    def get_anagrams(self):
        self.word = ','.join(self.word).upper()
        wordInList = self.word.split(',')
        # print(wordInList)
        with open("sowpods.txt") as f:
            info = f.readlines()
        for line in info:
            if len(wordInList) == (len(line)-1):
                line= ','.join(line)
                lineList=line.split(',')
                lineList.pop()
                # lineList.sort()
                # wordInList.sort()
                if sorted(wordInList) == sorted(lineList):
                    print(f'Here are all the anagrams of {self.word} : {lineList}')




    # def is_anagram(self,word1, word2):
    #     pass


# if __name__ == "__main__":
#     menu=input('''Welcome to the Anagram Word Game
#     If you want to play, press 1
#     If you want to exit, press 2\n\n''')
#     if menu=='1':
#         ask= input('Put a word !\n')
#         wordasked=AnagramChecker(ask)
#         print(wordasked.is_valid_word())
#         wordasked.get_anagrams()
#
#     elif menu=='2':
#         print('Goodbye My friend !')
