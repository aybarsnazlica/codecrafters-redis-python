import socket
import threading


def handle_connection(connection):
    try:
        while True:
            data = connection.recv(1024)
            if not data:
                break

            connection.sendall(b"+PONG\r\n")
    except ConnectionError as e:
        print(e)
    finally:
        connection.close()


def main():

    with socket.create_server(("localhost", 6379), reuse_port=True) as server_socket:
        while True:
            connection, _ = server_socket.accept()
            thread = threading.Thread(target=handle_connection, args=(connection,))
            thread.start()


if __name__ == "__main__":
    main()
