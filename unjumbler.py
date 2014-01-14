__author__ = 'Chris Fincher'


def unjumble(jumble, wlist):
    candidates = permutations(jumble)
    for seq in candidates:
        if is_in_list(seq, wlist):
            candidates.remove(seq)
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


def is_in_list(word, wlist):
    True

if __name__ == '__main__':
    # TODO Handle parameters
    print(unjumble('dog', 'sample_dict'))
