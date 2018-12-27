import re


def abbreviate(words: str):
    return ''.join(re.findall(r'\b[A-Z]', words.upper().replace("'", '')))
