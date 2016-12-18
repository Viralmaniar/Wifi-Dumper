# Wifi-Dumper
This is an open source tool to dump the wifi profiles and cleartext passwords of the connected access points on the Windows machine. This tool will help you in a Wifi testing. Furthermore, it is useful while performing red team or an internal infrastructure engagements.<br>
<img src=https://github.com/Viralmaniar/Wifi-Dumper/blob/master/Wifi-Dumper.PNG>
# Features
<i>Option 1:</i>Shows the wireless networks available to the system. If interface name is given, only the networks on the given interface will be listed. Otherwise, all networks visible to the system will be listed.<br>
<br>
<i>Option 2:</i> Shows a list of wireless profiles configured on the system.<br>
<br>
<i>Option 3:</i> Shows the allowed and blocked wireless network list.<br>
<br>
<i>Option 4:</i> Shows a list of all the wireless LAN interfaces on the system.<br>
<br>
<i>Option 5:</i> Generates a detailed report about each wireless access point profile on the system. Group Policy Profiles are read only. User Profiles are readable and writeable, and the preference order can be changed.<br>
<br>
<i>Option 6:</i> Dumps the cleartext passwords of every wireless profiles on the system. Make sure to generate the profile file (by selecting option 2) before running this option. Always run this as an administrator user to see the cleartext password. User needs to provide individual wireless name by reading the profile names(option 7). <br>
<br>
<i>Option 7:</i> It opens the list of wireless profiles on the system using notepad.<br>
<br>
<i>Option 8:</i> It saves WLAN profiles to XML files.<br>

<i>Option 9:</i> Exit gracefully.<br>

# General Notes
[+] Each option in the tool generates the ".txt" file as an output.<br>
[+] If you run the tool multiple times, the output gets appended to the previous results.

# How to run the application?
[+] Run cmd.exe as an administrator.<br>
[+] Change Directory<br>
[+] Run the application as C:\\>python wifi_dumper.py

# Questions?
Twitter: https://twitter.com/maniarviral<br>
LinkedIn: https://au.linkedin.com/in/viralmaniar

