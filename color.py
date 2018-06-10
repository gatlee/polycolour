import subprocess
import sys
import os

os.system("./colorpane.sh")

print("hello")

directory = "./"

def refreshPolybar():
    os.system("cp colors config")
    os.system("cat configbody >> config")
    os.system("killall polybar")
    os.system("nohup polybar autumn &")


refreshPolybar()

