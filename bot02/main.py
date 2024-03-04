import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install()) # Baixa a ultima versão do webdrivemanager do navegador correspondente

navegador = webdriver.Chrome(service=servico) # Cria uma nova aba com a versão atual
navegador.get('https://google.com.br') # Entra na url

janela_atual = pyautogui.getActiveWindow() # Na janela ativa
janela_atual.maximize() # Maximize ela

navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys("RPA") # Encontra o input e digita rpa
pyautogui.press('enter')
pyautogui.sleep(1)
pyautogui.screenshot('screenshot.png')

navegador.quit()