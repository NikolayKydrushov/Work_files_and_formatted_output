from pprint import pprint
import io

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = { }
        signs = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                new_text = ""
                for c in text:
                    if c not in signs or c == '-':
                        new_text += c
                text = new_text
                words = text.split()
                all_words[file_name] = words
        return all_words


    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            index = words.index(word)
            results[filename] = index + 1
        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for filename, words in all_words.items():
            count = words.count(word)
            results[filename] = count
        return results



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего