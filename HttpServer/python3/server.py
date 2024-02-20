import socket

# HTTP Response
HTTP_OK = b"HTTP/1.1 200 OK\r\n\r\n"
HTTP_ERROR = b"HTTP/1.1 404 Not Found\r\n\r\n"

def main():
    print("\n\tPython HTTP Server\n")

    print("[+] Binding port 4221")
    server_socket = socket.create_server(("localhost", 4221), reuse_port=False) # Bind port 4221 to localhost
    print("[+] Port Binded successfully")

    client, addr = server_socket.accept() # wait for client connections
    with client:
        print(f"\n[-] Client {addr} connected.")
        reqData = client.recv(1024).decode("utf-8")

        lines = reqData.split("\r\n")
        begin = lines[0]
        space = " "

        print(f"[!] Received Request {begin}")

        http_method, path, http_ver = begin.split()

        #print(f"{space*4}HTTP Method: {http_method}\n{space*4}HTTP Version: {http_ver}\n{space*4}Path: {path}")

        if path == "/":
            resp = HTTP_OK
        else:
            resp = HTTP_ERROR

        client.sendall(resp)
        client.close()

if __name__ == "__main__":
    main()
