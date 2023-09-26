import pyautogui
import keyboard

agentDisp = ["Astra", "Breach", "Brimstone", "Chamber", "Cypher", "Fade", "Harbor", "Jett", "Kayo", "Killjoy", "Neon", "Omen", "Phoenix", "Raze", "Reyna", "Sage", "Skye", "Sova", "Viper", "Yoru"]

print("Instalock v1 par Fael")
print(" ")

def agentLocked():
    agentLock = input("Quel agent voulez-vous instalock ? ")
    if agentLock in agentDisp:
        print("Vous avez choisi: " + agentLock + ". Bon choix ! (M pour activer / P pour quitter !)")
        defaultMouseLoc = pyautogui.position()
        while True:
            try:
                if keyboard.is_pressed('m'):
                    #Astra
                    if agentLock == "Astra":
                        pyautogui.moveTo(590, 925)
                        pyautogui.click()
                    #Breach
                    elif agentLock == "Breach":
                        pyautogui.moveTo(675, 925)
                        pyautogui.click()
                        #Brimstone
                    elif agentLock == "Brimstone":
                        pyautogui.moveTo(750, 925)
                        pyautogui.click()
                        #Chamber
                    elif agentLock == "Chamber":
                        pyautogui.moveTo(830, 925)
                        pyautogui.click()
                        #Cypher
                    elif agentLock == "Cypher":
                        pyautogui.moveTo(915, 925)
                        pyautogui.click()
                    #Fade
                    elif agentLock == "Fade":
                        pyautogui.moveTo(1005, 925)
                        pyautogui.click()
                    #Harbor
                    elif agentLock == "Harbor":
                        pyautogui.moveTo(1090, 925)
                        pyautogui.click()
                        #Jett
                    elif agentLock == "Jett":
                        pyautogui.moveTo(1175, 925)
                        pyautogui.click()
                        #Kayo
                    elif agentLock == "Kayo":
                        pyautogui.moveTo(1260, 925)
                        pyautogui.click()
                        #Killjoy
                    elif agentLock == "Killjoy":
                        pyautogui.moveTo(1340, 925)
                        pyautogui.click()
                    #Neon
                    if agentLock == "Neon":
                        pyautogui.moveTo(590, 1010)
                        pyautogui.click()
                    #Omen
                    elif agentLock == "Omen":
                        pyautogui.moveTo(675, 1010)
                        pyautogui.click()
                    #Phoenix
                    elif agentLock == "Phoenix":
                        pyautogui.moveTo(750, 1010)
                        pyautogui.click()
                    #Raze
                    elif agentLock == "Raze":
                        pyautogui.moveTo(830, 1010)
                        pyautogui.click()
                    #Reyna
                    elif agentLock == "Reyna":
                        pyautogui.moveTo(915, 1010)
                        pyautogui.click()
                    #Sage
                    elif agentLock == "Sage":
                        pyautogui.moveTo(1005, 1010)
                        pyautogui.click()
                    #Skye
                    elif agentLock == "Skye":
                        pyautogui.moveTo(1090, 1010)
                        pyautogui.click()
                    #Sova
                    elif agentLock == "Sova":
                        pyautogui.moveTo(1175, 1010)
                        pyautogui.click()
                    #Viper
                    elif agentLock == "Viper":
                        pyautogui.moveTo(1260, 1010)
                        pyautogui.click()
                    #Yoru
                    elif agentLock == "Yoru":
                        pyautogui.moveTo(1340, 1010)
                        pyautogui.click()
                    #Verrouiller
                    pyautogui.moveTo(958, 813)
                    pyautogui.click()
                elif keyboard.is_pressed('p'):
                        print("Fermeture de VLock !")
                        pyautogui.moveTo(defaultMouseLoc)
                        break
            except:
                pyautogui.moveTo(defaultMouseLoc)
                break
    else:
        print("Agent introuvable, réessaye avec la bonne orthographe ! (Première lettre en majuscule le reste en minuscule !)")
        agentLocked()    
              
agentLocked()
