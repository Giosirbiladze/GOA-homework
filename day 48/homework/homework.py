def order(sentence):
    if not sentence:
        return ""

    words = sentence.split()
    words_with_numbers = []
    for word in words:
        number = int(''.join(filter(str.isdigit, word)))
        words_with_numbers.append((number, word))
    
    words_with_numbers.sort(key=lambda x: x[0])
    sorted_words = [word for _, word in words_with_numbers]
    
    return ' '.join(sorted_words)
