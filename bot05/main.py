import os
import pyautogui

caminho_path = os.path.dirname(os.path.abspath(__file__))

pyautogui.hotkey('win', 'r')
pyautogui.write(caminho_path + '\RPA.pbix')
pyautogui.press('enter')

pyautogui.sleep(20)
pyautogui.click(x=779, y=96)

pyautogui.sleep(5)
pyautogui.click(x=1901, y=15)
pyautogui.sleep(2)
pyautogui.press('enter')