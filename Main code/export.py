#Going to reuse code from SMP project
#This is supposed to be the final step after the conversion from blocks to code lines
#Saves the code string in a .py file
import os

#I think this should be deleted when this is officially added to the project
from pathlib import Path #Used to know the directory of the file
os.chdir(Path(__file__).parent) #Changes terminal directory to the one that has the file

def savepy(exponame,projcode):
    if not os.path.exists("{}.py".format(exponame)):
        pyW("{}.py".format(exponame),projcode)
        runcode("{}.py".format(exponame))
        return True
    else:
        print("file name exists")
        return False

def pyW(filename,projcode): #This could be used to write anyfile needed not just py ones
    file = open(filename, "w")
    file.write(projcode)
    print("Written!")
    file.close()

def runcode(filename): #Can be used to run the user's project after completion
    import subprocess
    subprocess.Popen(r'explorer /select,{}'.format(filename))
        
#Example of how this funtion needs to be called
# savepy("Test","print('This code works too!')")
# runcode("start_menu.py")