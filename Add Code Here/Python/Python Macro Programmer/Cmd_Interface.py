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

def printing(formatLen, keys, macro):
    print('''{}{:>{}}'''.format(keys,"-> " + macro, formatLen + len(macro) - len(keys)))
    
def listing():
    formatLen = 5 + len(max(allKeys, key=len))
    print("STARTUP TYPE:")
    printing(formatLen, "RunType", runtype["RunType"])

    if runtype["RunType"] == "0":
        printing(formatLen, "Toggle", runtype["Toggle"])
        
    elif runtype["RunType"] == "1":
        printing(formatLen, "Start", runtype["Start"])
        printing(formatLen, "Stop", runtype["Stop"])
    
    print("\nMACROS:")
    for keys,macro in macros.items():
        printing(formatLen, keys, macro)
        
    
    print("\nREMAPPED KEYS")
    for keys,remaped in remap.items():
        printing(formatLen, keys, remaped)
        
def readJson():
    with open("Macro.json", "r") as outfile:
        # json.dump(macros, outfile)
        # json.dump(remap, outfile)
        return json.load(outfile)
    
def WriteJson():
    with open("Macro.json", "w") as outfile:
        json.dump((runtype, macros, remap), outfile, indent=4)

def delete_last_line(howmanyLines = 1):
    '''Deletes the last line in the STDOUT'''
    for i  in range(howmanyLines):
        # cursor up one line
        sys.stdout.write('\x1b[1A')
        # delete last line
        sys.stdout.write('\x1b[2K')

def keyPressed(textToPrint = '''(`/~)    -> back to main menu
Your Input: 
'''):
    enteredkey = None
    print(textToPrint)
    while True:
        event = ky.read_event()
        
        if event.event_type == ky.KEY_DOWN and not (event.name in ("enter","`","~")):
            delete_last_line()
            enteredkey = (ky.read_hotkey(suppress=False))
            print(enteredkey)

        if ky.is_pressed("enter"):
            input()
            delete_last_line()
            return (enteredkey)
        
        if ky.is_pressed("`") or ky.is_pressed("~") :
            
            return ("`")

def MenuKeyinput():
    enteredkey = None
    print()
    while True:
        event = ky.read_event()
        
        if event.event_type == ky.KEY_DOWN and not (event.name in ("enter")):
            delete_last_line()
            enteredkey = (ky.read_key(suppress=False))
            print(enteredkey)

        if ky.is_pressed("enter"):
            input()
            return (enteredkey)
                
def runTypeRemap():
    formatLen = 5 + len(max(allKeys, key=len))
    
    while True:
        print("Set startup Type:")
        printing(formatLen, "Toggle", "0")
        printing(5+len("different keys for Start and Stop"), "different keys for Start and Stop", "1")
        output = keyPressed()
        
        if output in ("`","~"):
            return 
        
        elif output in ("0","1"):
            runtype["RunType"] = output

            while True:
                
                os.system('cls')
                if runtype["RunType"] == "0":
                    print(f'''Current: Toggle -> {runtype["Toggle"]}''')
                    remapTO = keyPressed('''(`/~) -> back to main menu
new: Toggle -> 
''')
                    if remapTO in ("`","~"):
                        return
                    
                    else:
                        runtype["Toggle"]=remapTO
                    
                    print(f'New Toggle -> {runtype["Toggle"]}')
                    WriteJson()
                    return 
                
                elif runtype["RunType"] == "1":
                    for i in ("Start", "Stop"):
                        
                        print(f"Current: {i} -> {runtype[i]}")
                        remapTO = keyPressed(f'''(`/~) -> back to main menu
new: {i} -> 
''')
                        if remapTO in ("`","~"):
                            return
                        
                        else:
                            runtype[i] = remapTO
                            
                        print()
                    WriteJson()
                    return 
                
        else:
            os.system('cls')
            continue
        
def macroKey():
    formatLen = 5 + len(max(allKeys, key=len))
    macroList = list(macros.keys())

    print(f'''press which key to make macro:
          ''')
    
    for i in (macroList):
        printing(formatLen, i, macros[i])

    output =keyPressed()
    os.system('cls')    
    if output in ("`","~"):
        return 

    if (output not in macroList):
        print(f'''New macro key:''')
        
    newKey = output
    print(f'''{newKey} : ''')
    newMacro = input("enter the string: ")
    
    if newMacro == "":
        if (output not in macroList):
            print("Macro creation aborted")
            return
        
        else:
            macros.pop(newKey)
            print(f'''{newKey} remap key removed''')
            WriteJson()
            return 
        
    else:
        print(f"New Remap:")
        printing(formatLen,newKey, newMacro)
        
    macros[newKey] = newMacro
    WriteJson()
    return 

def remapkey():
    formatLen = 5 + len(max(allKeys, key=len))
    remapList = list(remap.keys())
    
    while True:
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
                printing(formatLen, i, remap[i])
            output =keyPressed()
            
            if output in ("`","~"):
                return 

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
                    print(f"new remap")
                    printing(formatLen,newKey, newRemap)
                    
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
                    print(f"new remap")
                    printing(formatLen,newKey, newRemap)
                    
            remap[newKey] = newRemap
            WriteJson()
            return 
        
        else:
            os.system('cls')
            continue

def spKey():
    formatLen = 5 + len(max(allKeys, key=len))
    remapList = list(key for key,item in remap.items() if item in sp_function_list.keys())
    sp_functions = list(sp_function_list.keys())
    
    print(f'''which key to make special macro:''')
    
    for i in (remapList):
        printing(formatLen,i, remap[i])
    output =keyPressed()
    
    if output in ("`","~"):
        return 

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


if __name__ =="__main__":
    runtype, macros, remap  = readJson()
    allKeys = list((runtype | macros | remap))
    
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