import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Функция приводит текст к единому регистру и стилю"""
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
    """Функция разбивает текст на «слова» по небуквенно-цифровым разделителям"""
    pattern = r'[\w-]+'
    tokenstext = re.findall(pattern, text)

    return tokenstext

def count_freq(tokens: list[str]) -> dict[str, int]:
    """Функция возвращает словарь слово - количество"""
    counts={}
    for word in tokens:
        counts[word]=counts.get(word,0)+1
    return counts

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Функция возвращает топ-N по убыванию частоты"""
    sorted_freq= sorted(freq.items(),key=lambda item: [-item[1], item[0]])
    top_n=[]

    for i in range(min(n, len(sorted_freq))):
        top_n.append((sorted_freq[i][0], sorted_freq[i][1]))

    return top_n

print( normalize("ПрИвЕт\nМИр\t"))
print( normalize("ёжик, Ёлка"))
print( normalize("Hello\r\nWorld"))
print( normalize("  двойные   пробелы  "))

print( tokenize(normalize("привет мир")))
print( tokenize(normalize("hello,world!!!")))
print( tokenize(normalize("2025 год")))
print( tokenize(normalize("emoji 😀 не слово")))

print (count_freq(["a","b","a","c","b","a"]),top_n(count_freq(["a","b","a","c","b","a"]),2))
print (count_freq(["bb","aa","bb","aa","cc"]),top_n(count_freq(["bb","aa","bb","aa","cc"]),2))


