# we figured out the rest, but the 3rd word...

# bruh i just guessed "pretty" and it worked
# chatgpt led me down the wrong path with
# this itertools stuff, didn't even generate
# the word "pretty" in the brute forcer

import itertools
import enchant

REMAINING_LETTERS = "BCDGHJKLMOPQRTUVWXYZ"


# Create an English dictionary object
dictionary = enchant.Dict("en_US")
COMBO_LEN = 4

# Generate all possible combinations of the specified length
combos = list(itertools.combinations(REMAINING_LETTERS, COMBO_LEN))

for combo in combos:
    _2, _7, _8, _0 = combo
    fmt = f"{_7}{_8}E{_2}{_2}{_0}"

    # if not a word, skip
    # if not dictionary.check(fmt.lower()):
    #     # print(fmt, "not a word")
    #     continue

    print(fmt)
