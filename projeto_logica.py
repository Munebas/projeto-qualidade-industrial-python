import time #Tempos de pausas
import os # Para limpar o terminal

estoque_geral = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "-"*30)
    print( "MENU DE GESTÃO DE PEÇAS ")
    print("-"*30)
    print("1. Cadastrar nova peça")
    print("2. Consultar estoque")
    print("3. Remover peça cadastrada")
    print("4. Relatório de Produção")
    print("5. Sair do sistema")
    
    opcao_escolha = input("\nO que você deseja fazer?")
    
    # Caso queira cadastrar uma nova peça
    if opcao_escolha == "1":
        #Inserção dos parâmetros da peça
        nome = input("Digite o ID ou nome da peça: ").lower()
        peso = float(input("Digite o peso da peça: "))
        tamanho = float(input("Digite o tamanho da peça: "))

        #lógica de escolha de cor (estilo um toggle, para evitar respostas distintas)
        print("Cores disponíveis: [1] Azul | [2] Verde")
        cor_numero = input("Selecione a cor: ")
        cor = "azul" if cor_numero == "1" else "verde" if cor_numero == "2" else "outro"

    # Identificação da regra de negócio (Se o produto se encaixa ou não)
        if (95 <= peso <= 105) and (10 <= tamanho <= 20) and (cor == "azul" or cor == "verde"):
            status = "Aprovada!"

        else:
            status = "Reprovada! A peça não se enquadra nas regras de negócio da empresa"
            
        peca_atual = {
            "id": nome,
            "peso": peso,
            "tamanho": tamanho,
            "cor": cor,
            "status": status
            }

        estoque_geral.append(peca_atual)

        print(f"Sua peça foi {status}")
        print("Retornando ao menu em instantes...")
        time.sleep(5)

    # Caso queira consultar os itens de estoque
    elif opcao_escolha == "2":
        print("\n--- ITENS NO ESTOQUE ---")
        for peca in estoque_geral:
            print(peca)
        input("\naperte ENTER para voltar para o menu...")

    elif opcao_escolha == "3":
        id_remover = input("Digite o Id/Nome da peça que deseja remover:").lower()
        for peca in estoque_geral:
            if peca["id"] == id_remover:
                estoque_geral.remove(peca)
                print(f"Peça {id_remover} removida com sucesso!")
                input("\naperte ENTER para voltar para o menu...")
                break
    # contar o estoque e buscar quantas aprovadas | Fazer o cálculo de caixas            
    elif opcao_escolha == "4": 
        total = len(estoque_geral)
        aprovadas = 0

        for aprovado in estoque_geral:
            if aprovado["status"] == "Aprovada!":
                aprovadas += 1

        caixas = aprovadas // 10 # cálculo de quantas caixas fechada
        sobras = aprovadas % 10 # porcentagem de sobra para a próxima caixa

        print("\n" + "-"*30)
        print("  Relatório de Produção")
        print("-"*30)
        print(f"Total de Peças: {total}")
        print(f"Peças aprovadas: {aprovadas}")
        print(f"Caixas fechadas: {caixas}")
        print(f"Aguardando nova caixa: {sobras}")
        print("-"*30)
        input("\naperte ENTER para voltar para o menu...")




    # Caso queira sair     
    elif opcao_escolha == "5":
        print("Até logo... Encerrando sistema!")
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        print("Opção inválida! Tente novamente")
    







