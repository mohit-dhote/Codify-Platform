import json
import os
import keyboard as ky
import sys
import subprocess
from Macro_Programmer import sp_Functions as sp_function_list
def mainMenu():
    print('''Welcome to the Python Macro Programmer
Help ->\t\t\t0 
list all macros -> \t1
change Start Type -> \t2
change macro keys -> \t3
change remap keys -> \t4
change special keys ->\t5
Quit and start app -> \t6
Quit without starting - (`/~)
\tYour Input:\t''')
    output = MenuKeyinput()
    os.system('cls')
    return output
    
def help():
    print('''
•   This is a program that can help you make and use Macros or remap keys using python!!
              
•   Dont forget to add START and STOP macros, if you plan on changing the run type (also change the runtype to 1)

•   You can find all the supported keys/keytypes here:
    (https://pyautogui.readthedocs.io/en/latest/keyboard.html#:~:text=%5B%27%5Ct,%27optionright%27%5D)
    ''')
# •	Import the following libraries so that the code can run properly:
# 	(keyboard, pyautogui, screen_brightness_control)
# 	you can also convert the .py to .pyw so that it can run directly without any console popups,
# 	Or, use the .exe file which contains all the necessary dependencies.
# •	This program only supports simple macros, the (') would cause issues with the program.
# 	Also it only supports single line macros, so dont go adding paragraphs and expecting it to work
    
def listing():
    print("STARTUP TYPE:")
    print(f'''Runtype: {runtype["RunType"]}''')

    if runtype["RunType"] == "0":
        print(f'''Toggle -> {runtype["Toggle"]}''')
    elif runtype["RunType"] == "1":
        print(f'''Toggle -> {runtype["Start"]}''')
        print(f'''Toggle -> {runtype["Stop"]}''')
    
    print("\nMACROS:")
    for keys,macro in macros.items():
        print(f"{keys} -> {macro}")
    
    print("\nREMAPPED KEYS")
    for keys,remaped in remap.items():
        print(f"{keys} -> {remaped}")
        
def readJson():
    with open("Macro.json", "r") as outfile:
        # json.dump(macros, outfile)
        # json.dump(remap, outfile)
        return json.load(outfile)
    
def WriteJson():
    with open("Macro.json", "w") as outfile:
        json.dump((runtype, macros, remap), outfile, indent=4)

def delete_last_line():
    "Deletes the last line in the STDOUT"
    # cursor up one line
    sys.stdout.write('\x1b[1A')
    # delete last line
    sys.stdout.write('\x1b[2K')

def keyPressed():
    enteredkey = None
    print('''(`/~) -> back to main menu
Your Input: 
''')
    while True:
        event = ky.read_event()
        if event.event_type == ky.KEY_DOWN and not (event.name in ("enter","`","~")):
            delete_last_line()
            enteredkey = (ky.read_hotkey(suppress=False))
            print(enteredkey)

            # enteredkey = None
        if ky.is_pressed("enter"):
            input()
            delete_last_line()
            return (enteredkey)
        
        if ky.is_pressed("`") or ky.is_pressed("~") :
            
            return ("`")
        
        
        
        
    return enteredkey

def MenuKeyinput():
    enteredkey = None
    print()
    while True:
        event = ky.read_event()
        if event.event_type == ky.KEY_DOWN and not (event.name in ("enter")):
            delete_last_line()
            enteredkey = (ky.read_key(suppress=False))
            print(enteredkey)

            # enteredkey = None
        if ky.is_pressed("enter"):
            input()
            return (enteredkey)
                
def runTypeRemap():
    while True:
        print(''' Set startup Type:
0 -> Toggle
1 -> different keys for Start and Stop''')
        output = keyPressed()
        if output in ("`","~"):
            return 
        elif output in ("0","1"):
            
            
            runtype["RunType"] = output
            while True:
                if runtype["RunType"] == "0":
                    print(f'''\nCurrent: Toggle -> {runtype["Toggle"]}''')
                    print("new: Toggle -> ")
                    remapTO = keyPressed()
                    if remapTO in ("`","~"):
                        return
                    else:
                        runtype["Toggle"]=remapTO
                    
                    print(f'New Toggle -> {runtype["Toggle"]}')
                    
                    WriteJson()
                    return 
                elif runtype["RunType"] == "1":
                    for i in ("Start", "Stop"):
                        print(f'''\nCurrent: {i} -> {runtype[i]}
    new: {i} ->''')
                        remapTO = keyPressed()
                        if remapTO in ("`","~"):
                            return
                        else:
                            runtype[i] = remapTO
                    WriteJson()
                    return 
        else:
            os.system('cls')
            continue
        
def remapkey():
    while True:
        remapList = list(remap.keys())
        print('''Select the remapping method:
change by typing the keycode or name of the key -> \t0 
change by pressing the keys on the keyboard -> \t\t1''')
        remapMethod = keyPressed()
        if remapMethod in ("`","~"):
            return 
        elif remapMethod in ("0","1"):
            os.system('cls')
            print(f''' Remapping method : {remapMethod}

press which key to remap:
''')
            for i in remapList:
                print(f"{i} -> {remap[i]}")
            output =keyPressed()
            if output in ("`","~"):
                return 
            # selectedKey = (macroList[output-1], macros[macroList[output]])

            if bool(int(remapMethod)):
                if (output not in remapList):
                    print(f'''New remap key:''')
    
                newKey = output

                print(f'''{newKey} : ''')
                newRemap = keyPressed()
                if newRemap == None:
                    if output not in remapList:
                        print("new macro aborted")
                        return
                    else:
                        remap.pop(newKey)
                        print(f'''{newKey} remap key removed''')
                        WriteJson()
                        print()
                        
                        return
                else:
                    print(f'''new remap
{newKey} -> {newRemap}''')
            else:
                if (output not in remapList):
                    print(f'''combine different keys with (+)''')
                    print(f'''New remap key:''')
                else:
                    newKey = output

                print(f'''{newKey} : ''')
                newRemap = input("enter the key: ")
                if newRemap == "":
                    remap.pop(newKey)
                    
                    print(f'''{newKey} remap key removed''')
                    WriteJson()
                    
                    return
                else:
                    print(f'''new remap
{newKey} -> {newRemap}''')
            remap[newKey] = newRemap
            WriteJson()
            
            return 
        else:
            os.system('cls')
            continue

def spKey():
    remapList = list(key for key,item in remap.items() if item in sp_function_list.keys())
    sp_functions = list(sp_function_list.keys())
    print(f'''which key to make special macro:''')
    for i in (remapList):
        print(f"{i} -> {remap[i]}")
    output =keyPressed()
    if output in ("`","~"):
        return 
    # selectedKey = (remapList[output-1], macros[remapList[output]])
    while True:
        if (output not in remapList):
            print(f'''New macro key:''')
        newKey = output
            
        print(f'''{newKey} : 
enter -> remove macro''')
        for j in range(1,len(sp_functions)+1):
            print(f'''{j} -> {sp_functions[j-1]}''')
        newMacro = input("choose the function: ")
        if newMacro in ("0", ""):
            if output not in remapList:
                print("removed")
                return
            else:
                remap.pop(newKey)
                print(f'''{newKey} special macro removed''')
                WriteJson()
                return 
        elif newMacro in (str(i) for i in range(1,len(sp_functions)+1)):
            print(f'''new special macro:
    {newKey} -> {sp_functions[int(newMacro) -1]}''')
            remap[newKey] = sp_functions[int(newMacro) - 1]
            WriteJson()
            return 
        else:
            os.system('cls')
            continue

def macroKey():
    macroList = list(macros.keys())

    if ky.is_pressed('''`'''):
        return
    print(f'''press which key to make macro:
          ''')
    for i in (macroList):
        print(f"{i} -> {macros[i]}")
    output =keyPressed()
    os.system('cls')
    if output in ("`","~"):
        return 
    # selectedKey = (macroList[output-1], macros[macroList[output]])
    
    if (output not in macroList):
        print(f'''New macro key:''')
    newKey = output
        
    print(f'''{newKey} : ''')
    newMacro = input("enter the string: ")
    if newMacro == "":
        if (output not in macroList):
            print("Macro creation aborted`")
            return
        else:
            macros.pop(newKey)
            print(f'''{newKey} remap key removed''')
            WriteJson()
            return 
    else:
        print(f'''New Remap:
{newKey} -> {newMacro}''')
    macros[newKey] = newMacro
    WriteJson()
    return 




runtype, macros, remap  = readJson()
    
# keyPressed()  
while True:
    match mainMenu():
        case "0" :
            help();
        case "1" :
            listing();
        case "2" :
            runTypeRemap();
        case "3" :
            macroKey();
        case "4" :
            remapkey();
        case "5" :
            spKey()
        case "6":
            subprocess.run("Macro_Programmer.exe")
            break
        case "`":
            break
        case "~":
            break
        case _ :
            continue
    input("\nPress Enter to go back to main menu...")
    os.system('cls')
delete_last_line()