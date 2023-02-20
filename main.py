
import time
from datetime import date
import pyautogui
import os
import msvcrt
import pyperclip

usrInputCoords = [700,450]
usrPassworCoords = [780,530]
contador = 0
today = date.today()
numeroTxt = input("Agregue el nombre del txt")
linesArray = []
coordPestanas = {
    "1" : [119,65],
    "2" : [343,65],
    "3" : [540,72],
    "4" : [768,72],
    "5" : [988,72],
    "6" : [1203,72],
    "7" : [1424,58]

}



botones = {
    "iniciarSesion" : [1400,230],
    "start" : [740,140]
}
""""

RECORRER PESTAÑAS 
CLICAR INICIAR SESSION
COPIAR USER 
PEGAR EN FORMULARIO
COPIAR PASSWORD 
PEGAR EN FORMULARIO
PRESIONAR ENTER
PRESIONAR INICIAR
"""

#aBRIR PROGRAMA

#os.startfile(r"C:\Users\rafae\AppData\Local\Programs\Ultra\Ultra.exe")
time.sleep(12)
print("Fin sleep")

with open("lastview.txt","+a") as file:
    file.write(f'{today}\n {numeroTxt}\n')

"""

#ABRIR LAS PESTAÑAS 
while contador <=6:
    
    try:
        contador = contador+1
        
        pyautogui.click("images/icon.png")
        print("CLicked here")
    except:    
        pyautogui.click("images/addPestanaUltra.png")
        contador = contador+1
   

#Recorrer pestañar
for p in coordPestanas:
    time.sleep(2)
    pyautogui.Sinthianice@protonmail.comclick(x=coordPestanas[p][0],y=coordPestanas[p][1])
    time.sleep(3)
    pyautogui.click(x=botones["iniciarSesion"][0],y=botones["iniciarSesion"][1])
    time.sleep(3)
"""
    
   
with open(f"{numeroTxt}.txt","r") as file:
        lines = file.readlines()
        lineArray = lines
    
    
for idx,line in enumerate(lines):       
    #obteniendo usr y password
    lineArray = line.split(",")
    usr = lineArray[0]
    pyperclip.copy(usr)
    pyautogui.click(x=coordPestanas[f"{idx+1}"][0],y=coordPestanas[f"{idx+1}"][1])
    pyautogui.click(x=usrInputCoords[0],y=usrInputCoords[1])
    pyautogui.hotkey ("ctrl","v")
    time.sleep(2)
    
    password = lineArray[1]
    pyperclip.copy(password)
    time.sleep(2)
    pyautogui.click(x=usrPassworCoords[0],y=usrPassworCoords[1])  

    pyautogui.click(x=usrPassworCoords[0],y=usrPassworCoords[1])  
    
    time.sleep(2)
    pyautogui.hotkey("ctrl","v")
    time.sleep(2)   
    pyautogui.press('enter')


for p in coordPestanas:
    time.sleep(2)
    pyautogui.click(x=coordPestanas[p][0],y=coordPestanas[p][1])
    pyautogui.click(x=botones["start"][0], y= botones["start"][1])
    time.sleep(2)   



msvcrt.getch()




           
        