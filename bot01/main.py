import pyautogui as auto

auto.hotkey('win', 'r') # Executa duas teclas simultâneas

auto.sleep(2)
auto.typewrite('notepad') # Escreve notepad
auto.sleep(2)
auto.press('enter') # Pressiona enter
auto.sleep(2)
auto.typewrite("Hello, I'm a bot")
auto.sleep(2)

janela = auto.getActiveWindow() # Captura a informação da janela atual
auto.sleep(2)
janela.close() # Tenta fechar a janela 

# Windows 11 não precisa!
"""auto.sleep(2)
auto.press('right') # Seta p/ direita
auto.sleep(2)
auto.press('enter') # Pressiona enter p/ não salvar o arquivo"""
