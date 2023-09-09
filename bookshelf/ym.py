import socket
from time import sleep

URL = "chal.pctf.competitivecyber.club"
PORT = 4444
SLEEP_LEN = 0.5

with open("steps.txt", "r") as file:
    fc = file.read().split("\n")

    # filter out comment lines
    fc = filter(lambda x: len(x) != 0 and x[0] != "#", fc)

    fc = "\n".join(fc)
    INIT_PROMPT = fc.replace("+", "\n")

print(INIT_PROMPT)


def connect():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((URL, PORT))

    return client_socket


try:
    conn = connect()

    # Send the current line to the server
    conn.send(INIT_PROMPT.encode())
    sleep(SLEEP_LEN)

    # get the second line
    full_response = conn.recv(16384)

    print(full_response.decode())

    # Close the socket
    conn.close()
except Exception as e:
    print(f"Error: {e}")
