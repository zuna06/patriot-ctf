import socket
from time import sleep

SLEEP_LEN = 0.1
i = 1

with open("animals.txt", "r") as file:
    for line in file:
        print(i)
        i += 1

        try:
            # Create a socket and connect to the server
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(("chal.pctf.competitivecyber.club", 9999))

            # Send the current line to the server
            client_socket.send(line.encode())

            sleep(SLEEP_LEN)
            # Receive and print the server's response
            response = client_socket.recv(4096)
            print(response.decode())

            # Close the socket
            client_socket.close()

        except Exception as e:
            print(f"Error: {e}")

print("Script completed.")
