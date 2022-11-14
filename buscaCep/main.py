import requests

perguntaCep = input('Digite o cep que deseja buscar: ')
if len(perguntaCep) != 8:
    print("Quantidade de digitos Inválido!")
    exit()

buscaCep = requests.get(f'https://viacep.com.br/ws/{perguntaCep}/json')

informaCep = buscaCep.json()

if "erro" not in informaCep:
    print(buscaCep.json())
    print()
    print("Cep: {}".format(informaCep['cep']))
else:
    print("Cep Inválido!")