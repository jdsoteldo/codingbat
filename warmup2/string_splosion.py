# Given a non-empty string like "Code" return a string like "CCoCodCode".

def word_splosion(str):
    word = ''

    for i in range(len(str)):
        word += str[:i+1]

    return word
