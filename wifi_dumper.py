#!/usr/bin/python
'''
This is an open source tool to dump the wifi profiles and cleartext passwords on the Windows machine. This tool will help you in a Wifi testing. Furthermore, it is useful while performing red team or an internal infrastructure engagements. 

Author: Viral Maniar 
Twitter: https://twitter.com/maniarviral
Github: https://github.com/Viralmaniar
LinkedIn: https://au.linkedin.com/in/viralmaniar

'''
import os
import subprocess
from subprocess import check_output
import sys
	
def logo():
	logo='''
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
			
def menu():
    while True:
        try:
            choice = str(input('[?] Do you want to continue?')).lower()
            if choice[0] == 'y':
                main()
                break
            if choice[0] == 'n':
                sys.exit(0)
                break
        except ValueError:
            sys.exit(0)

def main():
	os.system('cls')
	print (logo())
	try:
			if os.name == "nt":
				print ('[+] All good....')
			elif os.name != "nt":
				print ('[!] Please run the application on Windows machine')
				sys.exit(0)

			while True:
				try:
					choice = int(input("\n[?] What do you want to perform?\n\n1. List of Available SSID \n2. List Wireless Profiles\n3. List of Blocked Wireless Access Points\n4. Detailed Information about Current Wireless Interface (Including SNR)\n5. Generate Full Report\n6. Show Cleartext Passwords\n7. Open Profiles\n8. Dump Encrypted Profiles (XML files)\n9.  Exit"))
				except ValueError:
					print ('[!] Enter Only a Number')
					continue
			
				if choice == 1:
					print (check_output("netsh wlan show networks >> networks.txt", shell=True))
					print ("Report printed as networks.txt file")
					print("\n")
					menu()
					break
				if choice == 2:
					print (check_output("netsh wlan show profiles >> profiles.txt", shell=True))
					print ("Report printed as profiles.txt file")
					print("\n")
					menu()
					break
				if choice == 3:
					print (check_output(" netsh wlan show filters >> blocked.txt", shell=True))
					print ("Report printed as blocked.txt file")
					print("\n")
					menu()
					break
				if choice == 4:
					print (check_output(" netsh wlan show interfaces >> Interface_info.txt", shell=True))
					print ("Report printed as Interface_info.txt file")
					print("\n")
					menu()
					break
				if choice == 5:
					print (check_output("netsh wlan show all >> Full_Report.txt", shell=True))
					print ("Report printed as Full_Report.txt file")
					print("\n")
					menu()
					break
				if choice == 6:
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
					menu()	
					break
				if choice == 7:
					print (check_output("notepad profiles.txt", shell=True))
					menu()
					break
				if choice == 8:
					print (check_output("netsh wlan export profile folder=.", shell=True))
					print ("Wireless profiles exported as XML files")
					print("\n")
					menu()
					break
				if choice == 9:
					sys.exit(0)
					
				else:
					print ('[!] Invalid Choice')
						
	except KeyboardInterrupt:
			print ('[!] Ctrl + C detected\n[!] Exiting')
			
	except EOFError:
			print ('[!] Ctrl + D detected\n[!] Exiting')
			sys.exit(0)

if __name__ == "__main__":
    main()