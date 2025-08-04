print("💥 Minha Lista de Desejos para o Futuro💥\n")
#Define o nome do arquivo onde os desejos serão salvos.
NOME_ARQUIVO = "meus_desejos.txt"
desejos = [] # Lista vazia para guardar os desejos

# --- Carregar desejos existentes (se houver) ---
try:
    # 'r' significa modo de leitura (read) .
    # 'with open(...) as f:' garante que o arquivo seja fechado
    # automaticamente, mesmo se ocorrer um erro.
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for desejo in lista_de_desejos:
            arquivo.write(desejo + "\n") # Escreve cada desejo seguido de uma nova linha.
            print("\n✅ Seus desejos foram salvos com sucesso!")
        except Exception as e:
print(f"\n❌ Erro ao salvar os desejos: {e}")

# --- Loop Principal do Programa ---
while True:
    print("\n--- O que você quer fazer? ---")
    print("1 - Adicionar um novo desejo")
    print("2 - Ver meus desejos")
    print("3 - Sair")

    opcao = input("Digite sua opção (1, 2 ou 3): ")

    if opcao == "1":
        novo_desejo = input("Qual é o seu novo desejo para o futuro? ")
        if novo_desejo.strip(): # Garante que o desejo não seja vazio
            desejos.append(novo_desejo.strip())
            salvar_desejos(desejos) # Salva a lista toda vez que um desejo é adicionado
        else:
            print("Desejo nãõ pode ser vazio! Tente novamente.")
        elif opcao == "2":
print("\n")