class GreekDictionary:
    def __init__(self):
        # fmt: off
        self.words = {
            "hello": "γεια σου",
            "thank you": "ευχαριστώ",
            "goodbye": "αντίο"
        }
        # fmt: on

    def __getitem__(self, english_word):
        return self.words.get(english_word, "Δεν βρέθηκε")

dictionary = GreekDictionary()

print(dictionary["hello"])
print(dictionary["thank you"])
print(dictionary["water"])
