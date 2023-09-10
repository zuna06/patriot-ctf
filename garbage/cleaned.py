# fmt: off
random_seq = [
    4, 0, 3, 3, 4, 0, 1, 3, 3, 2, 5, 1, 0, 4, 3, 2, 0, 1, 5, 2,
    0, 3, 1, 4, 2, 3, 3, 2, 5, 2, 3, 1, 5, 2, 5, 2, 1, 3, 1, 3,
    4, 3, 0, 4, 0, 1, 1, 1, 2, 4, 2, 1, 2, 5, 4, 3, 3, 3, 0, 5,
    4, 2, 4, 1, 1, 3, 1, 0, 0, 3, 2, 4, 5, 0, 4, 0, 1, 3, 4, 2,
    4, 1, 0, 0, 3, 1, 1, 2, 3, 3, 3, 1, 5, 2, 1, 4, 4, 1, 0, 2,
    3, 2, 1, 5, 5, 1, 1, 3, 2, 2, 3, 1, 0, 4, 5, 0, 2, 2, 1, 0,
    2, 3, 3, 4, 1, 3, 3, 5, 1, 5, 4, 2, 4, 3, 4, 3, 0, 1, 3, 5,
    3, 3, 1, 3, 4, 4, 2, 4, 3, 3, 5, 1, 4, 3, 0, 3, 0, 0, 3, 4,
    0, 0, 2, 0, 1, 0, 4, 3, 3, 1, 3, 3, 4, 3, 2, 5, 2, 5, 3, 3,
    2, 5, 4, 4, 1, 5, 1, 2, 4, 0, 5, 1, 5, 4, 4, 5, 3, 0, 0, 2,
    3, 1, 5, 2, 0, 0, 4, 4, 0, 2, 1, 5, 3, 1, 2, 4, 3, 1, 2, 1,
    0, 4, 1, 3, 1, 0, 5, 2, 3, 5, 5, 4, 5, 3, 3, 5, 5, 4, 1, 2,
    4, 2, 0, 5, 5, 0, 1, 3, 4, 3, 3, 5, 1, 0, 3, 0, 0, 2, 2, 2,
    3, 3, 1, 5, 5, 2, 3, 5, 2, 4, 3, 4, 2, 3, 3, 5, 2, 2, 5, 2,
    3, 3, 3, 4, 3, 0, 5, 4, 5, 2, 5, 3, 1, 4, 3, 5, 4, 0, 4, 5,
    2, 0, 4, 2, 5, 2, 0, 5, 3, 4, 2, 2, 4, 1, 1, 1, 2, 0, 4, 0,
    1, 4, 5, 0, 3, 1, 4, 4, 3, 4, 0, 3, 1, 2, 4, 1, 4, 4, 2, 0,
    5, 5, 4, 0, 0, 4, 2, 3, 2, 4, 5, 1, 1, 0, 4, 2, 1, 0, 5, 4,
    4, 2, 0, 3, 3, 4, 2, 0, 1, 3, 5, 3, 4, 3, 5, 3, 4, 1, 2, 3,
    2, 4, 4, 3, 3, 1, 0, 3, 5, 1, 0, 1, 5, 5, 1, 4, 3, 2, 4, 3,
    0, 4, 0, 1, 2, 1, 0, 4, 1, 0, 5, 4, 2, 1, 2, 0, 3, 4, 3, 0,
    2, 1, 3, 1, 1, 3, 3, 2, 0, 1, 1, 4, 5, 3, 1, 4, 5, 5, 3, 0,
    3, 0, 1, 0, 3, 5, 5, 2, 5, 2, 4, 5, 0, 2, 4, 4, 3, 4, 1, 4,
    2, 0, 5, 1, 5, 3, 5, 1, 0, 4, 5, 3, 0, 4, 3, 4, 1, 2, 2, 0,
    1, 4, 4, 4, 0, 0, 3, 0, 0, 5, 3, 2, 1, 5, 0, 2, 2, 5, 3, 1,
]
# fmt: on


def compile(in_data):
    # reverse order
    backwards = list(in_data)
    backwards.reverse()
    # backwards as bytes
    joined = "".join(x for x in backwards)
    print(f"Entry complete: {bytes(joined, 'utf-8')}")

    # stage 1
    char_xor = [chr(ord(v) ^ i) for i, v in enumerate(backwards)]
    z = "".join(x for x in char_xor)
    print(f"Stage 1 complete: {bytes(z, 'utf-8')}")

    # stage 2
    t = "".join([chr(ord(z[q]) - random_seq.pop(0)) for q in range(len(z))])
    print(f"Stage 2 complete: {bytes(t, 'utf-8')}")

    # stage 3
    wtf = list(t)
    wtf.reverse()
    wtf = "".join(g for g in wtf)
    flag = ""

    h = 0
    while h < len(wtf):
        try:
            flag += wtf[h + 1] + wtf[h]
        except:
            flag += wtf[h]
        h += 2

    print(f"Final Stage complete: {bytes(flag, 'utf-8')}")
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

        rand_calls = 500 - len(random_seq)
        print(f"Calls to RNG: {rand_calls}")
