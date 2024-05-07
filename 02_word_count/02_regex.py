import re

WORD_RE = re.compile(r'[\w]+')
word = WORD_RE.findall('Big data, hadoop and map reduce. (hello world!)')
print(word)
