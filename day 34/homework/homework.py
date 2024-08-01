def find_short(s):
    list1 = s.split(" ")


    word_len = len(list1[0])
    for i in list1:
        if len(i) < word_len:
            word_len = len(i)
    
    # word_len = 3
    return word_len

print(find_short("bitcoin take over the world maybe who knows perhaps"))

# list1 იქნება: ['bitcoin', 'take', 'over', 'the', 'world', 'maybe', 'who', 'knows', 'perhaps']
# სიგრძე word_len პირველ სიტყვაზე ('bitcoin') იქნება 7.
# ციკლის შემდეგ, ყველაზე მოკლე სიტყვა იქნება 'the', რომლის სიგრძეა 3.
# find_short ფუნქცია დააბრუნებს 3.
# ფუნქცია  განიხილავს  თითოეული სიტყვას და პოულობს ყველაზე მოკლე სიტყვის სიგრძეს.

s1 = "apple banana cherry"
result1 = s1.split()  
print(result1)  


s2 = "dog,cat,rabbit"
result2 = s2.split(',')  
print(result2)  


s3 = "2024:08:01"
result3 = s3.split(':')  
print(result3)  


s4 = "file-2024-version1"
result4 = s4.split('-')  
print(result4) 


s5 = "one;two;three;four"
result5 = s5.split(';')  
print(result5) 


s6 = "user1@example.com"
result6 = s6.split('@')  
print(result6)  


s7 = "part1part2part3"
result7 = s7.split('1') 
print(result7)  


s8 = "hello!world!python"
result8 = s8.split('!')  
print(result8)  


s9 = "path/to/file"
result9 = s9.split('/')  
print(result9)  


s10 = "www.example.com"
result10 = s10.split('.')   
print(result10) 
#code wars 1 
def reverse_words(text):
    words = text.split(' ')
    reversed_word = ' '.join(word[::-1] for word in words)
    return reversed_word
#code wars 2
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Input must be between 0 and 12, inclusive.")
        
        
    result = 1
    
    
    for i in range(1, n+1):
        result *= i
        
    return result