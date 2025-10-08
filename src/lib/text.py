import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    s=text
    if casefold :
        s=s.casefold()
    if yo2e :
        s=s.replace("ё","е")
        s=s.replace("Ё","Е")
    s=s.replace("\t"," ")
    s=s.replace("\r"," ")
    s=s.replace("\n"," ")
    s = ' '.join(s.split())
    s=s.strip()

    return s

def tokenize(text: str) -> list[str]:
    pattern = r'[\w-]+'
    tokenstext = re.findall(pattern, text)

    return tokenstext

def count_freq(tokens: list[str]) -> dict[str, int]:
    counts={}
    for word in tokens:
        counts[word]=counts.get(word,0)+1
    return counts

#{'a': 3, 'b': 2, 'c': 1}
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_freq=dict(sorted(freq.items()))


print (count_freq({'a': 3, 'b': 2, 'c': 1}))