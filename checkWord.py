from uzwords import words
from difflib import get_close_matches

def checkWord(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False # this word doesn't exists

    if word in matches:
        available = True # exists
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))

    return {'available': available, 'matches': matches}

if __name__ == '__main__':
    print(checkWord("нокк"))
    print(checkWord("ҳато"))
    print(checkWord("хато"))
    print(checkWord("олма"))