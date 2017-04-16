#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__   = "16.04.2017"

import os, sys, pip, subprocess

dirs = os.listdir(os.getcwd())

def installModule(module):
	pip.main(['install', module])
	print "=" * 60

def main():
	try:
		import mss
	except ImportError:
		 if raw_input("[!] Mss module not found. Do you want install it?[Y/n] --> ").lower() == "y":
		 	installModule("mss")
		 else:
		 	sys.exit()

	try:
		import colorama
	except ImportError:
		 if raw_input("[!] Colorama module not found. Do you want install it?[Y/n] --> ").lower() == "y":
		 	installModule("colorama")
		 else:
		 	sys.exit()

	if "pyinstaller.exe" not in os.listdir(sys.exec_prefix + os.sep + "Scripts"):
		 if raw_input("[!] PyInstaller module not found. Do you want install it?[Y/n] --> ").lower() == "y":
		 	installModule("pyinstaller")
		 else:
		 	sys.exit()

	else:
		pass

	if "downloads" not in dirs:
		os.mkdir("downloads")
		print "[~] Directory created ==> 'downloads'"
	else:
		pass

	if "screenshots" not in dirs:
		os.mkdir("screenshots")
		print "[~] Directory created ==> 'screenshots'"

	else:
		pass

	if "executables" not in dirs:
		os.mkdir("executables")
		print "[~] Directory created ==> 'executables'"

	subprocess.Popen([sys.executable, 'vkng.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
	sys.exit()

if __name__ == "__main__":
	main()
