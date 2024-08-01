import pyautogui as gui
import random, time, os
from colorama import Fore

version = "1.0"
os.system("pip install colorama")
os.system("pip3 install colorama")
os.system("pip3 install pyautogui")
os.system("clear")

print(Fore.GREEN+"""

Hewo!, welcome to ZBrute
visit my github: https://github.com/AlbedoPrime
By: Zeldr1$

""")
print(Fore.MAGENTA+"Type 'help' or -h to see commands ")
	
while True:
	
	
	def path():
		print(Fore.MAGENTA+"Type 'start' to start")
		print(Fore.MAGENTA+"and it will automatically start in 5sec")
		print(Fore.MAGENTA+"you must select a textbox so it will work")
		ui = input(Fore.CYAN+"Zeldr1$~: ").lower()
		if(ui == 'start'):
		      
			w = "pass.txt"
			w_open = open(w, 'r')
			
			time.sleep(10)
			for x in w_open:
				print(Fore.GREEN+x)
				gui.write(x)
				gui.press('Enter')
				time.sleep(.5)
				gui.press('backspace', presses=6)
		      
		else:
		      print("Type s or start to start.")
		      return()
 	
	def default():
		print(Fore.MAGENTA+"Type 'start' to start")
		print(Fore.MAGENTA+"and it will automatically start in 5sec")
		print(Fore.MAGENTA+"you must select a textbox so it will work")
		ui = input(Fore.CYAN+"Zeldr1$~: ").lower()
		if(ui == 'start'):
		      
			char = "1234567890"
			char_list = list(char)
			chars = "four"
			
			time.sleep(5)
			while True:
				r = random.choices(char_list, k=len(chars))
				print(Fore.GREEN, r)
				gui.write(r)
				gui.press('Enter')
				time.sleep(.2)
				gui.press('backspace',presses=6)
				
		else:
		      print("Type s or start to start.")
		      return()  
	
	
	def help():
		print("""  
	==================================================
	+-+|  ZBrute coded by Zeldr1$                 |+-+
	==================================================
	+-+|     COMMANDS            Decription       |+-+
	+-+|------------------------------------------|+-+
	+-+|   [1] =======   bruteforce por wordlist  |+-+
	+-+|   [2] ==========  brutefoce por pin      |+-+
	+-+|   [3] ==============  Ajuda              |+-+
	+-+|   [0] =================== Sair           |+-+
	+-+|                                          |+-+
 	==================================================		
 	""")	

	def about():
		print(f"""
          =================================================
  	      +-+|             About this tool             |+-+
  	      =================================================
  	      +-+|              This Tool Is               |+-+
          +-+|                Createad                 |+-+
    	  +-+|                   By                    |+-+
    	  +-+|                 Zeldr1$                 |+-+
     	  +-+|        for Zeldr1$ team Clonwters       |+-+
          +-+|-----------------------------------------|+-+
    	  +-+| Tool name: ZBrute                       |+-+
   	      +-+| Use To Brute Zeldr1$                    |+-+
    	  +-+| Tool version: {version}                 |+-+
          +-+|-----------------------------------------|+-+
    	  +-+|                Contact                  |+-+
    	  +-+|                Telefone                 |+-+
          +-+|             +5515997224510              |+-+
          +-+|--------------^--------^-----------------|+-+
    	  +-+| Github: https://github.com/AlbedoPrime  |+-+
     	  +-+|                                         |+-+
    	  +-+|                 Note!                   |+-+
          +-+|   This tool is Originally created by me |+-+
          +-+|   so please dont republish it on github |+-+
          +-+|   i do not autorized you to edit this   |+-+
          +-+|   tool or republish it on github.       |+-+
          +-+|                                         |+-+
          +-+|         Editing or changing the         |+-+
          +-+|       name of the coder or developer    |+-+
          +-+|        wont make you a programmer.      |+-+
          +-+|                                         |+-+
          +-+|        [+]Respect the coder's[+]        |+-+
          +-+|     ©️Copyright All Rights Reserved      |+-+
          ================================================= 
		""")


	ui = input(Fore.WHITE+"Zeldr1$ >~: ").lower()
	
	if(ui == 'help' or ui == '-h'):
		help()
	elif(ui == '1'):
		path()
	elif(ui == '2'):
		default()
	elif(ui == '3'):
		about()
	elif(ui == '0'):
		break
	else:
		os.system("clear")
		print("Error! command not found!")
		print("Try Executing -h ")
		time.sleep(1)

