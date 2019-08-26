from subprocess import *
import time
Popen('python GUI.py')
time.sleep(1)
Popen('python DataProcessing-and-Firebase-Part.py')
time.sleep(1)
Popen('python Data.py')
time.sleep(1)


