pip install pyautogui
pip install pyperclip

import pyautogui
import pyperclip #auxiliar para copiar uma string com possíveis caracteres especiais
import time #pre instalado

#in order to not break the flow, you might want to wait a second for each step, there you wait 1 second
pyautogui.PAUSE = 1

#hotkey is for combined shortcuts
pyautogui.hotkey("crtl", "t")
pyperclip.copy("www.thelinkyouwant.com") #copy site's link 

pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5) #para o sistema esperar n segundos para um sistema carregar

#para descobrir a coordenada na tela de algum botão pra clicar
   time.sleep(5)
   pyautogui.position()
    
#para clicar
pyautogui.click(x = x, y = y, clicks = "n de clicks") 
