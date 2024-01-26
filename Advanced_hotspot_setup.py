import csv
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
starting_number = input("What number do you need to lead with for your configuration? TGIF usually is 5 for example: ") # Which DMR network are you configuring? 
# BM does not need changing, TGIF usually is 5, DMR+ uses 8 for example. 
filename = filedialog.askopenfilename() # Opens file dialog to select your TG file
filepath = os.path.dirname(filename) # grab path for the original file so output files can be saved to same directory

for row in csv.reader((open(filename, 'r')), delimiter=','):
    if len(row[0]) < 7:
        row[0] = starting_number + row[0].rjust(6, '0') # if cell is less than 7 add your prefix digit and pad cell to 7
        csv.writer(open((filepath + "/TG_" + starting_number + "_list.csv"), 'a', newline='')).writerow(row) # write to TG_x_List.csv in same folder as original file
    elif len(row[0]) == 7 and row[0].startswith(starting_number): # already 7 digits, first digit matches what we want
        csv.writer(open((filepath + "/TG_" + starting_number + "_list.csv"), 'a', newline='')).writerow(row) # append to TG_x_List.csv
    elif row[0].startswith("T"): # strip out header row
        continue
    else:
        writer = csv.writer(open((filepath + "/TG_" + starting_number + "_Errorlog.csv"), 'a', newline='')) # outputs to TG_x_Errorlog.csv file
        writer.writerow(row) # result is 7 or more digits long and first digit not match the number we selected in begining, goes to error file

# Create text file of rewrite rules for your chosen network, saved to same location as the TG list

with open((filepath + "/DMR_Network_" + starting_number + "_ReWrite_rules.txt"), 'w') as f: # creating rules file with name DMR_Network_x_ReWrite_rules.txt
    f.write('\n'"[DMR Network " + starting_number + "]") # writing the lines of the file
    f.write('\n'"Enabled=1") # writing the lines of the file
    f.write('\n'"# you need to input you server address in next line, example tgif.network or 3102.master.brandmeister.network. Whatever your specific network uses.") # writing the lines of the file
    f.write('\n'"# If you do not know your network address, port or name there is a DMR_Hosts.txt file on your hotspot at /usr/local/etc/")
    f.write('\n'"Address=xxx.xxx.xxx.xxx")
    f.write('\n'"# Network port goes on next line, most are 62031, NOT ALL ARE THOUGH!!")
    f.write('\n'"Port=62031")
    f.write('\n'"# enter you network name in line below, TGIF Network, DMR+, FreeDMR,...")
    f.write('\n'"Name=xxxx")
    f.write('\n'"Debug=0")
    f.write('\n'"Location=1")
    f.write('\n'"# Your DMR ID goes in next line")
    f.write('\n'"Id=xxxxxx")
    f.write('\n'"# Your password for the specific network is next BM and TGIF only")
    f.write('\n''Password="Passw0rd"')
    f.write('\n'"# rewriting slot 1 and 2")
    f.write('\n'"PCRewrite1=1," + starting_number + "009990,1,9990,1")
    f.write('\n'"PCRewrite2=2," + starting_number + "009990,2,9990,1")
    f.write('\n'"TypeRewrite1=1," + starting_number + "009990,1,9990")
    f.write('\n'"TypeRewrite2=2," + starting_number + "009990,2,9990")
    f.write('\n'"TGRewrite1=1," + starting_number + "000001,1,1,999999")
    f.write('\n'"TGRewrite2=2," + starting_number + "000001,2,1,999999")
    f.write('\n'"SrcRewrite1=1,9990,1," + starting_number + "009990,1")
    f.write('\n'"SrcRewrite2=2,9990,2," + starting_number + "009990,1")
    f.write('\n'"SrcRewrite3=1,1,1," + starting_number + "000001,999999")
    f.write('\n'"SrcRewrite4=2,1,2," + starting_number + "000001,999999")
    f.write('\n'"# You will need to copy this information to your hotspot advanced configuration replacing whatever is there for the numbered network")
    f.write('\n'"# Once you have made changes to your configuration you will still need to modify your codeplug with your new talkgroups and create channels, groups and scan lists etc as your radio requires and update your radio")
    