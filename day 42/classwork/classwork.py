def remove_exclamation_marks(s):
    return s.replace('!', '')

def reverse(st):
    return ' '.join(st.split()[::-1])

def distinct(seq):
    seen = set()
    result = []
    for number in seq:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result

def distinct(seq):
    seen = set()
    result = []
    for number in seq:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result

def remove_duplicate_words(s):
    seen = set()
    result = []
    for word in s.split():
        if word not in seen:
            seen.add(word)
            result.append(word)
    return ' '.join(result)

def vaporcode(s):
    return '  '.join(c.upper() for c in s if c != ' ')


def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    
    count = 0
    
    while h > window:
        count += 1
        h *= bounce
        if h > window:
            count += 1
    
    return count