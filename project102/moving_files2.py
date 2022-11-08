import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/user/Downloads"
to_dir = "C:/Users/user/Desktop/moved_files"

listOfFiles = os.listdir(from_dir)

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event.src_path + "has been created")
        return super().on_created(event)

    def on_deleted(self, event):
        print(event.src_path + "has been deleted")
        return super().on_deleted(event)
    
    def on_modified(self, event):
        print(event.src_path + "has been edited or modified")
        return super().on_modified(event)
    
    def on_moved(self, event):
        print(event.src_path + "has been moved") 
        return super().on_moved(event)

eventHandler = FileEventHandler()
observer = Observer()
observer.schedule(eventHandler, from_dir, recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")   
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()