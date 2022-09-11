import os, re
from dotenv import load_dotenv
load_dotenv()

class Settings:
    def __init__(self,):
        for k, v in os.environ.items():
            if 'ENV_' in k:
                self.set(re.sub('ENV_', '', k).lower(), v)
    
    def set(self, name, value=None):
        setattr(self, name, value)
        
    def get(self, name):
        try:
            return getattr(self, name)
        except Exception as e:
            return None
            
    def __del__(self,):
        try:
            del self
        except:
            pass