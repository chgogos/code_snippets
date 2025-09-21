file1 = "python.txt"
file2 = "java.txt"

with open(file1, "r", encoding="utf-8") as f:
    text1 = f.read()

with open(file2, "r", encoding="utf-8") as f:
    text2 = f.read()

text1 = text1.lower()
text2 = text2.lower()

for ch in [".", ",", ";", ":", "!", "?", "(", ")", '"', "'"]:
    text1 = text1.replace(ch, "")
    text2 = text2.replace(ch, "")

words1 = set(text1.split())
words2 = set(text2.split())
common_words = words1.intersection(words2)
print("Αριθμός κοινών λέξεων:", len(common_words))
print("Κοινές λέξεις:", ", ".join(sorted(common_words)))
