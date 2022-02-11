# importing tkinter module
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import time
import threading
import os
import sys

# creating tkinter window
root = Tk()
  
# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
              length = 800, mode = 'determinate')
  
# Function responsible for the updation
# of the progress bar value
def bar(size, speed):
    running = True
    while running:
        
        units = 100 / (size / speed)
    
        progress['value'] += units
        root.update_idletasks()
        time.sleep(1)

        if progress['value'] >= 100:
            progress.stop()
            running = False

  
def thread():
    thread1 = threading.Thread(target=bar, args=(round(target_size), upload_speed))
    thread1.start()


      
progress.pack(pady = 10)



test_file = sys.argv[1]

upload_speed = 2.5

target_size = round(int(os.path.getsize((test_file)) / 1000) / 1000)

total_transfer_time = target_size / upload_speed

root.title(str(target_size) + " MB")



# This button will initialize
# the progress bar
Button(root, text = 'Start', command = thread).pack(pady = 10)
  
# infinite loop
root.mainloop()
