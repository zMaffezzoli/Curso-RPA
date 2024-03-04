import pyautogui
import pandas
from io import StringIO

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install()) # Baixa a ultima versão do webdrivemanager do navegador correspondente

navegador = webdriver.Chrome(service=servico) # Cria uma nova aba com a versão atual
navegador.get('https://rpachallengeocr.azurewebsites.net/') # Entra na url

janela_atual = pyautogui.getActiveWindow() # Na janela ativa
janela_atual.maximize() # Maximize ela
pyautogui.sleep(5)

page = 1

while page <= 3:
    
    table = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]').get_attribute('outerHTML')
    df  = pandas.read_html(StringIO(table))
    df[0]["Invoice"] = df[0]["Invoice"].fillna("NaN") # Adicionar os valores NaN
    
    if page == 1:
        df[0].to_csv(r'Tabela.csv', mode='a', index=False, header=True)
    
    else:
        df[0].to_csv(r'Tabela.csv', mode='a', index=False, header=False)

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    page += 1

navegador.close()