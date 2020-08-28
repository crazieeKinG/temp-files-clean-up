# Dependencies
import os
from subprocess import run
from time import sleep

# User modules
import temp_modules as tm
import temp_clear as tc
import enableRunAtStartUp as es

# pip installl elevate
check_pip = run(["pip"], shell=True, capture_output=True).returncode
if check_pip == 1:
    print("INSTALLING PIP...")
    run(["python", "get-pip.py"], shell=True)
check_elevate = run(
    ["pip", "show", "elevate"], shell=True, capture_output=True
).returncode
if check_elevate == 1:
    print("INSTALLING ELEVATE...")
    run(["pip", "install", "elevate"], shell=True)
from elevate import elevate

# Creating startup file
es.createBat()
# Start
print(f"Admin priviledge:: { tm.is_root() }")
if not tm.is_root():
    print("\nPlease provide ADMINISTRATOR priviledge")
    sleep(1)
try:
    elevate(True)
except:
    quit()
print("\nTEMPORARY FILES CLEAN UP v3.0")

temp_path = list()
# user temp folder
temp_path.append(os.environ.get("TEMP", ""))
# windows temp folder
windir = os.environ.get("windir", "")
temp_path.append("{}\\TEMP".format(windir))
# windows prefetch folder
temp_path.append("{}\\Prefetch".format(windir))
# clean up all folder
for temp_folder in temp_path:
    tc.main(temp_folder)
# END
input("Press ENTER to exit...")
