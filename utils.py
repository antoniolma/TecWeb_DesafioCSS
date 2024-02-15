import json

def extract_route(request):
    pos_requests = ["POST", "GET", "PATCH", "DELETE"]
    req_list = request.split(" ")

    for word in req_list:
        if word in pos_requests:
            index = req_list.index(word)
            break

    route = req_list[index+1]

    if route[0] == "/":
        route = route[1:]

    return route

def read_file(path):
    with open(path,'rb') as file:
        return file.read()
    
def load_data(file_name):
    try:
        with open("data/" + file_name,'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f'O arquivo {file_name} não foi encontrado.')
    except json.JSONDecodeError:
        print(f'O arquivo {file_name} não é um JSON válido.')

def load_template(file_name):
    with open('templates/' + file_name,'r') as file:
        return file.read()

def add_input(params):
    # Abrir arquivo
    with open('data/notes.json', 'r') as file:
        data = json.load(file)

    # Adiciona a data coletada
    data.append(params)

    # Sobrescreve
    with open('data/notes.json', 'w') as file:
        json.dump(data, file, indent=2) 

def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        response = f'HTTP/1.1 {code} {reason}\n\n{body}'
    else:
        response = f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'
    return response.encode()