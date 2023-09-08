from string import punctuation

alphabet = list(punctuation)
data = "bHEC_T]PLKJ{MW{AdW]Y"
keys = alphabet
def main():
    for key in keys:
        decrypted = ''.join([chr(ord(x) ^ ord(key)) for x in data])
        print(decrypted)

main()