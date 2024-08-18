def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

def stray(arr):
    count = {}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num, cnt in count.items():
        if cnt == 1:
            return num
        


def dup(arry):
    def remove_consecutive_duplicates(s):
        if not s:
            return s
        result = [s[0]]
        for char in s[1:]:
            if char != result[-1]:
                result.append(char)
        return ''.join(result)
    
    return [remove_consecutive_duplicates(s) for s in arry]