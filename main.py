import config as cfg
import json
import os
import wget 
from datetime import date as dt
# Move files to recycling bin and clean this according to setting in config
# ================
# Global Variables
# ================
PWD = 'C:\\PyWindowsCleaner\\'
DATE = dt.today()

def prelim():
    print("Prelim started")
    dirs = os.listdir('C:\\')
    count = 0
    found = False
    while count < len(dirs) and found != True:
        if dirs[count] == 'PyWindowsCleaner':
            found = True
        count += 1

    if found != True:
        print("Root folder not found. Creating")
        os.makedirs(PWD)
    sevenzip()

def checkFolderExists(folderName, path):
    dirs=os.listdir(path)
    found = False
    count = 0
    while count < len(dirs) and found != True:
        count += 1
        if dirs[count - 1] == folderName:
            print(folderName + "found")
            return True
    return False
    

def sevenzip():
    print("Checking if 7-Zip exist")
    if checkFolderExists("7-Zip", 'C:\\Program Files (x86)\\') != True:
        if checkFolderExists("7-Zip", 'C:\\Program Files\\') != True:
            print("7-Zip not found. Installing")
            wget.download('https://www.7-zip.org/a/7z1900.exe', PWD + "7-ZipSetup.exe")
            os.system('cmd /c ' + PWD + '7-ZipSetup.exe /S && del ' + PWD + '7-ZipSetup.exe')
            if checkFolderExists("7-Zip"< 'C:\\Program Files (x86)\\') != True:
                if checkFolderExists("7-Zip"< 'C:\\Program Files\\') != True:
                    print("7-Zip failed to install")
                else:
                    os.system('cmd /c set path=%path%;c:\program files\7-zip;')
            else:
                os.system('cmd /c set path=%path%;c:\program files (x86)\7-zip;')

def backup(data):
    print(data)
    backupFolders=data["Backup"]["BackupFolders"]
    zipPath=data["Backup"]["ZipTo"]
    for folder in backupFolders:
      break
      #os.system('
    # for each folder in backupFolders add the folder to the archive
    makeZip(zipPath)

def makeZip(path): 
    # 7zip archive
    pass

def clean(data): 
    pass

def main():
    # Check if this is first time running
    first_run = cfg.main()
    if first_run == 1:
        exit()
    else:
        jsonData = cfg.readConfig()
    prelim()
    backup(jsonData)
    clean(jsonData)


if __name__ == "__main__":
    main()
