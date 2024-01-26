# Advanced_Hotspot_Setup
Ham Radio DMR Hotspot multiple network configuration assistance.

This python script is written 2 make adding additional DMR networks on your Hotspot simpler.

This takes talk group cell padding script and adds the abilty to generate nearly complete talk group rewrite rules for each network.

- To use download the script, download talkgroup list from your desired network.
- Execute the script, enter the number you want as your first digit of your talkgroups on the command line then using the file browser select the talkgroup list file you saved earlier.
- The script will create either 2 or 3 files in the same directory you have your original talkgroup list saved in.
  1. First file is talkgroup list .csv with each talkgroup padded to 7 digits using your entry as the first digit.
  2. Second file is an error log .csv, only created if your talkgroup list has groups already using 7 digits and those leading digits don't match your desired number.
  3. Third file is a .txt file with your network settings and rewrite rules using your desired number matching your talkgroups.

 This should make setting up multiple networks a bit easier and help us all have options instead of just BM.
 You will need to add the following items to the network section:
 1. DMR ID
 2. Network passwords
 3. Server Address
 4. Server Port
 5. Server Name
Server address, port and name are available in a DMR_Hosts.txt file on your hotspot at /usr/local/etc/ in case you do not know them, they are also available online from each network website.
