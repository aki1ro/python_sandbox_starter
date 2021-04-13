#!/usr/bin/env python3

# This is a module designed for use with certain monkey actions performed, may print
# random bananas and also have the monkeycat saying whatever it is you want.
import platform as p
from random import randrange
__counter = 0 


def monkeytime():
   print("✺◟(⏒□⏒)◞✺ ✺◟(⏒□⏒)◞✺ ✺◟(⏒□⏒)◞✺ ✺◟(⏒□⏒)◞✺ ✺◟(⏒□⏒)◞✺")
   print("IT'S MONKEY TIME")
   print("✺◟(⏒□⏒)◞✺ ✺◟(⏒□⏒)◞✺ ✺◟(⏒□⏒)◞✺ ✺◟(⏒□⏒)◞✺ ✺◟(⏒□⏒)◞✺")

 
def monkeysee():
   global __counter
   __counter += 1
   print(p.platform())
   print(p.processor())
   print(p.system())


def monkeydo(r = randrange(10)):
   global __counter
   __counter += 1
   banana = "'-..___     __.='>\n`.     '''''   ,'\n'-..__   _.-'"
   return f"Random Banana looking objects coming your way!!!\n{banana * r}\n*Monkey threw {r} bananas at you!"
   

def monkeycat(to_say):
   global __counter
   __counter += 1
   print("──────▄▀▄─────▄▀▄\n─────▄█░░▀▀▀▀▀░░█▄\n─▄▄──█░░░░░░░░░░░█──▄▄\n█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█")
   print(f"I AM THE GREAT MONKEYCAT\nAND TODAY I'M GOING\nTO SAY THIS TO YOU:\n{to_say}")


if __name__ == '__main__':
   print("I'm a module running in the terminal")
