story_raw = open("metamorphis.txt", "r").read()

story_list = story_raw.split()

story = [x.strip('";./()-_?,').lower() for x in story_list]

# Frequency of a single word
def finder(word):
    word = word.lower()
    count = [1 for x in story if x == word]
    return reduce((lambda a,b: a + b), count)

print "Word: ", "One", "Count: ", finder("One") # 59
   
# Frequency of 2 words
def phrase_finder(phrase):
    phrase = phrase.lower()
    phrase = phrase.split()
    pairs = [[story[i], story[i+1]] for i in range(0, len(story) - 1)]
    count = [1 for x in pairs if x == phrase]
    return reduce((lambda a, b: a + b), count)

print "Phrase: ", "but gregor", "Count: ", phrase_finder('but gregor') # 5

def group_finder(group):
    return reduce((lambda a, b: a + b), [finder(x) for x in group])

print "Group: ['but', 'gregor']", "Total Count: ", group_finder(['but', 'gregor']) # 372

def most_freq():
    freq = [ [x,finder(x)] for x in story]
    return reduce(lambda a,b: a if a[1] > b[1] else b, freq)

print "[Most frequently appearing word, frequency]",most_freq() # the - 1330
