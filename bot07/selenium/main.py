import pyautogui as p
import pandas as pd
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

caminho_path = os.path.dirname(os.path.abspath(__file__))

options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": caminho_path,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

servico = Service(ChromeDriverManager().install()) # Baixa a ultima versão do webdrivemanager do navegador correspondente

navegador = webdriver.Chrome(service=servico, options=options) # Cria uma nova aba com a versão atual
navegador.get('https://rpachallenge.com') # Entra na url
#navegador.implicitly_wait(30)
janela_atual = p.getActiveWindow() # Na janela ativa
janela_atual.maximize() # Maximize ela

p.sleep(2)
navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a').click()
p.sleep(2)

navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()

dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(dados, columns=['First Name', 'Last Name ', 'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number'])

for linha in df.itertuples():
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').click()
    p.write(linha[1])
    
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').click()
    p.write(linha[2])
    
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').click()
    p.write(linha[3])
    
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').click()
    p.write(linha[4])
    
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').click()
    p.write(linha[5])
    
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').click()
    p.write(linha[6])
    
    navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').click()
    p.write(str(linha[7]))

    navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

p.sleep(2)
p.screenshot("score.png")
navegador.quit()