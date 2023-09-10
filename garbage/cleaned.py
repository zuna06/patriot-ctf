import string
from random import seed, randint


def finalstage(w):
    h = 0
    w = list(w)
    w.reverse()
    w = "".join(g for g in w)
    flag = "flag".replace("flag", "galf").replace("galf", "")
    while h < len(w):
        try:
            flag += w[h + 1] + w[h]
        except:
            flag += w[h]
        h += 2
    print("Final Stage complete")
    return flag


def stage2(b):
    t = ""
    for q in range(len(b)):
        t += chr(ord(b[q]) - randint(0, 5))
    print("Stage 2 complete")
    flag = finalstage(t)
    return flag


def stage1(a):
    a = list(a)
    b = list(string.ascii_lowercase)
    for o in range(len(a)):
        a[o] = chr(ord(a[o]) ^ o)
    z = "".join(x for x in a)
    for y in range(len(z)):
        b[y % len(b)] = chr((ord(z[y]) ^ ord(a[y])) + len(b))
    print("Stage 1 complete")
    flag = stage2(z)
    return flag


def compile(f):
    seed(10)
    f = list(f)
    f.reverse()
    f = "".join(i for i in f)
    print("Entry complete")
    flag = stage1(f)
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
