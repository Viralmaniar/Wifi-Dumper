#!/usr/bin/python
'''
This is an open source tool to dump the wifi profiles and cleartext passwords on a Windows machine.
It will help you with Wifi testing. Furthermore, it is useful while performing red team or an internal infrastructure engagements.

Author: Viral Maniar 
Twitter: https://twitter.com/maniarviral
Github: https://github.com/Viralmaniar
LinkedIn: https://au.linkedin.com/in/viralmaniar

'''
import os, sys
import subprocess
from subprocess import check_output
	
def logo():
	logo = '''
 __      __ .__ ___________.__          ________                                          
/  \    /  \|__|\_   _____/|__|         \______ \   __ __   _____  ______    ____ _______ 
\   \/\/   /|  | |    __)  |  |  ______  |    |  \ |  |  \ /     \ \____ \ _/ __ \\_  __ \
 \        / |  | |     \   |  | /_____/  |    `   \|  |  /|  Y Y  \|  |_> >\  ___/ |  | \/
  \__/\  /  |__| \___  /   |__|         /_______  /|____/ |__|_|  /|   __/  \___  >|__|   
       \/            \/                         \/              \/ |__|         \/        
[+] Author: Viral Maniar
[+] Twitter: @ManiarViral
[+] Description: Wifi Profiles and Password Dumper for Windows.
[+] Note: Run the application as administratror to see the clear-text passwords.

'''
	return logo

OPTIONS = '''
[?] What do you want to perform?

1. List of Available SSID
2. List Wireless Profiles
3. List of Blocked Wireless Access Points
4. Detailed Information about Current Wireless Interface (Including SNR)
5. Generate Full Report
6. Show Cleartext Passwords
7. Open Profiles
8. Dump Encrypted Profiles (XML files)
9.  Exit
'''

def menu():
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? \n> ')).lower()
			if choice[0] == 'y':
				return
			if choice[0] == 'n':
				sys.exit(0)
				break
		except ValueError:
			sys.exit(0)

def checkHostWindows():
	if os.name == "nt":
		print ('[+] All good....')
	else:
		print ('[!] Please run the application on Windows machine')
		sys.exit(0)

def cmd_listAvailableSSIDs():
	print (check_output("netsh wlan show networks >> networks.txt", shell=True))
	print ("Report printed as networks.txt file")
	print("\n")

def cmd_listProfiles():
	print (check_output("netsh wlan show profiles >> profiles.txt", shell=True))
	print ("Report printed as profiles.txt file")
	print("\n")

def cmd_listBlockedAPs():
	print (check_output(" netsh wlan show filters >> blocked.txt", shell=True))
	print ("Report printed as blocked.txt file")
	print("\n")

def cmd_showCurrentInterface():
	print (check_output(" netsh wlan show interfaces >> Interface_info.txt", shell=True))
	print ("Report printed as Interface_info.txt file")
	print("\n")

def cmd_genFullReport():
	print (check_output("netsh wlan show all >> Full_Report.txt", shell=True))
	print ("Report printed as Full_Report.txt file")
	print("\n")

def cmd_showCleartext():
	print ("\n")
	print ("------------------------------------------------------------------------------------")
	print ("\n[*] Make sure you've selected Option (2) and Option (7) before running Option (6)")
	print ("\n[*] Always run this application as an administratror to see the cleartext passwords")
	print ("--------------------------------------------------------------------------------------")
	ap_selector = input("Enter the name of the Access Point:")
	if ap_selector == "":
		print ("[!] Enter the Correct Wireless Access Point Name.")
	else: 
		print (check_output("netsh wlan show profiles name=" + ap_selector +" key=clear >> Plaintext_Credentials.txt", shell=True))
		print ("Check plaintext credentials in Plaintext_Credentials.txt file (Key Content) ")
		print("\n")

def cmd_openProfiles():
	print (check_output("notepad profiles.txt", shell=True))

def cmd_dumpEncryptedProfiles():
	print (check_output("netsh wlan export profile folder=.", shell=True))
	print ("Wireless profiles exported as XML files")
	print("\n")

cmds = {
	"1" : cmd_listAvailableSSIDs,
	"2" : cmd_listProfiles,
	"3" : cmd_listBlockedAPs,
	"4" : cmd_showCurrentInterface,
	"5" : cmd_genFullReport,
	"6" : cmd_showCleartext,
	"7" : cmd_openProfiles,
	"8" : cmd_dumpEncryptedProfiles,
	"9" : lambda: sys.exit(0)
}

def main():
	os.system('cls')
	print (logo())
	checkHostWindows()
	try:
		while True:
			choice = input("\n%s" % OPTIONS)
			if choice not in cmds:
				print ('[!] Invalid Choice')
				continue
			cmds.get(choice)()
	except KeyboardInterrupt:
		print ('[!] Ctrl + C detected\n[!] Exiting')
		sys.exit(0)
	except EOFError:
		print ('[!] Ctrl + D detected\n[!] Exiting')
		sys.exit(0)

if __name__ == "__main__":
	main()
