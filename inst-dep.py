#for all dependecys
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("pyautogui") 
install("opencv_python") 
