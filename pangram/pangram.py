def is_pangram(sentence: str) -> bool:
    lower_sentence = sentence.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if lower_sentence.find(char) == -1:
            return False

    return True
