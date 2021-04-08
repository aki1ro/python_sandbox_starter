#!/usr/bin/python3
import os
import subprocess as sp
import time


def error(func):
    def wrap():
        try:
            func()
        except(KeyboardInterrupt):
            print("\nEXITING SCRIPT...")

    return wrap


def banner(func):
    def wrap():
        sp.run('reset')
        print("・‥…━━━━━━━━━━━━━☆☆━━━━━━━━━━━━━━━…‥・")
        print("°。°。°。°。°(*´￫ܫ￩｀*)。°。°。°。°。°")
        print("\n***SYSTEM CHECK SCRIPT***")
        func()
        print("△▼△▼n̶ ̶e̶ ̶v̶ ̶e̶ ̶r̶ ̶( ͜。 ͡ʖ ͜。) ̶m̶ ̶i̶ ̶n̶ ̶d̶ △▼△▼")
        print("・‥…━━━━━━━━━━━━━☆☆━━━━━━━━━━━━━━━…‥・")
        select()

    return wrap


@banner
def welcome():
    print("SELECT FROM THE FOLLOWING:\n\nQUICK INFO(0)\nSYSTEM INFO(1)\nSYSTEM ACTIVITY(2)\nSTORAGE(3)\nMEMORY(4)\nNETWORK(5)\nLOGS(6)\n")


@error
def select():
    x = (input("ENTER NUMBER FOR SELECTION(PRESS ENTER TO EXIT):"))
    if x == "0":
        quick_info()
    elif x == "1":
        system_info()
    elif x == "2":
        system_activity()
    elif x == "3":
        storage()
    elif x == "4":
        memory()
    elif x == "5":
        network()
    elif x == "6":
        logs()


def quick_info():
    sp.run('reset')
    print("\nCURRENT/TOTAL UPTIME:\n")
    sp.run("uptime")
    print("\nTOTAL ACTIVITY PER DAY PER USE(HOURS):\n")
    sp.run(["ac", "-pd"])
    print("\nCURRENT MEMORY USAGE:\n")
    sp.run(["free", "-h"])
    print("\nCPU/DISK USAGE/PERFORMANCE:\n")
    sp.run("iostat")
    print("\nHOSTNAME:\n")
    sp.run(['hostname', '-f'])
    print("\nCURRENT NETWORK CONFIGURATION:\n")
    sp.run("ifconfig")
    input("\nPRESS ENTER TO RETURN TO MENU...")
    welcome()


@error
def system_info():
    sp.run('reset')
    sp.run(['lshw', '-short'])
    sp.run(['dmidecode', '-t', 'bios'])
    input("\nPRESS ENTER TO RETURN TO MENU...")
    welcome()


@error
def system_activity():
    sp.run('reset')
    print("\nTOTAL USER ACTIVITY (HOURS):\n")
    sp.run(["ac", "-p"])
    print("\nTOTAL ACTIVITY PER DAY (HOURS):\n")
    sp.run(["ac", "-d"])
    print("\nCURRENT/TOTAL UPTIME:\n")
    sp.run("uptime")
    try:
        sp.run(["top", "-d", ".7"])
    except(KeyboardInterrupt):
        input("\nPRESS ENTER TO RETURN TO MENU...")
        welcome()


@error
def storage():
    try:
        sp.run(["iotop", "-o"])
    except(KeyboardInterrupt):
        sp.run('reset')
        print("\nCPU/DISK USAGE/PERFORMANCE:\n")
        sp.run("iostat")
        print("\nBLOCK/STORAGE DEVICES:\n")
        sp.run("lsblk")
        input("\nPRESS ENTER TO RETURN TO MENU...")
        welcome()


@error
def memory():
    sp.run('reset')
    print("\nCURRENT MEMORY USAGE:\n")
    sp.run(["free", "-h"])
    print("\nREALTIME MEMORY USAGE OVERALL(KB --> MB = DECIMAL TO THE LEFT x3):\n")
    sp.run(["cat", "/proc/meminfo"])
    input("\nPRESS ENTER TO RETURN TO MENU...")
    welcome()


@error
def network():
    print("\nCURRENT ROUTES:\n")
    sp.run(["netstat", "-r"])
    print("\nNETWORK CONFIGURATION:\n")
    sp.run(["ifconfig", "-v"])
    try:
        print("\nLIVE NETWORK PACKET ANALYZER:\n")
        sp.run("tcpdump")
    except(KeyboardInterrupt):
        input("\nPRESS ENTER TO RETURN TO MENU...")
        welcome()


@error
def logs():
    sp.run("reset")
    print("\nSELECT LOG:\n")
    print("\nmessages(0)\n")
    print("\nsecure(1)\n")
    print("\ncron(2)\n")
    x = input("* \nENTER NUMBER FOR LOG OR PRESS ENTER TO RETURN TO MENU:")
    try:
        if x == "0":
            sp.run('cat "/var/log/messages" | tail "-1000" | more', shell=True)
            input("\nPRESS ENTER TO RETURN TO LOG SELECT...")
            logs()
        elif x == "1":
            sp.run('cat "/var/log/secure" | tail "-1000" | more', shell=True)
            input("\nPRESS ENTER TO RETURN TO LOG SELECT...")
            logs()
        elif x == "2":
            sp.run('cat "/var/log/cron" | tail "-1000" | more', shell=True)
            input("\nPRESS ENTER TO RETURN TO LOG SELECT...")
            logs()
        else:
            print("\n\nRETURNING TO MAIN MENU...")
            time.sleep(1.5)
            welcome()
    except(KeyboardInterrupt):
        input("\nPRESS ENTER TO RETURN TO LOG SELECT...")
        logs()


welcome()
