from requests import get

def cep_validation(cep):
    cep = cep.replace("-","")
    while len(cep) != 8:
        print("O CEP deve conter 8 dígitos! ")
        cep = str(input("CEP: ")).replace("-","")

    return cep

def cep_consult():
    cep = cep_validation(input("CEP: "))

    link = f'https://viacep.com.br/ws/{cep}/json/'

    response = get(link)

    response_json = response.json()

    for key, value in response_json.items():
        if key == "erro":
            print('CEP inválido!')
        elif value == "":
            print(f'{key} : ------')
        else:
            print(f'{key.upper()} : {response_json[key]}')

cep_consult()