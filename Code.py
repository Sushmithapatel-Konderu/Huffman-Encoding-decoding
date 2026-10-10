
import random

def jumble_word(word):
    if len(word) <= 3:
        return word

    middle = list(word[1:-1])
    random.shuffle(middle)

    return word[0] + ''.join(middle) + word[-1]

sentence = input("Enter a sentence: ")

result = ' '.join(jumble_word(word) for word in sentence.split())

print("Jumbled sentence:", result)
