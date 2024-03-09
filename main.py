#!/usr/bin/python3
import os
import glob
import sys
import argparse

def printDir(path, logfile=None):    # function to print all contents in the dir. base command
    output=[]           # output list for log file if applicable
    counter=1
    if os.path.exists(path):                # makes sure path exists
        if not logfile:
            # table formatting if content is to be displayed (not going to log)
            print(f"{'File/Dir #':<10} {'Name':<30}")
            print(f"{'********':<10} {'*******************':<25}")
        for file in os.listdir(path):                               # iterates through every file

            if logfile:
                output.append(file)                         # if logfile option true, append to list output
            else:
                print(f"{counter:<10} {file:<25}")          # else print to console
                counter=counter+1
        if len(output)>0 and logfile:
            logFile(output,logfile)                 # once finished, if logfile option, call function to make file

    else:
        print('Error: path not found')

def onlyDirectories(path, logfile=None):
    counter=1
    output=[]
    if os.path.exists(path):                # same as previous function
        if not logfile:
            print(f"{'File/Dir #':<10} {'Name':<30}")
            print(f"{'********':<10} {'*******************':<25}")

        for item in os.listdir(path):
            if os.path.isdir(os.path.join(path, item)):
                if logfile:
                    output.append(item)         # append to ooutput list for logfile
                else:

                    print(f"{counter:<10} {item:<25}")
                    counter=counter+1

        if len(output)>0 and logfile:
            logFile(output,logfile)             # call logFile function, pass output into it
    else:
        print("Error: path not found")
def logFile(output,name):
    with open(name, 'w') as file:       # create logfile
        for line in output:         # iterate through given list
            file.write(line +'\n')      # write everything to file
        file.close()



def main():
    parser=argparse.ArgumentParser(description='returns contents in a directory')       # parser setup
    parser.add_argument('DIR_PATH',type=str, help='Path to the directory')  # main argument
    parser.add_argument('-i','--logfile',type=str,help='name of logfile to output to')  #-i logile argument
    # -d directories only argument, used as boolean for later logic
    parser.add_argument('-d','--dir',action='store_true',help='return only directories found in a given path')
    args=parser.parse_args()
    # logic to determine which functions to call based on given arfuments
    if args.dir:
        onlyDirectories(args.DIR_PATH,args.logfile)
    else:
        printDir(args.DIR_PATH, args.logfile)


main()
