story_raw = open("metamorphis.txt", "r").read()

story = story_raw.split()

# Frequency of a single word
def finder(word):
    count = len([x for x in story if x == word])
    #print "Finding word:",word,"Count:",count
    return count

print "Word: ", "One", "Count: ", finder("One")
   
# Frequency of 2 words
def phrase_finder(phrase):
    phrase = phrase.split()
    pairs = [[story[i], story[i+1]] for i in range(0, len(story) - 1)]
    count = len([x for x in pairs if x == phrase])
    return count

print "Phrase: ", "help produce", "Count: ", phrase_finder('help produce')

def most_freq():
    freq = [ [x,finder(x)] for x in story]
    return reduce(lambda a,b: a if a[1] > b[1] else b, freq)

print most_freq()
