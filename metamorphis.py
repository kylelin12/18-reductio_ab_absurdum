story_raw = open("metamorphis.txt", "r").read()

story = story_raw.split()

# Frequency of a single word
def finder(word):
    count = len([x for x in story if x == word])
    print "Finding word:",word,"Count:",count

finder("One")

# Frequency of 2 words
def phrase_finder(phrase):
    phrase = phrase.split()
    pairs = [[story[i], story[i+1]] for i in range(0, len(story) - 1)]
    count = len([x for x in pairs if x == phrase])
    print "Finding:",phrase,"Found:",count
    return count

phrase_finder('help produce')