import pyautogui
import smtplib

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

servico = Service(ChromeDriverManager().install()) # Baixa a ultima versão do webdrivemanager do navegador correspondente

navegador = webdriver.Chrome(service=servico) # Cria uma nova aba com a versão atual
navegador.get('https://www.melhorcambio.com/dolar-hoje') # Entra na url

janela_atual = pyautogui.getActiveWindow() # Na janela ativa
janela_atual.maximize() # Maximize ela
pyautogui.sleep(2)
cotacao_dolar = navegador.find_element(By.ID, 'comercial').get_attribute("value") # Encontra o elemento na página e extraí seu valor

#texto do email
texto_email = f"Cotação dólar R${cotacao_dolar}. Dia: {datetime.today().strftime('%d/%m/%Y')}"

# email remetente, senha, destinatário
de = "rpabot88@gmail.com"
senha = "********"
para = "rpabot88@gmail.com"

# Setup the MIME
message = MIMEMultipart()
message['From'] = de
message['To'] = para
#message['To'] = para02
message['Subject'] = 'Cotação do dolar'   #Título do e-mail

# Corpo do E-mail com anexos
message.attach(MIMEText(texto_email, 'plain'))

# Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  # Usuário do Gmail com porta
session.starttls()  # Habilita a segurança
session.login(de, senha)  # Login e senha de quem envia o e-mail
texto = message.as_string()
session.sendmail(de, para, texto)
session.quit()
navegador.quit()