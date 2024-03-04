from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install()) # Baixa a ultima versão do webdrivemanager do navegador correspondente

navegador = webdriver.Chrome(service=servico) # Cria uma nova aba com a versão atual
navegador.get('https://www.situacao-cadastral.com/') # Entra na url
navegador.maximize_window()
time.sleep(1)
navegador.find_element(By.XPATH, '//*[@id="doc"]').send_keys("03.774.688/0001-55")
navegador.find_element(By.XPATH, '//*[@id="consultar"]').click()
time.sleep(10)
navegador.quit()