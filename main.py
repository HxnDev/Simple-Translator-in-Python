import os
from tabulate import tabulate   
from googletrans import Translator


class Simple_Translator(object):
    def __init__(self, sentence, language):
        self.sentence = sentence
        self.language = language
        self.translator = Translator()

    def translation(self):
        translation = self.translator.translate(self.sentence, dest=self.language)
        data = [["Original Sentence: ", "Translated Sentence: "], [self.sentence, str(translation.text)]]
        return tabulate(data, headers="firstrow", tablefmt="fancy_grid")

    def __str__(self):
        return self.translation()


if __name__ == '__main__':
    sentence1 = input("Enter the string to translate = ")
    os.system("cls")
    print(Simple_Translator(sentence1, "en"))
