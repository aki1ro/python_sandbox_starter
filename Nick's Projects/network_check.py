import subprocess as sp
import time as t
import os


def cmd(x):
    if x == "d":
        disable(x)
    elif x == "e":
        enable(x)
    elif x == "c":
        status_check()


def status_check():
    interface = str(sp.check_output('netsh interface show interface "Ethernet"')).split()
    print(sp.run('netsh interface show interface "Ethernet"'))
    for i in interface:
        if i == "Disconnected":
            print("Adapter was found disabled, fixing now.")
            print("Adapter is currently being disabled")
            sp.run('netsh interface set interface "Ethernet" disable')
            print("Waiting 6 seconds before enabling adapter")
            t.sleep(6)
            print("Adapter is currently being enabled")
            sp.run('netsh interface set interface "Ethernet" enable')
            cmd(input(
                "Check Complete. press enter to exit or type 'd' to disable or 'e' to enable adapter or 'c' to check adapter status: "))
        if i == "Connected":
            print("Adapter is Connected")
            cmd(input(
                "Check Complete. press enter to exit or type 'd' to disable or 'e' to enable adapter or 'c' to check adapter status: "))


def disable(d):
    if d == "d":
        print("Adapter is currently being disabled")
        sp.run('netsh interface set interface "Ethernet" disable')
        cmd(input(
            "Disable Complete. press enter to exit or type 'd' to disable or 'e' to enable adapter or 'c' to check adapter status: "))


def enable(e):
    if e == "e":
        print("Adapter is currently being enabled")
        sp.run('netsh interface seinterface "Ethernet" enable')
        cmd(input(
            "Enable Complete. press enter to exit or type 'd' to disable or 'e' to enable adapter or 'c' to check adapter status: "))


status_check()
