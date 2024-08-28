def pig_it(text):
    words = text.split()
    result = []
    
    for word in words:
        if word.isalpha() or word.isalnum():
            pig_word = word[1:] + word[0] + 'ay'
            result.append(pig_word)
        else:
            result.append(word)
    
    return ' '.join(result)

def duplicate_count(text):
    from collections import Counter

    text = text.lower()
    counts = Counter(text)
    return sum(1 for count in counts.values() if count > 1)
