import re

match = re.search(r"^Hello", "Hello World")
print(match)  # <re.Match object; span=(0, 5), match='Hello'>