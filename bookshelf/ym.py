import socket
from time import sleep

# try "Giraffe"

SLEEP_LEN = 0.1

with open("animals.txt", "r") as file:
    for line in file:
        try:
            # Create a socket and connect to the server
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(("chal.pctf.competitivecyber.club", 9999))

            # Send the current line to the server
            client_socket.send(line.lower().encode())

            sleep(SLEEP_LEN)

            # get the second line
            full_response = client_socket.recv(4096)
            response = full_response.decode().split("\n")[1]

            sus = "ERRR! Wrong!" not in response
            sus_fmt = "SUS!" if sus else "fail:"

            print(f"{sus_fmt} {line}")
            if sus:
                print(f"Full Response: {full_response}")

            # Close the socket
            client_socket.close()

        except Exception as e:
            print(f"Error: {e}")

print("Script completed.")
