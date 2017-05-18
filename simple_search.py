import sys

# take first argument as file name
in_text = open(sys.argv[1], 'r').read().rstrip("\n")
# take second argument as pattern (i.e. a string)
in_pattern = sys.argv[2]

# define global variables
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
    return """positions""", matches

print(simple_search(entry, pitterpatter))
