import socket

def handle_data(data,conn):
    data_str = data.decode()
    data_line = data_str.split("\r\n")
    path=data_line[0].split(" ")[1]
    if path=="/":
        conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    else:
        conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, addr = server_socket.accept()
    data = conn.recv(1024)
    handle_data(data,conn)
    #response = "HTTP/1.1 200 OK\r\n\r\n".encode()
    #conn.send(response)

if __name__ == "__main__":
    main()
