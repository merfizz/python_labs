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



print(tokenize(normalize("emoji 😀 не слово" )))