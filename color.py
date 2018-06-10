import subprocess
import sys
import os



os.system("./colorpane.sh")


DIRECTORY = "."
CONFIG_NAME = "config"
POLYBAR_BAR = "autumn"

def refreshPolybar():
    os.system("cp colors %s/config" % (DIRECTORY))
    os.system("cat %s/configbody >> %s/config" % (DIRECTORY, DIRECTORY))
    os.system("killall polybar")
    os.system("nohup polybar autumn &")


def readColors():
    with open("%s/colors" % (DIRECTORY), "r") as readfile:
        for line in readfile:
            print(line)



#Takes string and modifies color
def modifyLine():
    newfile = open('%s/newfile' % (DIRECTORY), 'w') 
    with open("%s/colors" % (DIRECTORY), "r") as readfile:
        for line in readfile:
            print((line.split("="))[0])
            newfile.write(changeColor(line))
    newfile.close


def changeColor(line, number=0):
    i=0
    while (i < len(line)):
        if line[i:].startswith('xrdb:color'):
            return line[:i+10] + str(number) + line[i+11:]
        i+=1
    
    return line
    
        

modifyLine()
    


