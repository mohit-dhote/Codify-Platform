import keyboard as ky
import pyautogui as pag
import screen_brightness_control as sbc
import json
import re


def Toggle():
    global is_running
    is_running = not is_running
    print("workinggg")
    Macro()
    
def Start():
    global is_running
    is_running = True
    Macro()
    
def Stop():
    global is_running
    is_running = False
    Macro()

def runType():
    
    if  toggle["RunType"] == "0":
        ky.add_hotkey(toggle["Toggle"],Toggle, suppress=True)

    elif toggle["RunType"] =="1":
        ky.add_hotkey(toggle["Start"], Start, suppress=True)
        ky.add_hotkey(toggle["Stop"], Stop, suppress=True)

def default_Macro (toPrint):
    ky.call_later(pag.write,args=[toPrint],delay= 0.001)
    
def remap_Macro(toRemap):
    ky.call_later(pag.hotkey,args=[toRemap])

def Macro():
    if is_running:
        print(macroString)
        print(type(macroString))
        
        for key, macro in macroString.items():
            print(f"{key} : {macro}")
            ky.add_hotkey(key,default_Macro, args= [macro], suppress=True)
            
        for key, remap in remapString.items():
            print(f"{key} : {remap}")
            if remap in sp_Functions:
                ky.add_hotkey(key,sp_Functions.get(remap), suppress=True)
                
            else:
                ky.add_hotkey(key,remap_Macro,args=[remap], suppress=True)

    elif not is_running:
        for macro in macroString.keys():            
            ky.remove_hotkey(macro)
            
        for remap in remapString.keys():            
            ky.remove_hotkey(remap)


sp_Functions = {
                'Brightness_Up':lambda:ky.call_later(sbc.set_brightness, args=["+10"]),
                'Brightness_Down':lambda:ky.call_later(sbc.set_brightness, args=["-10"])
                }

if __name__ =="__main__":
    with open("Macro.json", "r") as readFile:
        toggle,macroString,remapString = json.load(readFile)

    is_running = False
        


    runType()

    ky.wait(toggle["Exit"], suppress= True, trigger_on_release= True)
    