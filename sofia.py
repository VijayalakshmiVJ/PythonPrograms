# program to download history files

import subprocess
import pyautogui
import time

count = 0
try:
    process = subprocess.Popen([r"C:\apps\DMXSEE\Winsofia\winsofia.exe"])
    
    def pos_calc(sofia_width, sofia_height):
        width, height = pyautogui.position()
        rel_width = sofia_width - width
        rel_height = sofia_height - height
        return rel_width, rel_height
    
    # Calculates the mouse position to reach various Sofia browsers attributes
    
    # Position when Winsofia appears in the middle
    #rel_width, rel_height = pos_calc(712, 497)

    # Calculate position of Sofia browser within Winsofia(when it appears at top left)
    rel_width, rel_height = pos_calc(38, 217)
    
    time.sleep(10)
    
    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)
    
    pyautogui.click()
    
    time.sleep(10)
    
    # Calculate position of Field to type PAC within Sofia browser
    rel_width, rel_height = pos_calc(44, 107)
    
    pyautogui.typewrite('RCS_BXSX.PAC')
    time.sleep(2)
    
    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)
    
    pyautogui.typewrite(['enter'])
    
    # Calculate position of History file tab within Sofia browser
    rel_width, rel_height = pos_calc(186, 62)
    
    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)
    
    time.sleep(3)
    
    pyautogui.click()
    
    # Calculate position of History in text mode tab within Sofia browser
    rel_width, rel_height = pos_calc(1078, 184)
    
    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)
    
    time.sleep(2)
    
    pyautogui.click()
    
    time.sleep(15)
    
    # Calculate position of Save file in History tab within Sofia browser
    rel_width, rel_height = pos_calc(943, 203)
    
    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)
    
    time.sleep(2)
    
    pyautogui.click()

    count = count + 1

    # Calculate position of Save file in History tab within Sofia browser
    rel_width, rel_height = pos_calc(649, 736)

    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)
    
    pyautogui.typewrite('RCS_BXSX' + str(count) + '.TXT')
    
    time.sleep(2)
    
    pyautogui.typewrite(['enter'])
    
    time.sleep(2)

    ##############################


    count = count + 1
    rel_width, rel_height = pos_calc(765, 207)

    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)

    pyautogui.click()
    time.sleep(1)

    pyautogui.typewrite('31.26-0')
                        

    time.sleep(1)
    rel_width, rel_height = pos_calc(672, 205)

    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)

    pyautogui.click()
    time.sleep(1)

    pyautogui.typewrite('31.26-0')
    time.sleep(1)


    rel_width, rel_height = pos_calc(943, 203)
    
    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)
    
    time.sleep(1)
    
    pyautogui.click()
    
    rel_width, rel_height = pos_calc(649, 736)

    pyautogui.moveRel(rel_width, 0, duration=0.50)
    pyautogui.moveRel(0, rel_height, duration=0.50)
    
    pyautogui.typewrite('RCS_BXSX' + str(count) + '.TXT')
    
    time.sleep(2)
    
    pyautogui.typewrite(['enter'])
    
    time.sleep(2)

    #############################
    
    process.terminate()
except KeyboardInterrupt:
    print('\nDone')









