import pyautogui

pyautogui.moveTo(32, 235) # Move para o icone do chrome
pyautogui.doubleClick() # Abre o chrome
pyautogui.sleep(1)
pyautogui.write("www.udemy.com.br") # Escreve a url
pyautogui.press('enter') # Entra no site

janela_atual = pyautogui.getActiveWindow()
janela_atual.maximize() # Maximiza a tela

pyautogui.sleep(15) # Internet ruim, demora muito para abrir
localPesquisa = pyautogui.locateOnScreen('pesquisa.png', confidence=0.9) # Localiza o print da imagem no site
centerLocalPesquisa = pyautogui.center(localPesquisa) # Pega o centro das dimensões acima
xLocal, yLocal = centerLocalPesquisa # Descompacta para cada variável

pyautogui.moveTo(xLocal, yLocal) # Move para o meio do campo de pesquisa
pyautogui.click() # Clica no campo de pesquisa
pyautogui.write("RPA Python")
pyautogui.press('enter')

pyautogui.sleep(3)
pyautogui.screenshot('Cursos.png')

pyautogui.sleep(3)
localFechar = pyautogui.locateOnScreen('fechar.png', confidence=0.9) # Localiza o print da imagem no PC
centerLocalFechar = pyautogui.center(localFechar) # Pega o centro das dimensões acima
xLocal, yLocal = centerLocalFechar # Descompacta para cada variável

pyautogui.moveTo(xLocal, yLocal) # Move para o meio do campo de pesquisa
pyautogui.click() # Fecha a aba