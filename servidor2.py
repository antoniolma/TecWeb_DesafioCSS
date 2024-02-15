import socket
from pathlib import Path
from utils import extract_route, read_file, build_response
from views import index


CUR_DIR = Path(__file__).parent
print(CUR_DIR)
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen()

# print(f'Servidor escutando em (ctrl+click): http://{SERVER_HOST}:{SERVER_PORT}')
print(f'Servidor escutando em (ctrl+click): http://localhost:8080')

while True:
    client_connection, client_address = server_socket.accept()

    request = client_connection.recv(1024).decode()
    print('*'*100)
    print(request)

    route = extract_route(request)
    filepath = CUR_DIR / route
    if filepath.is_file():
        print(' +++++++++++ 1')
        response = build_response() + read_file(filepath)
    elif route == '':
        print(' +++++++++++ 2')
        print(len(request.split("\n\n")))
        if request.split()[0] == 'POST' and len(request.split("\n\n")) == 1:
            request += client_connection.recv(1024).decode()

        response = index(request)
        print(response)
    else:
        print(' +++++++++++ 3')
        response = build_response()

    client_connection.sendall(response)
    client_connection.close()

server_socket.close()

# Entra 2 / 2 / 2