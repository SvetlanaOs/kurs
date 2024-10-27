class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)
    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open (name, encoding = 'utf-8') as file:
                s = file.read()
                s = s.lower()
                s = s.replace('\n', ' ')
                for k in [',', '.', '=', '!', '?', ';', ':', ' -']:
                    s = s.replace(k,'')
                    a = s.split(' ')
            all_words [name] = a
        return all_words
    def find(self, word):
        s = self.get_all_words()
        one_word = {}
        for k, v in s.items():
            x = v.index(word.lower())+1
            one_word [k] = x
        return one_word
    def count(self, word):
        s = self.get_all_words()
        one_word2 = {}
        for k, v in s.items():
            x = v.count(word.lower())
            one_word2[k] = x
        return one_word2



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))