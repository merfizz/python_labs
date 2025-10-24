import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n

text = sys.stdin.readline()

normalized_text = normalize(text)

tokens = tokenize(normalized_text)

total_words = len(tokens)
freq_sorted = count_freq(tokens)
unique_words = len(freq_sorted)
top = top_n(freq_sorted, 5)

print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")

for word, count in top:
    print(f"{word}:{count}")
