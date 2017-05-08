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
        p_count += 1
        if i == len(pattern)-1 and pattern[i] == text[i]:
            return True
        elif pattern[i] != text[i]:      
            return False
            

def simple_search(text, pattern):
    t_length = len(text) - 1
    p_length = len(pattern) - 1
    positions = []
    t_count = 0
    for n in range(t_length-p_length+1):
        t_count += 1
        if text[n] == pattern[0]:
            if match(text[n:n+p_length+1], pattern) == True:
                positions.append(n+1)
        else:
            pass
    matches = len(positions)
    print('t_counts = ' + str(t_count) + '\np_count = ' + str(p_count))
    return positions, matches

print(simple_search(entry, pitterpatter))

p_count = 0

def make_skip_values(pattern):
    global skip 
    # do not forget backspace ' ', ':', ',', ';', '.'
    alphabet = [' ', ':', ';', ',', '.', '\'', '\"', '!', '?', '(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '\n', '/', '\\', '+', '-', '=', '<', '>', '#', '_', '*', '|', '&','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü']
    for c in alphabet:
        skip[c] = len(pattern)
    for i in range(0, len(pattern)-1):
        skip[pattern[i]] = len(pattern)-i-1

"""
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

def Horsepool(text, pattern):
    make_skip_values(pattern)
    #print(skip)
    t_length = len(text) - 1
    p_length = len(pattern) - 1
    positions = []
    pos = p_length
    t_count = 0
    while (pos < t_length-p_length):
        t_count += 1
        if text[pos] == pattern[p_length]:
            if match(text[pos-(p_length):pos+1], pattern):                
                positions.append(pos-p_length+1)
                pos += skip[text[pos]]
            # forgot this == endless loop            
            else:
                pos += skip[text[pos]]
        else:
            pos += skip[text[pos]]
    matches = len(positions)
    print('t_counts = ' + str(t_count) + '\np_count = ' + str(p_count))
    return positions, matches


print(Horsepool(entry, pitterpatter))
