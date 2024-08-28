def accum(st):
    parts = []
    for i, char in enumerate(st):
        part = char.upper() + char.lower() * i
        parts.append(part)
    return '-'.join(parts)