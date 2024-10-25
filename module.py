import string
import os

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names  

    def get_all_words(self):
        all_words = {}  
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                       
                        line = line.lower().translate(str.maketrans('', '', string.punctuation))
                        words.extend(line.split()) 
                    all_words[file_name] = words  
            except FileNotFoundError:
                print(f'Файл {file_name} не найден.')
            except Exception as e:
                print(f'Ошибка при обработке файла {file_name}: {e}')
        return all_words

    def find(self, word):
        word = word.lower()  
        found = {}
        all_words = self.get_all_words()  
        for file_name, words in all_words.items():
            if word in words:
                found[file_name] = words.index(word) + 1  
        return found

    def count(self, word):
        word = word.lower() 
        count_dict = {}
        all_words = self.get_all_words() 
        for file_name, words in all_words.items():
            count_dict[file_name] = words.count(word) 
        return count_dict


if __name__ == "__main__":

    finder = WordsFinder('test_file.txt')
    
    print(finder.get_all_words())  
    print(finder.find('text'))  
    print(finder.count('text'))  
