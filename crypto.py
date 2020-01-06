from nltk.corpus import words

word_list = words.words()
import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encrypt(words, key):
    encrypted_words = ''

    for char in words.lower():
        if char in letters:
            encrypted_letter = letters[
                (letters.index(char.lower()) + key) % len(letters)
            ]
            encrypted_words += encrypted_letter
        else:
            encrypted_words += char
    return encrypted_words


def decrypt(words):
    def english_words(list_of_words):
        correct = 0
        for word in list_of_words:
            if word in word_list:
                correct += 1
        if correct / len(list_of_words) >= 0.5:
            return True
        return False

    for key in range(len(letters)):
        x = encrypt(words, (-1 * (key)))
        y = english_words(x.split(' '))
        if y:
            return x
