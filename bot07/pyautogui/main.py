import pyautogui as p
import pandas as pd
import os

caminho_path = os.path.dirname(os.path.abspath(__file__))

p.hotkey('win', 'r')
p.typewrite('chrome')
p.sleep(2)
p.press('enter')

janela = p.getActiveWindow()
janela.maximize()

p.sleep(2)
p.typewrite('https://rpachallenge.com')
p.press('enter')
p.sleep(2)

localBaixar = p.locateOnScreen('./images/download.png', confidence=0.9) # Localiza o print da imagem no PC
centerLocalBaixar = p.center(localBaixar)
p.rightClick(centerLocalBaixar[0], centerLocalBaixar[1])

p.press('down')
p.press('down')
p.press('down')
p.press('down')
p.press('enter')

p.write(f'{caminho_path}\challenge')
p.sleep(1)
p.press('enter')

localStart = p.locateOnScreen('./images/start.png', confidence=0.9)
centerLocalStart = p.center(localStart)
p.click(centerLocalStart[0], centerLocalStart[1])

dados = pd.read_excel('challenge.xlsx', sheet_name='Sheet1')

df = pd.DataFrame(dados, columns=['First Name', 'Last Name ', 'Company Name', 'Role in Company', 'Address', 'Email', 'Phone Number'])

for linha in df.itertuples():
    localName = p.locateOnScreen('./images/labelName.png', confidence=0.9)
    centerLocalName = p.center(localName)
    p.click(centerLocalName[0], centerLocalName[1]+20)
    p.write(linha[1])

    localLastName = p.locateOnScreen('./images/labelLastName.png', confidence=0.9)
    centerLocalLastName = p.center(localLastName)
    p.click(centerLocalLastName[0], centerLocalLastName[1]+20)
    p.write(linha[2])

    localCompany = p.locateOnScreen('./images/labelCompany.png', confidence=0.9)
    centerLocalCompany = p.center(localCompany)
    p.click(centerLocalCompany[0], centerLocalCompany[1]+20)
    p.write(linha[3])

    localRole = p.locateOnScreen('./images/labelRole.png', confidence=0.9)
    centerLocalRole = p.center(localRole)
    p.click(centerLocalRole[0], centerLocalRole[1]+20)
    p.write(linha[4])

    localAddress = p.locateOnScreen('./images/labelAddress.png', confidence=0.9)
    centerLocalAddress = p.center(localAddress)
    p.click(centerLocalAddress[0], centerLocalAddress[1]+20)
    p.write(linha[5])

    localEmail = p.locateOnScreen('./images/labelEmail.png', confidence=0.9)
    centerLocalEmail = p.center(localEmail)
    p.click(centerLocalEmail[0], centerLocalEmail[1]+20)
    p.write(linha[6])

    localPhone = p.locateOnScreen('./images/labelPhone.png', confidence=0.9)
    centerLocalPhone = p.center(localPhone)
    p.click(centerLocalPhone[0], centerLocalPhone[1]+20)
    p.write(str(linha[7]))

    localSubmit = p.locateOnScreen('./images/labelSubmit.png', confidence=0.9)
    centerLocalSubmit = p.center(localSubmit)
    p.click(centerLocalSubmit[0], centerLocalSubmit[1])