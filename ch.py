import random
from random import randint
import string
import uuid
import os
import time 
from time import sleep
from colorama import Fore
import sys
print("")
print(Fore.RED+" "+" Loading....")
sleep(2.0)
print("\n")
print(Fore.GREEN+"""
    upgrade Code ... 
  """)
sleep(2.0)
print("\n"*49)
print("""
  Load . . .
  """)
Dmo = """

My strongest filtering code
"""
for i in Dmo:
  sleep(0.02)
  print(i,end='',flush=True)
print()
sleep(2.1)
def random_string_generator(str_size, allowed_chars):
  return ''.join(random.choice(allowed_chars) for x in range(str_size))
chars = string.ascii_letters + string.punctuation
size = 28
print(Fore.GREEN+"    "+"["+"-_"*50+"]")
print(Fore.RED+'   Cod FIltering Chanel >> ',random_string_generator(size, chars))
print(Fore.GREEN+"    "+"["+"_"*50+"]")
input()