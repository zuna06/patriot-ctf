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

divis = [(x % 3 == 0) for x in counts]
divis_fmt = "".join(["1" if x else "0" for x in divis])
print(divis_fmt)
