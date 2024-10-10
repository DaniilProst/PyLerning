punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                content = content.lower()
                for punct in punctuation:
                    content = content.replace(punct, ' ')
                words = content.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        result_found = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1
                result_found[file_name] = position
        return result_found

    def count(self, word):
        word = word.lower()
        result_count = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            result_count[file_name] = count
        return result_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))