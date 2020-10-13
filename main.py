import config as cfg
import os
import downloader 
from datetime import date as dt

# Move files to recycling bin and clean this according to setting in config


# ================
# Global Variables 
# ================
PWD = 'C:\\PyWindowsCleaner\\'
DATE = dt.today()


# Needs to make folder PWD


def sevenzip(): # { 
    print("Checking if 7-Zip exist")
    dirs = os.listdir('C:\\Program Files (x86)\\')
    dirs += os.listdir('C:\\Program Files\\')
    found = False
    count = 0
    while count < len(dirs) and found != True:
        print(dirs[count], count)
        count += 1
        if dirs[count - 1] == '7-Zip': 
            print("7-Zip found")
            found = True
    if found != True: 
        print("7-Zip not found. Installing")
        download=downloader.Download('ttps://www.7-zip.org/a/7z1900.exe', PWD + "7-ZipSetup.exe")
        os.system('cmd /c ' + PWD + '7-ZipSetup.exe /S && del ' + PWD + '7-ZipSetup.exe')
#} 


def storeData(): #{ 
    pass
#}


def backup(): # { 
    pass
#}

def zip(): # { 
    pass
#}

def clean(): # { 
    pass

#}


def main(): # { 
    # Check if this is first time running
    first_run = cfg.main();
    if first_run == 1: 
        exit();
    else: 
        jsonData = first_run
    sevenzip()

    # Back upper
        # Zipper
    # Cleaner 



#}
      


if __name__ == "__main__": 
    main()




