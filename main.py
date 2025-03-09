# library
import time
import sys
import os
import platform
from matematika import matematika
sys.path.append('d:/Programs/python')

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# My name
myname = """
##########        ###       ##  #####           ###       ###       ##
       ##        ## ##      ##  ##   ###       ## ##      ####      ##
     ##         ##   ##     ##  ##     ##     ##   ##     ## ###    ##
   ##          #########    ##  ##     ##    #########    ##   ###  ##
 ##           ##       ##   ##  ##   ###    ##       ##   ##     #####
###########  ##         ##  ##  #####      ##         ##  ##       ###
"""

mainfitur = """

++ pilih fitur utama

+====+============+
+ NO + nama fitur +
+====+============+
+ 01 + Portofolio +
+ 02 + Matematika +
+====+============+

"""

try:
    clear_screen()
    
    # teks animation
    for char in myname:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

    for char in mainfitur:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

    pilihanmain = float(input("Pilih fitur utama [0 = exit] : "))

    if pilihanmain == 1:
        portofolio()
    elif pilihanmain == 2:
        matematika()
    elif pilihanmain == 0:
      sys.exit(0)
        
except KeyboardInterrupt:
    print("\nProgram dihentikan...")
    sys.exit(0)