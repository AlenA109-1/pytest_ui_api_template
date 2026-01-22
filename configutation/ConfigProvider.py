import configparser

config = configparser.ConfigParser()
config.read('mytest_config.ini')

class ConfigProvider:

    def __init__(self) -> None:
        self.config = config
        
    def get(self, section: str, prop: str):
        return self.config[section].get(prop)

    def get_ui_url(self):
        return self.config["ui"].get("base_url")
    
    def get_api_url(self):
        return self.config["api"].get("base_url")
    
    def getint(self, section: str, prop: str):
        return self.config[section].getint(prop)