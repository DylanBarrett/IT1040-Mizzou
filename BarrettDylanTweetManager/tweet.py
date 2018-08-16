# Import the time module
import time

# Define class
class Tweet:
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()
        
    def get_author(self):
        return self.__author
    
    def get_text(self):
        return self.__text
    
    def get_age(self):
        now = time.time()
        difference = now - self.__age
        hours = difference // 3600
        difference = difference % 3600
        minutes = difference // 60
        seconds = difference % 60
        
        hours = str(int(hours))
        minutes = str(int(minutes))
        seconds = str(int(seconds))
        
        if int(hours) > 0:
            return hours + "h"
        
        elif int(minutes) > 0:
            return minutes + "m"
        
        else:
            return seconds + "s"
    
