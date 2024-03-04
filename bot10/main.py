from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install()) # Baixa a ultima versão do webdrivemanager do navegador correspondente

navegador = webdriver.Chrome(service=servico) # Cria uma nova aba com a versão atual
navegador.get('https://ferendum.com/pt') # Entra na url
navegador.maximize_window()
time.sleep(1)
navegador.find_element(By.XPATH, '/html/body/spamtrap/main/div[1]/div/form/div[1]/input').send_keys("A automação é uma coisa boa?")
navegador.find_element(By.XPATH, '/html/body/spamtrap/main/div[1]/div/form/div[2]/textarea').send_keys("Os robôs estão cada vez mais frequentes em nossas vidas...")
navegador.find_element(By.XPATH, '//*[@id="op1"]').send_keys("Sim! Ela me ajuda muito...")
navegador.find_element(By.XPATH, '//*[@id="op2"]').send_keys("Não! Estou com medo de perder meu emprego...")
navegador.find_element(By.XPATH, '/html/body/spamtrap/main/div[1]/div/form/table/tbody/tr/td/input[2]').click()
navegador.find_element(By.XPATH, '/html/body/spamtrap/main/div[1]/div/form/table/tbody/tr/td/input[4]').click()
navegador.find_element(By.XPATH, '/html/body/spamtrap/main/div[1]/div/form/table/tbody/tr/td/input[5]').click()
navegador.find_element(By.XPATH, '/html/body/spamtrap/main/div[1]/div/form/div[7]/input').click()
time.sleep(1)

navegador.find_element(By.XPATH, '/html/body/spamtrap/main/div[1]/div/form/input[5]').click()
time.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="crear_votacion"]').click()
time.sleep(5)

link = navegador.find_element(By.XPATH, '//*[@id="textoACopiar"]').text
print(link)

navegador.quit()