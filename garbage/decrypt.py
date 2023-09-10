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

CIPHERTEXT = open("output.txt", "r").readlines()[0]
LEN_CIPHERTEXT = len(CIPHERTEXT)


def compile(in_data):
    # reverse order
    backwards = list(in_data)
    backwards.reverse()
    print("Entry complete")


def dc1(z):
    # get backwards flag from screwed-up xor ciphertext
    res = ""

    for i, v in enumerate(z):
        res += chr(ord(v) ^ i)

    return bytes(res, "utf-8")


def dc2(t):
    # get output of stage 1 from t
    # they're both strings...

    res = ""
    # need: b"aucG$vs`gdK+\x7fxi`R"

    # for q in range(len(t)):
    #     t += chr(ord(res[q]) - random_seq.pop(0))

    # certified math class moment...
    # i love composition of functions :)
    for q in range(len(t)):
        res += chr(ord(t[q]) + random_seq[q])

    return bytes(res, "utf-8")


def dc3(flag: str):
    print("Final Stage decrypting...")

    # len wtf is the same as len ciphertext
    temp_wtf = list(flag)

    # swap every 2 chars with each other
    wtf = []
    h = 0
    while h < len(temp_wtf):
        try:
            first = bytes(temp_wtf[h], "utf-8")
            second = bytes(temp_wtf[h + 1], "utf-8")
            wtf += second + first
        except:
            wtf += bytes(temp_wtf[h], "utf-8")
        h += 2

    wtf.reverse()
    return bytes(wtf)


def decompile(flag: str):
    return dc1(dc2(dc3(flag)))


def unit_test():
    ciph = b"^Rtf*\x7fbF]dvrD u`]"
    ciph = dc3(ciph.decode("utf-8"))

    assert ciph == b"]u`D vr]dbF*\x7ftf^R", f"got {ciph}"

    ciph = dc2(ciph.decode("utf-8"))
    assert ciph == b"aucG$vs`gdK+\x7fxi`R", f"got {ciph}"

    ciph = dc1(ciph.decode("utf-8"))
    assert ciph == b"ataD sugomA sugoB", f"got {ciph}"


if __name__ == "__main__":
    unit_test()

    print("Length of ciphertext: ", LEN_CIPHERTEXT)

    plaintext = decompile(CIPHERTEXT)
    print(plaintext)
