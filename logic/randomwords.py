from wonderwords import RandomWord

def getRandomWords():
    r=RandomWord()
    word=r.word(include_parts_of_speech=['nouns','verbs','adjectives'], word_min_length=4)
    return word
