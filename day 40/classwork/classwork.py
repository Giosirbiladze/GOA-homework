def sum_str(a, b):
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    
    int_a = int(a)
    int_b = int(b)
    
    result = int_a + int_b
    
    return str(result)



def flick_switch(lst):
    result = []
    flip = True
    
    for item in lst:
        if item == 'flick':
            flip = not flip
        result.append(flip)
    
    return result


def open_or_senior(data):
    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

def is_anagram(test, original):
    return sorted(test.lower()) == sorted(original.lower())


def is_isogram(string):
    string = string.lower()
    seen_letters = set()
    
    for letter in string:
        if letter in seen_letters:
            return False
        seen_letters.add(letter)
    
    return True

def get_middle(s):
    length = len(s)
    if length % 2 == 1:
        return s[length // 2]
    else:
        return s[(length // 2) - 1:(length // 2) + 1]


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')