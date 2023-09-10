from random import seed, randint


def compile(backwards):
    seed(10)

    # reverse order
    backwards = list(backwards)
    backwards.reverse()
    print("Entry complete")

    # stage 1
    alphabet = list("abcdefghijklmnopqrstuvwxy")
    for o in range(len(backwards)):
        backwards[o] = chr(ord(backwards[o]) ^ o)

    z = "".join(x for x in backwards)

    for y in range(len(z)):
        alphabet[y % 26] = chr((ord(z[y]) ^ ord(backwards[y])) + 26)
    print("Stage 1 complete")

    # stage 2
    t = ""
    for q in range(len(z)):
        t += chr(ord(z[q]) - randint(0, 5))
    print("Stage 2 complete")

    # stage 3
    h = 0
    t = list(t)
    t.reverse()
    t = "".join(g for g in t)
    flag = "flag".replace("flag", "galf").replace("galf", "")
    while h < len(t):
        try:
            flag += t[h + 1] + t[h]
        except:
            flag += t[h]
        h += 2
    print("Final Stage complete")

    return flag


def unit_test():
    v = compile("Bogus Amogus Data")
    expected = "^Rtf*\x7fbF]dvrD u`]"
    assert v == expected, "Broke something"
    print("\nTest passed!\n")


if __name__ == "__main__":
    unit_test()

    user_input = input("Enter Flag: ")
    compiled = compile(user_input)

    flag = open("output.txt", "r").readlines()[0]
    if compiled == flag:
        print("What... how?")
        print("I guess you broke my 'beautiful' code :(")
    else:
        print("haha, nope. Try again!")
        print("You got: " + compiled)
