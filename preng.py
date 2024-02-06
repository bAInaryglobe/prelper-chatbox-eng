import string
import random



def preng_input():
    user_input = input("Please enter something: ")
    return user_input


# a is a list of all lowercase and uppercase letters
a = list(string.ascii_letters)

# b is a list of numbers from 0 to 9
b = list(range(10))

# c is a list of all common punctuations, and can be consistently added to
c = list(string.punctuation)

# d is a list of all ASCII whitespace characters
d = list(string.whitespace)

# e is a list of all printable ASCII characters
e = list(string.printable)

# print(e)


def random_sentence():
    user_input = input("Please enter a sentence: ")
    words = user_input.split()

    # Randomly rearrange the words
    random.shuffle(words)

    # Randomly convert words to different cases
    for i in range(len(words)):
        transformation = random.choice(['upper', 'lower', 'title'])
        if transformation == 'upper':
            words[i] = words[i].upper()
        elif transformation == 'lower':
            words[i] = words[i].lower()
        elif transformation == 'title':
            words[i] = words[i].title()

    # Join the words back into a sentence
    new_sentence = ' '.join(words)

    return new_sentence

# print(random_sentence())