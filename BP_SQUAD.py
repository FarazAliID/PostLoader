import os, platform, time, sys
print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mChecking For Update...')
os.system('git pull --quiet 2>/dev/null')
os.system("curl -L https://raw.githubusercontent.com/K0J4/files/main/bp32.cpython-311.so -o bp32.cpython-311.so")
os.system('xdg-open https://chat.whatsapp.com/KThLuumIszgD0UCJz3T33C')
mrkoja = platform.architecture()[0]
if mrkoja == '64bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Device is 64bit');time.sleep(2)
 os.system('chmod 777 BP_SQUAD && ./BP_SQUAD')
elif mrkoja == '32bit':
 print('\033[1;97m[\033[1;91m+\033[1;91m] \033[1;97mYour Devive is 32bit');time.sleep(2)
 import bp32
