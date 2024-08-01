def dna_to_rna(dna):
    return dna.replace('T', 'U')


def find_short(s):
    words = s.split()
    shortest_length = min(len(word) for word in words)
    
    return shortest_length