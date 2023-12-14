import os
print(os.getcwd())
os.chdir('F:/src')
print(os.getcwd())
print(os.path.basename('F:/src/git/GBPython/L04/map.py'))
print(os.path.abspath('map.py'))