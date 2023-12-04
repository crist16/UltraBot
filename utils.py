import time
import pyautogui
from pyautogui import ImageNotFoundException
import subprocess

import pyperclip

contador = 0

time.sleep(5)
def cerrarPestanas():
    while contador<=6:
        try:
            
            coordx,coordy = pyautogui.locateCenterOnScreen('images/cerrar.png',confidence=0.99)
            pyautogui.click(coordx,coordy)
        except:
            print("Error")
            break
        


def reiniciarIp():
    subprocess.call(['ipconfig','/release'],shell=True)
    subprocess.call(['ipconfig','/renew'],shell=True)


def pestanasRecorrer(contador):
    time.sleep(5)
    while contador <=7:
        try:
            contador = contador+1        
            coordenada = pyautogui.locateOnScreen('images/icon.png',confidence=0.99)
            center = pyautogui.center(coordenada)
            coordx,coordy = center
            pyautogui.click(coordx,coordy)
        except : 
               
            print('Fin de ciclo')
            break
            


def IniciarSession(coordPestanas, botones):
    for p in coordPestanas:
        time.sleep(6)
        pyautogui.click(x=coordPestanas[p][0],y=coordPestanas[p][1]) 
        time.sleep(3)
    
        pyautogui.click(x=botones["iniciarSesion"][0],y=botones["iniciarSesion"][1])
        time.sleep(3)

def IntroducirUsuario(usrInputCoords, usrPassworCoords, coordPestanas, lines):
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
        time.sleep(1)
        pyautogui.click(x=usrPassworCoords[0],y=usrPassworCoords[1])  

        pyautogui.click(x=usrPassworCoords[0],y=usrPassworCoords[1])  
    
        time.sleep(1)
        pyautogui.hotkey("ctrl","v")
        time.sleep(1)   
        pyautogui.press('enter')


def LeerLineas(numeroTxt):
    with open(f"{numeroTxt}.txt","r") as file:
            lines = file.readlines()
            lineArray = lines
    return lines


def LastViewWrite(today, numeroTxt):
    with open("lastview.txt","+a") as file:
        file.write(f'{today}\n {numeroTxt}\n')

def StartClick(coordPestanas, botones):
    for p in coordPestanas:
        time.sleep(2)
        pyautogui.click(x=coordPestanas[p][0],y=coordPestanas[p][1])
        pyautogui.click(x=botones["start"][0], y= botones["start"][1])
        time.sleep(2)