# 15. Given a string as your input, delete any reoccurring character, and return the new string.
def def_rep_char(string):
    seenChars = set()
    uniqueChars = ''
    for char in string:
        if char not in seenChars:
            seenChars.add(char)
            uniqueChars += char
    return uniqueChars

uniqueCharss = def_rep_char("mississipi")
print(uniqueCharss)