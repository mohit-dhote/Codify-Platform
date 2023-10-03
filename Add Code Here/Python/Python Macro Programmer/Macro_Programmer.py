import keyboard as ky
import pyautogui as pag
import screen_brightness_control as sbc
import re


def Toggle():
    global is_running
    is_running = not is_running
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

    if  not notToggle:
        ky.add_hotkey(re.findall(regex, data[3])[0],Toggle, suppress=True)

    else:
        ky.add_hotkey(re.findall(regex, data[4])[0], Start, suppress=True)
        ky.add_hotkey(re.findall(regex, data[5])[0], Stop, suppress=True)

def default_Macro (toPrint):
    ky.call_later(pag.write,args=[toPrint],delay= 0.001)
    
def remap_Macro(toRemap):
    ky.call_later(pag.hotkey,args=[toRemap])

def Macro():
    if is_running:
        for macro in macroString:
            functions = re.findall(regex, macro)
            print(functions)
            
            if macro[0] == 's':
                
                ky.add_hotkey(functions[0],sp_Functions.get(functions[1]), suppress=True)
            elif macro[0] == 'r':
                
                ky.add_hotkey(functions[0],remap_Macro,args=[functions[1]], suppress=True)
            else:
                ky.add_hotkey(functions[0],default_Macro, args= [str(functions[1])], suppress=True)


with open("Macros.txt", "r") as f:
    data = f.readlines()
macroString = re.findall(r'\{([^}]*)\}' , "".join(data))[0].strip().split("\n")


regex = r"'([^']*)'"
is_running = False
notToggle = bool(int(re.findall("([1,0])", data[0])[0]))

sp_Functions = {
                'Brightness_Up':lambda:ky.call_later(sbc.set_brightness, args=["+10"]),
                'Brightness_Down':lambda:ky.call_later(sbc.set_brightness, args=["-10"])
                }
runType()

ky.wait(re.findall(regex, data[2])[0], suppress= True, trigger_on_release= True)
