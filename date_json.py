# import json

# json_string = """[
# {
# "nome_carro":"toyota supra mk4",
# "fabricante":"toyota",
# "ano":"1993/2002",
# "estilo_carro":"esportivo",
# "preço":["400,000"]
# },
# {
# "nome_carro":"nissan skyline gt-r",
# "fabricante":"nissan",
# "ano":"1989/1994",
# "estilo_carro":"esportivo",
# "preço":["350,000"]
# },
# {
# "nome_carro":"mazda mx-5 miata",
# "fabricante":"mazda",
# "ano":"1989/1997",
# "estilo_carro":"esportivo",
# "preço":["300,000"]
# }






# """


import json

dados = {'nome': 'João', 'idade': 30,
         'cidade': 'Sao Paulo', 'servico': 'Premium'}
json_string = json.dumps(dados)
# Imprimindo o dicionário inteiro como uma string JSON

print(json_string)
# Imprimindo o dicionário inteiro

print(dados)











import json

frutas = {
    'frutas': [
        {
            "fruta1": "maçã",
            "preco": 2.34,
        },
        {
            "fruta2": "pera",
            "preco": 3.45,
        },
        {
            "fruta3": "banana",
            "preco": 1.23,
        },
        {
            "fruta4": "laranja",
            "preco": 4.56,
        }
    ]
}

##Escrever JSON
with open('frutas.json', 'w', encoding='utf-8') as arquivo:
    json.dump(frutas, arquivo, indent=8, ensure_ascii=False)

    ## Salvamento com identação usando ASCII encoding