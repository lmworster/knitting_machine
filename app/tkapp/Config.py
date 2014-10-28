import ConfigParser

class Config:
    def __init__(self):

        try:
            cfgFile = open('config.cfg','rb')
            config = ConfigParser.ConfigParser({'simulateEmulator':'False'},
                                               allow_no_value=True)
            config.readfp(cfgFile)
            self.imgdir = config.get('UserPrefs','imgdir')
            self.datFile = config.get('UserPrefs','datFile')
            self.device = config.get('UserPrefs','device')
            self.simulateEmulator = config.get('UserPrefs','simulateEmulator')
        except (OSError, IOError):
            self.imgdir = ""
            self.datFile = ""
            self.device = ""
            self.simulateEmulator = False

        cfgFile.close()