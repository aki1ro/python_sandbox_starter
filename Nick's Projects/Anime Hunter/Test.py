
# Episodes = []

# n = 1
# while n < 20:
#    if n > 9:
#       e = "Episode "
#       e = e + str(n)
#       Episodes.append(e,)
      
      
      
#    else:
#       e = "Episode 0"
#       e = e + str(n)
#       Episodes.append(e,)
      
#    n = n + 1
      


# print(Episodes)

import fnmatch
a = "Boku no Hero Academia"
el = ['Boku no Hero Academia — 90', '480p720p1080pXDCC', 'New!', 'Boku no Hero Academia — 89', '480p720p1080pXDCC', '03/27/21']

el = fnmatch.filter(el, (a + "*"))

print(el)