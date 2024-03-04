import schedule
import time
import pyautogui as p

def bot():
    p.FAILSAFE = False 
    p.hotkey('win', 'r') 

    p.sleep(2)
    p.typewrite('notepad') 
    p.sleep(2)
    p.press('enter') 
    p.sleep(2)
    p.typewrite("Hello, I'm a bot")
    p.sleep(2)

    janela = p.getActiveWindow()
    p.sleep(2)
    janela.close()

"""schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
schedule.every().minute.at(":17").do(job)"""

schedule.every().day.at("13:15").do(bot)

while True:
    schedule.run_pending()
    time.sleep(1)