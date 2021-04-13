'''
A module is basically a file containing a set of functions to include in your
application. There are core python modules, modules you can install using the pip
package manager (including Django) as well as custom modules

*** Packages contain modules, which contain functions: Package > Module > Function
'''



from platform import machine, processor, system, platform, version
from platform import python_version_tuple
from platform import python_implementation

inside = dir(platform) # <--- used to print names in namespace aka: functions within in a module
print(machine()) # <--- prints machine info ie: AMD64
print(system())  # <--- prints system info ie: Windows
print(platform()) # <--- prints platform info. ie: Windows-10-10.0.19041-SP0
print(processor()) # <--- prints processor info ie: AMD64 Family 23 Model 113 Stepping 0, AuthenticAMD
print(version()) # <--- prints version of OS ie: 10.0.19041 
print(python_version_tuple()) # <--- prints tuple of python version
print(python_implementation()) # <--- prints python implementation ie: CPython

for a in python_version_tuple():
   print(a)

for i in inside:
   print(i)
