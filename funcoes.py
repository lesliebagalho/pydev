import pyautogui
import time
import os

def limparTela():
    os.system("cls" if os.name == "nt" else "clear")

def repetidor():
    pyautogui.press("winleft")
    pyautogui.write(navegador)
    pyautogui.press("enter")
    return

def opcaoMenuNavegador():
    global navegador
    while True:
        print("Escolha o navegador ou digite um de sua preferência...")
        print("***************************************")
        print("[1] Chrome")
        print("[2] Outro")
        print("[0] Sair")
        opcaoNavegador = int(input("Qual navegador deseja usar? "))
        if opcaoNavegador == 1:
            navegador = "Chrome"
            opcaoMenuPesquisa()
            break
        elif opcaoNavegador == 2:
            navegador = input(
'''
Atenção!
Tenha certeza de que seu navegador preferencial está instalado...
Digite o seu navegador preferencial.
''')
            print()
            opcaoMenuPesquisa()
            break
        elif opcaoNavegador == 0:
            print("Saindo do menu de opçõs do navegador...")
            limparTela()
            opcaoMenuGeral()
            break

def abrirVsCode():
    print("Você escolheu a opção abrir o VS Code")
    pyautogui.press('winleft')
    pyautogui.write("vscode")
    pyautogui.press("enter")

def entrarNoGithub():
    print("Você escolheu a opção entrar no GitHub")
    gitHub = input("Entre com o seu usuário: ")
    repetidor()
    time.sleep(3) #Tempo para o navegador abrir
    pyautogui.write(f"https://github.com/{gitHub}")
    pyautogui.press("enter")

def opcaoMenuGeral():
    print("\n***************************************")
    print("\nSeja bem vindo ao Assitente PyDev!")
    print("\n***************************************")
    while True:
        print("\n***************************************")
        print("O que você deseja fazer?")
        print("\n[1] Abrir VS Code")
        print("[2] Pesquisar")
        print("[0] Sair")
        print("***************************************")
        
        try:
            opcao = int(input("\nEscolha a opção: "))
            pyautogui.PAUSE=2
            
            if opcao == 1:
                abrirVsCode()
                limparTela()
            elif opcao == 2:
                opcaoMenuNavegador()
            
            elif opcao == 0:
                print("\nSaindo do Assitente PyDev...")
                limparTela()
                break
            else:
                print("\nErro: Opção escolhida não encontrada. Escolha novamente!")
        except ValueError:
            print("\nErro: Opção escolhida não encontrada. Escolha novamente!")
            continue

def opcaoMenuPesquisa():
    print("\n***************************************")
    print("O que você desja fazer? ")
    print("[1] Pesquisar no YouTube")
    print("[2] Pesquisar no Google")
    print("[3] Pesquisar no ChatGPT")
    print("[4] Entrar no GitHub")
    print("[0] Sair")
    print("***************************************")
    
    while True:
        opcao = int(input("\nEscolha a opção: "))
        pyautogui.PAUSE=2
        
        if opcao == 1:
            print("Você escolheu a opção para pesquisar no YouTube")
            repetidor()
            pyautogui.write("https://youtube.com")
            pyautogui.press("enter")
        
        elif opcao == 2:
            print("Você escolheu a opção para pesquisar no Google")
            repetidor()
            pyautogui.write("https://google.com")
            pyautogui.press("enter")
            
        elif opcao == 3:
            print("Você escolheu a opção para pesquisar no ChatGPT")
            repetidor()
            pyautogui.write("https://chat.openai.com")
            pyautogui.press("enter")
        
        elif opcao == 4:
            entrarNoGithub()

        elif opcao == 0:
            limparTela()
            print("Saindo do menu de opções de pesquisa...")
            break
        
        else:
            limparTela()
            print("\nErro: Opção escolhida não encontrada. Escolha novamente!")
            
if __name__ == "__main__":
    limparTela()
    print("Mensangem ou menu atualizado")
    # opcaoMenuGeral()