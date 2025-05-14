import socket

# Define the server address and port
SERVER_HOST = "127.0.0.1"  # Change to server IP if connecting remotely
SERVER_PORT = 7777         # Must match server's port

def main():
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((SERVER_HOST, SERVER_PORT))
            print("Connected to the Guessing Game Server!")
            print("Guess a number between 1 and 100. Type 'exit' to quit.\n")
            
            while True:
                guess = input("Enter your guess: ").strip()
                if guess.lower() == 'exit':
                    print("Exiting the game.")
                    break

                sock.sendall(guess.encode())  # Send the guess to the server

                response = sock.recv(1024).decode()  # Receive the server's response
                if not response:
                    print("Server closed the connection.")
                    break

                print("Server:", response)

        except ConnectionRefusedError:
            print("Unable to connect to the server. Is it running?")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()

