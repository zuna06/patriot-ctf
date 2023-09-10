def count_seq(input_str):
    res = []
    count = 1

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            res.append(count)
            count = 1

    res.append(count)
    return res


with open("Binary.txt", "r") as f:
    bintxt = f.read()

counts = count_seq(bintxt)

# check divisibility by 3 (kinda a reach)
divis = [(x % 3 == 0) for x in counts]
divis_fmt = "".join(["1" if x else "0" for x in divis])
# print(divis_fmt)

# the thing CJ suggested
binl = [bin(x)[2:] if x > 1 else str(x) for x in counts]
binl_fmt = "".join(str(x) for x in binl)
# print(binl_fmt)
