import json

def orgIni(): # {
    default_config = { 
          "ExcludedFolders" : { 
              # Default OS folders...
              "SystemFolders" : ['C:\\Windows\\', 'C:\\Program Files\\', 'C:\\Program Files (x86)\\',
                  'C:\\ProgramData\\', 'C:\\PerfLogs\\', 'C:\\Users\\'],
              "UserFolders" : [] # Follow same format as above for folders you do not want cleared
          },
          "ForcedFolders" : { 
              "SystemFolders" : [],
              "UserFolders" : []
          },
          "FileNameRegexPatterns" : { 
              "SystemPatterns" : [],
              "UserPatterns" : []
          },
          "Excluded File Types" : { 
              "SystemFileTypes" : [],
              "UserFileTypes" : []
          },
          "Forced File Types" : { 
              "SystemFileTypes" : [],
              "UserFileTypes" : []
          }
      }

    with open('config.json','w') as iniFile: 
        json.dump(default_config, iniFile);
        iniFile.close();
# }

def readIni(iniFile): # { 
      config = json.load(iniFile);
      iniFile.close();
# } 

def main(): # { 
    # search for ini
        # if exists read
        # else 
    try: 
      with open('config.json','r') as iniFile: 
        readIni(iniFile);
        return readIni
    except:
      print("No config file exists. Creating") 
      orgIni()
      return 1
# } 

if __name__ == "__main__": 
    main()

