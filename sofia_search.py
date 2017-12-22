# program to download history files

import subprocess
import pyautogui
import time
import os
import glob
import collections
import itertools
import sys

count = 0
pac_num = 31

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

    def history_loop(from_pac, pac_num):

        # Calculate position of from Pac file in History tab within Sofia browser
        rel_width, rel_height = pos_calc(659, 207)
    
        pyautogui.moveRel(rel_width, 0, duration=0.50)
        pyautogui.moveRel(0, rel_height, duration=0.50)
    
        pyautogui.click()
    
        time.sleep(2)

        pyautogui.typewrite(from_pac)
        global count

        if count > 0:

            to_pac = str(pac_num + 1) + '.1-0'
            # Calculate position of to Pac History tab within Sofia browser
            rel_width, rel_height = pos_calc(771, 203)

            pyautogui.moveRel(rel_width, 0, duration=0.50)
            pyautogui.moveRel(0, rel_height, duration=0.50)

            pyautogui.click()

            pyautogui.typewrite(to_pac)
            
            
        # Calculate position of Show changes in History tab within Sofia browser
        rel_width, rel_height = pos_calc(833, 207)
    
        pyautogui.moveRel(rel_width, 0, duration=0.50)
        pyautogui.moveRel(0, rel_height, duration=0.50)

        pyautogui.click()
    
        time.sleep(200)

        # Calculate position of Save file in History tab within Sofia browser
        rel_width, rel_height = pos_calc(943, 203)

        pyautogui.moveRel(rel_width, 0, duration=0.50)
        pyautogui.moveRel(0, rel_height, duration=0.50)
    
        time.sleep(2)
    
        pyautogui.click()
    
        time.sleep(2)

        count = count + 1

        # Calculate position of Save file in History tab within Sofia browser
        rel_width, rel_height = pos_calc(649, 736)

        pyautogui.moveRel(rel_width, 0, duration=0.50)
        pyautogui.moveRel(0, rel_height, duration=0.50)

        pyautogui.typewrite('RCS_BXSX' + str(count) + '.TXT')
    
        time.sleep(2)

        pyautogui.typewrite(['enter'])
    
        time.sleep(2)

    while pac_num > 30:
        pac_num = pac_num - 1
        string = str(pac_num) + '.1-0'
        history_loop(string, pac_num)

    print('Enter search string')
    search_string = input()

    # Loop through all PAC history files and print those
    # history versions which match the string search
    path = 'D:\\userdata\\vijs\\Desktop'
    for infile in glob.glob( os.path.join(path, 'RCS_BXSX*') ):
        print ('current file is: ' + infile)
        with open(infile) as f:
            before = collections.deque(maxlen=20)
            for line in f:
                if 'search_string' in line:
                    sys.stdout.writelines(before)
                    sys.stdout.write(line)
                    sys.stdout.writelines(itertools.islice(f, 15))
                    break
                else:
                    print('No PAC history file has the given search string')
                before.append(line)

    process.terminate()
    
except KeyboardInterrupt:
    print('\nDone')









