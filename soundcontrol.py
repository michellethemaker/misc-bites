import psutil
import pyautogui
from win32gui import FindWindow, GetWindowText # install w pip install pywin32
import time
import argparse

def list_running_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)

def open_soundsettings_auto():
    x,y = pyautogui.locateCenterOnScreen('symbol_sound.PNG', confidence=0.8)
    pyautogui.moveTo(x, y)
    pyautogui.rightClick()
    x,y = pyautogui.locateCenterOnScreen('symbol_soundsettings.PNG', confidence=0.8)
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.hotkey('win', 'up')
    pyautogui.hotkey('esc')
    time.sleep(0.5)
    x,y = pyautogui.locateCenterOnScreen('symbol_soundoptions.PNG', confidence=0.8)
    pyautogui.moveTo(x,y)
    pyautogui.click()

def change_to_headphones(appname, appimg, appimg2): # note that impt_apps_img height must be slightly taller than speaker/headphones img so locateCenterOnScreen can find it within the region specified.
    running_apps = [proc.info['name'].lower() for proc in psutil.process_iter(['name'])]
    speaker_img = 'symbol_sound_speakers.png'
    headphones_img = 'symbol_sound_headphones.png'
    default_img = 'symbol_sound_default.png'
    default2_img = 'symbol_sound_default2.png'
    impt_apps = [appname, appname]
    impt_apps_img = [appimg, appimg2]
    im1 = pyautogui.screenshot('img.PNG')
    icon_left, icon_top = 0,0
    default_left, default_top = 0,0
    for app, app_img in zip(impt_apps, impt_apps_img):
        if app in running_apps:
            print(f'{app.capitalize()} is running. Switching to headphones...')
            try:
                icon_loc = pyautogui.locateOnScreen(app_img, region=(0, 0, im1.width, im1.height), confidence=0.95) # region=(startXValue,startYValue,width,height)
                if icon_loc:
                    icon_left = icon_loc.left
                    icon_top = icon_loc.top
                    print(f'{icon_loc.left}, {icon_loc.top}, {im1.width}, {icon_loc.height}')
                    print(f'icon located: {icon_loc.left}')
                    break
                else:
                    print(f'icon for {app} not found...')
            except:
                continue
    try:
        print("try to find speaker")
        x, y = pyautogui.locateCenterOnScreen(speaker_img, region=(icon_left, icon_top, im1.width, icon_loc.height), confidence=0.7)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter') # is now headphones
        
    except:
        print("cannot find speaker, try to find headphones")
        # curr_selected_loc = pyautogui.locateOnScreen(headphones_img, region=(0, 0, im1.width, im1.height), confidence=0.95)
        x, y = pyautogui.locateCenterOnScreen(headphones_img, region=(icon_left, icon_top, im1.width, icon_loc.height), confidence=0.7)
        # print(f'LOCATED: {pyautogui.locateCenterOnScreen(app_img, region=(0, 0, speaker_img.width, speaker_img.height), confidence=0.7)}, centre: {x},{y}')
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter') # is now speaker
        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen(speaker_img, region=(icon_left, icon_top, im1.width, icon_loc.height), confidence=0.7)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter') # is now headphones


def change_to_speaker(appname, appimg, appimg2): # note that impt_apps_img height must be slightly taller than speaker/headphones img so locateCenterOnScreen can find it within the region specified.
    running_apps = [proc.info['name'].lower() for proc in psutil.process_iter(['name'])]
    speaker_img = 'symbol_sound_speakers.png'
    headphones_img = 'symbol_sound_headphones.png'
    impt_apps = [appname, appname]
    impt_apps_img = [appimg, appimg2]
    im1 = pyautogui.screenshot('img.PNG')
    icon_left, icon_top = 0,0
    for app, app_img in zip(impt_apps, impt_apps_img):
        if app in running_apps:
            print(f'{app.capitalize()} is running. Switching to headphones...')
            try:
                icon_loc = pyautogui.locateOnScreen(app_img, region=(0, 0, im1.width, im1.height), confidence=0.95) # region=(startXValue,startYValue,width,height)
                if icon_loc:
                    icon_left = icon_loc.left
                    icon_top = icon_loc.top
                    print(f'{icon_loc.left}, {icon_loc.top}, {im1.width}, {icon_loc.height}')
                    print(f'icon located: {icon_loc.left}')
                    break
                else:
                    print(f'icon for {app} not found...')
            except:
                continue
    try:
        print("try to find speaker")
        x, y = pyautogui.locateCenterOnScreen(speaker_img, region=(icon_left, icon_top, im1.width, icon_loc.height), confidence=0.7)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.hotkey('up')
        pyautogui.hotkey('enter') # is now headphones
        time.sleep(2)
        x, y = pyautogui.locateCenterOnScreen(headphones_img, region=(icon_left, icon_top, im1.width, icon_loc.height), confidence=0.7)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter') # is now speaker

    except:
        print("cannot find speaker, try to find headphones")
        # curr_selected_loc = pyautogui.locateOnScreen(headphones_img, region=(0, 0, im1.width, im1.height), confidence=0.95)
        x, y = pyautogui.locateCenterOnScreen(headphones_img, region=(icon_left, icon_top, im1.width, icon_loc.height), confidence=0.7)
        # print(f'LOCATED: {pyautogui.locateCenterOnScreen(app_img, region=(0, 0, speaker_img.width, speaker_img.height), confidence=0.7)}, centre: {x},{y}')
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter') # is now speaker


parser = argparse.ArgumentParser()
parser.add_argument('--program', type=str, help='run what?') # soundsettings, changesoundsource 
parser.add_argument('--app', type=str, help='app name')
parser.add_argument('--source', type=str, help='source type')
# parser.add_argument('--source', type=int, nargs='+', help='List of numbers')


args = parser.parse_args()

if args.program == 'soundsettings':
    open_soundsettings_auto()

elif args.program == 'changesoundsource':
    open_soundsettings_auto()
    if args.source == 'speakers':
        change_to_speaker(f'{args.app}.exe',f'symbol_sound_{args.app}.png',f'symbol_sound_{args.app}2.png')
    elif args.source == 'headphones':
        change_to_headphones(f'{args.app}.exe',f'symbol_sound_{args.app}.png',f'symbol_sound_{args.app}2.png')