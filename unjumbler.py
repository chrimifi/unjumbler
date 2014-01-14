__author__ = 'Chris Fincher'


def unjumble(jumble, listfile):
    candidates = set()
    openfile = open(listfile, 'r')
    wlist = openfile.readlines()
    openfile.close()
    for seq in permutations(jumble):
        if seq + '\n' in wlist:
            candidates.add(seq)
    return candidates


# Return each combination of letters that can be formed from letters (a string)
# Returns a set of strings
# Using a set ensures uniqueness
def permutations(letters):
    perms = set()
    for i in range(len(letters)):
        # The letter by itself is a perfectly good sequence
        perms.add(letters[i])
        # Put the letter in front of every anagram of the remaining letters
        for tail in permutations(letters[:i] + letters[i + 1:]):
            perms.add(letters[i] + tail)
    return perms


if __name__ == '__main__':
    # TODO Handle parameters
    print(unjumble('dog', 'sample_dict'))
