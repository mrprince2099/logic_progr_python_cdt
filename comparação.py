###Criando uma lista
##Ivan, Rafael, Gustavo, Tarso, Vitor, Gabriel

#Qual seria o print e
#input para pedir os nomes

print("***Lista de Nomes ***\n")

nomes = input("Digite os nomes separados por vírgula; ").split(", ")

#print(nomes)

print("\nQuais operações você quer fazer:")
print("1 - Adicionar um nome")
print("2 - Remover um nome")
print("3 - Alistar nomes")
print("4 - Sair")

#faça um loop para pedir a opção do usuário

while True:
    opcao = input("\nDigite a opção desejada (1-4): ")

    if opcao == "1":
        #novo_nome = input("Digite o nome a ser adicionado:")
        #nome.append(novo_nome)
        #print(f"{novo_nome} foi adicionado a lista. ")
        print(f" foi adicionado a lista.")

    elif opcao == "2":
        #nome_remover = input("Digite o nome a ser removido: ")
        #if nome_remover in nomes:
        #    nomes.remove(nome_remover)
        #    print(f"{nome_remover} foi removido da lista. ")
        #else:
            #print(f"{nome_remover} não está na lista. ")
        print(f"n~so está na lista. ")

    elif opcao == "3":
        print    