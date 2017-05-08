import sys

# in_text = 'Hallelujah' * 3
# in_pattern = 'alle'
# take first argument as file name
in_text = open(sys.argv[1], 'r').read().rstrip("\n")
# take second argument as pattern (i.e. a string)
in_pattern = sys.argv[2]

# define global variables to be reused in different functions
p_count = 0
skip = {}

entry = in_text.lower()
pitterpatter = in_pattern.lower()

# compare slice of text with pattern
def match(text, pattern):
    # apply changes in p_count globally
    global p_count  
    # use every symbol in pattern
    for i in range(len(pattern)):
        # count numbers of pattern, text comparisons
        p_count += 1
        # found a match after passing through pattern without mismatch
        if i == len(pattern)-1 and pattern[i] == text[i]:
            return True
        # if text and pattern do not match in a position, stop comparing
        elif pattern[i] != text[i]:      
            return False
            break
            

# pass through text sequentially by position and check for match of the first symbol of the pattern with the text
def simple_search(text, pattern):
    # adjust length of text and pattern by 1 to turn length (starting at 1) into index (starting at 0)
    t_length = len(text) - 1
    p_length = len(pattern) - 1
    # initialize list to hold the positions of matches and a variable to remember number of tested positions
    positions = []
    t_count = 0
    # check over the length of the text until the remainder is to short to hold the pattern
    for n in range(t_length-p_length+1):
        # for each comparison increase comparison counter
        t_count += 1
        # if start of the pattern matches position in text...
        if text[n] == pattern[0]:
            # call match function with a slice of text of length(pattern) and compare with pattern
            if match(text[n:n+p_length+1], pattern) == True:
                # remember position of a successful match
                positions.append(n+1)
        else:
            pass
    # count successful matches by the number of their positions
    matches = len(positions)
    print('t_counts = ' + str(t_count) + '\np_count = ' + str(p_count))
    return positions, matches

print(simple_search(entry, pitterpatter))

p_count = 0

# create skip values dictionary for Horspool algorithm on string pattern
def make_skip_values(pattern):
    # make sure skip dictionary is available globally
    global skip 
    # do not forget backspace ' ', ':', ',', ';', '.' etc.
    alphabet = [' ', ':', ';', ',', '.', '\'', '\"', '!', '?', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n', '/', '\\', '+', '-', '=', '<', '>', '#', '_', '*', '|', '&','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü']
    # for each symbol in the alphabet enter a standard skip value of the length of the pattern
    for c in alphabet:
        skip[c] = len(pattern)
    # go through the pattern and enter a skip value for each symbol according to its position relativ to the end of the pattern, ...3-2-1-end
    for i in range(len(pattern)-1):
        skip[pattern[i]] = len(pattern)-i-1

"""
# variation of Horspool without calling match
def Horsepool(text, pattern):
    make_skip_values(pattern)
    print(skip)
    t_length = len(text) - 1
    p_length = len(pattern) - 1
    positions = []
    pos = p_length
    t_count = 0
    while (pos < t_length-p_length):
        if text[pos] == pattern[p_length]:
            if text[pos-(p_length):pos+1] == pattern:                
                positions.append(pos-p_length+1)
                pos += skip[text[pos]]
                print(pos)
        else:
            pos += skip[text[pos]]
            print(pos)
    matches = len(positions)
    print('t_counts = ' + str(t_count) + '\np_count = ' + str(p_count))
    return positions, matches
"""

# compare the last symbol of the pattern to the approppriate position in the text, if it is not a match, skip to a position determined by the symbol found in the text
def Horspool(text, pattern):
    # create a dictionary of skip values according to the pattern
    make_skip_values(pattern)
    #print(skip) for bugfixing purposes
    # adjust length of text and pattern by 1 to turn length (starting at 1) into index (starting at 0)
    t_length = len(text) - 1
    p_length = len(pattern) - 1
    positions = []
    # set first position in text to the end of the pattern
    pos = p_length
    t_count = 0
    # repeat until the position has gone over the length of the text that can hold the pattern
    while (pos < t_length-p_length):
        # count the comparisons of text and pattern
        t_count += 1
        # if symbol in the text matches symbol in the pattern...
        if text[pos] == pattern[p_length]:
            # call match function with a slice of text of length pattern ending at pos and compare with pattern
            if match(text[pos-(p_length):pos+1], pattern):   
                # remember position of successful match             
                positions.append(pos-p_length+1)
                # adjust position
                pos += skip[text[pos]]
            # adjust position after determining a mismatch inside a call to match, forgot this == endless loop            
            else:
                pos += skip[text[pos]]
        # if not, adjust position according to the symbol found at this position in the text
        else:
            pos += skip[text[pos]]
    # determine number of matches by counting positions of successful matches
    matches = len(positions)
    print('t_counts = ' + str(t_count) + '\np_count = ' + str(p_count))
    return positions, matches


print(Horspool(entry, pitterpatter))
