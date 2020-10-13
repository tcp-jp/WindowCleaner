import json


def orgIni(): 
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
          },
          "Backup" : {
              "PerformBackup" : 1,
              "BackupFolders" : [],
              "ZipTo" : "E:\\SystemBackups\\"
          }
      }

    with open('config.json','w') as config: 
        json.dump(default_config, config)
        config.close()

def readConfig():
    with open('config.json','r') as config:
        jsonData=json.load(config)
        return jsonData

def compareConfigs():
    pass


def main():  
    try: 
      with open('config.json','r') as config: 
        config = json.load(config)
        return 0
    except:
      print("No config file exists. Creating") 
      orgIni()
      return 1
 

if __name__ == "__main__": 
    main()

