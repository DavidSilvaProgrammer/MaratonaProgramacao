try:
    while True:
        linha = input("Digite algo (Ctrl+D para sair): ")
        print("Você digitou:", linha)
except EOFError:
    print("Fim de arquivo (EOF) detectado. Encerrando o programa.")


***************************


try:
    with open("arquivo.txt", "r") as arquivo:
        while True:
            linha = arquivo.readline()
            if not linha:
                break
            print("Linha lida:", linha)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except IOError:
    print("Erro ao ler o arquivo.")
except EOFError:
    print("Fim de arquivo (EOF) detectado.")
