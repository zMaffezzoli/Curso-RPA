from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install()) # Baixa a ultima versão do webdrivemanager do navegador correspondente

navegador = webdriver.Chrome(service=servico) # Cria uma nova aba com a versão atual
navegador.get('https://consultacnpj.com/cnpj/') # Entra na url
navegador.maximize_window()
time.sleep(1)
navegador.find_element(By.XPATH, '//*[@id="modal"]/div/div[1]/button').click()

cnpjs = ['30274252000170', '33000167000101', '08902115000507']

for cnpj in cnpjs:
    input = navegador.find_element(By.CSS_SELECTOR, 'input[placeholder="00.000.000/0000-00"]')
    input.clear()
    input.send_keys(cnpj)
    time.sleep(5)
    info = navegador.find_element(By.XPATH, '//*[@id="company-data"]').text
    
    with open(f'{cnpj}.csv', mode='w', encoding='UTF-8') as arquivo:
        arquivo.write(info)

    time.sleep(1)

navegador.quit()