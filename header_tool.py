import os
import time
import arrow

class Header_Tool:
    def __init__(self, target):
        self.target_file = target

    def _print_modified_time(self):
        modTimesinceEpoc = os.path.getmtime(self.target_file)
        # Convert seconds since epoch to readable timestamp
        modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
        print("Last Modified Time : ", modificationTime)
