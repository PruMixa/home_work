class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        pun = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for f in self.file_names:
            with open(f, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower().strip()
                    for sim in pun:
                        if sim != ' - ':
                            line = line.replace(sim, '')
                        else:
                            line = line.replace(sim, ' ')
                    words.extend(line.split())
                all_words[f] = words
        return all_words

    def find(self, word):
        word = word.lower()
        new_all_words = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                new_all_words[file_name] = words.index(word)
        return new_all_words

    def count(self, word):
        word = word.lower()
        new_all_words = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            new_all_words[file_name] = words.count(word)
        return new_all_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего