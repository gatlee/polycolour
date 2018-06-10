import subprocess
import sys
import os





DIRECTORY = "./"
CONFIG_NAME = "config"
POLYBAR_BAR = "autumn"

def refreshPolybar(array):
    with open("%scolors" % (DIRECTORY), "w") as writefile:
        for i in array:
            writefile.write(i)

    os.system("cp %scolors %sconfig" % (DIRECTORY, DIRECTORY))
    os.system("cat %sconfigbody >> %sconfig" % (DIRECTORY, DIRECTORY))
    os.system("killall polybar")
    os.system("nohup polybar autumn &")
    subprocess.call(["nohup", "polybar", "autumn", "&"], shell=False, stdout = open('/dev/null', "w"))
    os.system("clear")
    os.system("./colorpane.sh")






#Takes string and modifies color
def getVarName(rawLine):
    return (rawLine.split("="))[0]


def getCurrent(rawLine):
    line = rawLine
    i=0
    while (i < len(line)):
        if line[i:].startswith('xrdb:color'):
            return line[i+10]
        i+=1



def main():
    os.system("./colorpane.sh")
    colorArray = genColorArray()
    start = 0 
    for i in range(len(colorArray)):
        if start == 1:
            colorIndex = input("What colour would you like %s to be? Currently: %s" \
                    % (getVarName(colorArray[i]), getCurrent(colorArray[i])   ))
            modifyArray(colorArray, i, colorIndex)
            refreshPolybar(colorArray)

        elif colorArray[i].startswith("[colors]"):
            start = 1
        else:
            pass



def modifyArray(array, index, value):
    line = array[index] 
    if (value == ""):
        return
    else:
        i = 0
        while (i < len(line)):
            if line[i:].startswith('xrdb:color'):
                line = line[:i+10] + str(value) + line[i+11:]
            i+=1
        array[index] = line 

            
def genColorArray():
    outputArray = []
    
    with open("%scolors" % (DIRECTORY), "r") as readfile:
        for line in readfile:
            outputArray.append(line)
    return outputArray
     
    
        

main()    


