# creating a function that returns vowels
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

# Main function that counts the words
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
        # Words Score in Python 
            score += 1
        # Words Score in Python 
    return score

# taking the input from user
n = int(input())
words = input().split()
print(score_words(words))