#   A module to be used with other programs/projects to make
#   regular system tasks easy.
#
#
#   Create by: Riley Larche (Program Counter)
#   Date Created: 2019-05-19
#   Date Modified: 2015-05-20
#   Python Version: 3.7.2
#   Atom 1.37

#
#Functions
def GetCWD(mod):
    #Gets the current working directory, and modifies it if mod given
    CWD = os.getcwd()

    if mod[0] == '+':
        CWD += mod
        return CWD
    elif mod[0] == '-':
        CWD = CWD.replace(mod, '')
        return CWD
    return CWD

def Error(ex):
    #Used in an 'except', prints the error to screen, then quits.
    print("[ERROR] An exception has been made: {error}".format(error = ex))
    print("[INFO] Quitting...")

#def Console():
    #print("[{Catagory}] {Message}")

def GetLocalIP():
    #get the machines local IP, code is in portal 2 logbook

def LoadModules():
    #Check system for installed python modules. Install them if they are missing. Load them if they are installed.

def AptCheck():
    #check apt for installed system libraies and apps. Install them if they are missing.
