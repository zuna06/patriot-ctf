def simplify_string(input_str):
    simplified_str = ""
    count = 1

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1
        else:
            simplified_str += str(count) + " "
            count = 1

    simplified_str += str(count)
    return simplified_str


with open("Binary.txt", "r") as f:
    input_str = f.read()

simplified_result = simplify_string(input_str)
print(simplified_result)
