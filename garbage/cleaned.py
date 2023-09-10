from random import seed, randint


def compile(in_data):
    seed(10)

    # reverse order
    backwards = list(in_data)
    backwards.reverse()
    print("Entry complete")

    # stage 1
    char_xor = [chr(ord(v) ^ i) for i, v in enumerate(backwards)]
    z = "".join(x for x in char_xor)

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for y in range(len(z)):
        alphabet[y % 26] = chr((ord(z[y]) ^ ord(char_xor[y])) + 26)
    print("Stage 1 complete")

    # stage 2
    t = "".join([chr(ord(z[q]) - randint(0, 5)) for q in range(len(z))])
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
